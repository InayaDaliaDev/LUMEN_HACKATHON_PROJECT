"""
core/ai_engine.py — shared LLM plumbing for every AI-powered page.
Extracted from what used to be near-identical code copy-pasted across
03_Mr.Brown.py, 04_What_If.py and 05_TheOldDays.py: the model fallback
chain, the actual LLM invocation, the streaming loop, and error
classification (including the dev_mode gate that decides whether the
user sees a raw technical error or a friendly one).
What STAYS in each page (on purpose, not duplication — these are
genuinely different per page):
  - The system prompt content (persona, rules)
  - The page's own LangGraph state shape and node wiring
  - The Streamlit UI (forms, layout)
Usage in a page's node function:
    from core.ai_engine import invoke_llm_with_fallback
    def mentor_node(state, config):
        cfg = (config or {}).get("configurable", {})
        system_prompt = build_system_prompt(state)  # page-specific
        response = invoke_llm_with_fallback(
            system_prompt=system_prompt,
            history_messages=state.get("messages", []),
            api_key=cfg.get("api_key", ""),
            model=cfg.get("model", "gemini-2.5-flash"),
            temperature=cfg.get("temperature", 0.55),
            timeout=cfg.get("timeout", 45),
        )
        return {"messages": [response]}
Usage for the top-level streaming call (replaces each page's own
stream_turn function):
    from core.ai_engine import stream_graph_response
    full_response, error_message = stream_graph_response(
        app=mentor_app,
        input_state=input_state,
        config=build_config(),
        placeholder=message_placeholder,
        node_filter={"mentor"},   # only stream tokens from this node; None = all nodes
    )
    if error_message:
        st.error(error_message)
"""
import time
import streamlit as st
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_core.messages import trim_messages
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
except ImportError:
    ChatGoogleGenerativeAI = None
    trim_messages = None
    ChatPromptTemplate = None
    MessagesPlaceholder = None
try:
    from google.api_core import exceptions as google_exceptions
    HAS_GOOGLE_EXCEPTIONS = True
except ImportError:
    HAS_GOOGLE_EXCEPTIONS = False
from core.utils import extract_text
# ==============================================================================
# MODEL FALLBACK CHAIN
# ==============================================================================
DEFAULT_FALLBACK_MODELS = ["gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-flash-latest"]
def build_fallback_chain(primary_model: str) -> list:
    """Primary model first, then the default fallbacks, de-duplicated
    while preserving order (so the primary isn't tried twice if it's
    already one of the defaults)."""
    chain = [primary_model] + DEFAULT_FALLBACK_MODELS
    seen = []
    for m in chain:
        if m not in seen:
            seen.append(m)
    return seen
# ==============================================================================
# HISTORY TRIMMING
# ==============================================================================
def trimmed_history(messages, max_tokens: int = 24):
    """Keeps the last N messages (using message-count as a stand-in for
    token count, same approach every page was already using)."""
    if not messages:
        return []
    return trim_messages(
        messages,
        strategy="last",
        token_counter=len,
        max_tokens=max_tokens,
        start_on="human",
    )
# ==============================================================================
# LLM INVOCATION WITH FALLBACK
# ==============================================================================
def invoke_llm_with_fallback(
    system_prompt: str,
    history_messages: list,
    api_key: str,
    model: str,
    temperature: float,
    timeout: int,
    max_history_tokens: int = 24,
):
    """
    Builds the prompt, tries each model in the fallback chain in order,
    and returns the first successful response. Raises the last exception
    if every model in the chain fails — callers should catch this
    (stream_graph_response already does, if you use it for the outer loop).
    """
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder("history"),
    ])
    last_exception = None
    for model_name in build_fallback_chain(model):
        try:
            llm = ChatGoogleGenerativeAI(
                model=model_name,
                google_api_key=api_key,
                temperature=temperature,
                timeout=timeout,
                max_retries=1,
            )
            chain = prompt_template | llm
            return chain.invoke({"history": trimmed_history(history_messages, max_history_tokens)})
        except Exception as e:
            last_exception = e
            continue
    raise last_exception if last_exception else RuntimeError("All model execution attempts failed.")
# ==============================================================================
# ERROR CLASSIFICATION — gated by st.session_state.dev_mode
# ==============================================================================
def classify_error(e: Exception):
    """
    Returns (is_transient: bool, user_facing_message: str).
    When st.session_state.dev_mode is truthy (set by the cheat code in
    01_Assessment.py), the raw exception type/message is shown. Otherwise
    everyone gets a clean, non-technical message — no more raw JSON error
    dicts shown to a regular user.
    """
    dev_mode = bool(st.session_state.get("dev_mode"))
    transient = False
    message = None
    if HAS_GOOGLE_EXCEPTIONS:
        if isinstance(e, google_exceptions.PermissionDenied):
            message = "🔒 Access denied — the API key is invalid or lacks permission."
        elif isinstance(e, google_exceptions.Unauthenticated):
            message = "🔒 Authentication failed — check your API key."
        elif isinstance(e, google_exceptions.InvalidArgument):
            message = "⚠️ Invalid request — check the selected model."
        elif isinstance(e, google_exceptions.ResourceExhausted):
            transient = True
            message = "⏳ Rate limit or quota reached. Retrying..." if dev_mode else "⏳ High demand right now — retrying automatically..."
        elif isinstance(e, (google_exceptions.DeadlineExceeded, google_exceptions.ServiceUnavailable)):
            transient = True
            message = "🌐 Temporary network or service issue. Retrying..."
    if message is None:
        transient = True
        if dev_mode:
            message = f"❌ Engine issue ({type(e).__name__}: {str(e)})."
        else:
            message = "🤖 The AI engine is temporarily unavailable — this usually means high demand. Try again in a few seconds."
    return transient, message
# ==============================================================================
# STREAMING LOOP
# ==============================================================================
def stream_graph_response(
    app,
    input_state: dict,
    config: dict,
    placeholder,
    node_filter=None,
    max_attempts: int = 2,
    cursor: str = "▌",
    retry_backoff_seconds: float = 1.0,
):
    """
    Streams a compiled LangGraph app's output into a Streamlit placeholder.
    node_filter: a set of node names whose tokens should be shown (e.g.
    {"mentor"}). Pass None to stream tokens from every node — use this
    for single-node graphs; use a filter for multi-node graphs like
    What If's genesis/shock/ripple router, where only the active
    simulator node's tokens should render.
    Returns (full_response_text, error_message). Exactly one is
    meaningful: on success, full_response_text is set and
    error_message is None; on failure, full_response_text is None and
    error_message explains why (already dev_mode-gated).
    """
    last_error_message = None
    for attempt in range(1, max_attempts + 1):
        full_response = ""
        try:
            for msg_chunk, metadata in app.stream(input_state, config, stream_mode="messages"):
                node_name = metadata.get("langgraph_node") if metadata else None
                if node_filter is None or node_name in node_filter:
                    full_response += extract_text(getattr(msg_chunk, "content", ""))
                    placeholder.markdown(full_response + cursor)
            placeholder.markdown(full_response)
            return full_response, None
        except Exception as e:
            transient, message = classify_error(e)
            last_error_message = message
            if transient and attempt < max_attempts:
                time.sleep(retry_backoff_seconds * attempt)
                continue
            else:
                return None, last_error_message
    return None, last_error_message