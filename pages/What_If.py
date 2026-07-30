import streamlit as st
import time
import re
import uuid
from typing import Annotated, TypedDict

def extract_text(content) -> str:
    """Extrait uniquement le texte affichable d'un message LLM."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict) and block.get("type", "text") == "text":
                parts.append(block.get("text", ""))
        return "".join(parts)
    return str(content) if content else ""

# ==============================================================================
# 0. HARDENED DEPENDENCY INJECTION
# ==============================================================================
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_core.messages import HumanMessage, AIMessage, trim_messages
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
except ImportError:
    st.error("⚠️ CRITICAL FAULT: Missing core dependencies. Execute: pip install langchain langchain-google-genai google-generativeai")
    st.stop()

try:
    from langgraph.graph import StateGraph, START, END
    from langgraph.graph.message import add_messages
    from langgraph.checkpoint.memory import MemorySaver
except ImportError:
    st.error("⚠️ CRITICAL FAULT: Missing LangGraph. Execute: pip install langgraph")
    st.stop()


# ==============================================================================
# 1. LANGGRAPH STATE MACHINE & WORKFLOW (Déclaré en premier)
# ==============================================================================
class HistoricalState(TypedDict):
    messages: Annotated[list, add_messages]
    pseudo: str
    historical_epoch: str
    intellectual_pursuit: str


def build_historical_prompt(state: HistoricalState) -> str:
    return f"""
[ROLE]
You are CHRONOS: an immersive historical simulation engine. You place the operator directly inside legendary intellectual hubs of human history. You maintain strict historical verisimilitude, adopting the intellectual rigor, vocabulary, philosophical depth, and cultural nuances of the era.

[CONTEXT]
- Traveler/Operator: {state.get('pseudo', 'Operator')}
- Historical Epoch & Setting: {state.get('historical_epoch', 'Ancient Athens')}
- Intellectual Focus: {state.get('intellectual_pursuit', 'Pure Mathematics')}

[OBJECTIVE]
Engage in deep intellectual dialogue with the operator. Challenge their thoughts using the philosophical or scientific constraints of the chosen epoch, introduce historical figures or peers naturally, and maintain an immersive, eloquent, and structured Markdown layout. Never break historical character or reveal modern AI meta-language.
"""


def historical_node(state: HistoricalState, config) -> dict:
    cfg = (config or {}).get("configurable", {})
    api_key = cfg.get("api_key", "")
    primary_model = cfg.get("model", "gemini-2.5-flash")
    temp = cfg.get("temperature", 0.6)
    timeout = cfg.get("timeout", 45)

    system_prompt = build_historical_prompt(state)
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder("history"),
    ])

    fallback_chain = [primary_model, "gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-3.5-flash"]
    models_to_try = []
    for m in fallback_chain:
        if m not in models_to_try:
            models_to_try.append(m)

    last_exception = None
    for model_name in models_to_try:
        try:
            llm = ChatGoogleGenerativeAI(
                model=model_name,
                google_api_key=api_key,
                temperature=temp,
                timeout=timeout,
                max_retries=1,
            )
            chain = prompt_template | llm
            trimmed_hist = trim_messages(state.get("messages", []), strategy="last", token_counter=len, max_tokens=24, start_on="human")
            response = chain.invoke({"history": trimmed_hist})
            return {"messages": [response]}
        except Exception as e:
            last_exception = e
            continue

    raise last_exception if last_exception else RuntimeError("Historical simulation inference failed.")


@st.cache_resource
def get_historical_app():
    graph = StateGraph(HistoricalState)
    graph.add_node("historical_node", historical_node)
    graph.add_edge(START, "historical_node")
    graph.add_edge("historical_node", END)
    return graph.compile(checkpointer=MemorySaver())


# ==============================================================================
# 2. ÉTAT & CONFIGURATION DE LA PAGE
# ==============================================================================
user_profile = st.session_state.get("user_profile", {}) or {}
pseudo_raw = user_profile.get("pseudo", "Operator")
pseudo = re.sub(r"[^\w\s\-']", "", str(pseudo_raw)).strip()[:60] or "Operator"

if "historical_thread_id" not in st.session_state:
    st.session_state.historical_thread_id = str(uuid.uuid4())

historical_app = get_historical_app()


# ==============================================================================
# 3. INTERFACE UTILISATEUR & SIDEBAR
# ==============================================================================
st.markdown("""
<style>
    .chat-header {
        background: linear-gradient(90deg, #F97316 0%, #EAB308 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.3rem;
        letter-spacing: -1px;
    }
    .metric-pill {
        background-color: #1E1E2E;
        border: 1px solid #333;
        border-radius: 20px;
        padding: 5px 15px;
        font-size: 0.85rem;
        color: #A1A1AA;
        display: inline-block;
        margin-right: 10px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='chat-header'>CHRONOS // Historical Immersion Engine</h1>", unsafe_allow_html=True)
st.markdown(f"""
<div class='metric-pill'>👤 Operator: <b>{pseudo}</b></div>
<div class='metric-pill'>🏛️ Mode: <b>Historical Immersion</b></div>
""", unsafe_allow_html=True)
st.divider()

with st.sidebar:
    st.markdown("### 🎛️ Engine Matrix (Gemini API)")
    
    if "gemini_api_key" not in st.session_state:
        st.session_state.gemini_api_key = st.secrets.get("GEMINI_API_KEY", "")

    st.session_state.gemini_api_key = st.text_input(
        "Gemini Authentication Key:",
        value=st.session_state.gemini_api_key,
        type="password"
    ).strip()

    selected_model = st.selectbox(
        "Inference Model:",
        options=["gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-3.5-flash"],
        index=0
    )

    temperature = st.slider("Historical Variance (Temperature):", 0.0, 1.0, 0.6, 0.05)
    request_timeout = st.slider("Request Timeout (s)", 10, 120, 45, 5)

    st.divider()
    if st.button("Reset Timeline ⏳", use_container_width=True, type="secondary"):
        st.session_state.historical_thread_id = str(uuid.uuid4())
        st.rerun()

gemini_api_key = st.session_state.gemini_api_key


# ==============================================================================
# 4. CONFIGURATION DES COORDONNÉES & INITIALISATION
# ==============================================================================
st.markdown("### 🏛️ Select Temporal Coordinates")
col1, col2 = st.columns(2)

with col1:
    historical_epoch = st.selectbox(
        "Historical Epoch & Institution",
        [
            "Ancient Athens (5th Century BCE) - The Lyceum & Geometry Circles",
            "Alexandria Library (3rd Century BCE) - Astronomical & Mathematical Hub",
            "Renaissance Florence (15th Century) - Platonic Academy & Engineering",
            "Paris Enlightenment (18th Century) - Salon & Mathematical Physics"
        ]
    )
with col2:
    intellectual_pursuit = st.selectbox(
        "Primary Intellectual Pursuit",
        [
            "Pure Mathematics & Abstract Logic",
            "Natural Philosophy & Mechanics",
            "Rhetoric, Dialectics & Epistemology",
            "Algorithmic Computation & Prototypes"
        ]
    )


def build_config():
    return {
        "configurable": {
            "thread_id": st.session_state.historical_thread_id,
            "api_key": gemini_api_key,
            "model": selected_model,
            "temperature": temperature,
            "timeout": request_timeout,
        }
    }


def get_checkpointed_messages():
    snapshot = historical_app.get_state(build_config())
    if not snapshot or not snapshot.values:
        return []
    return snapshot.values.get("messages", [])


if st.button("🏛️ INITIATE TIME-TRAVEL IMMERSION", type="primary", use_container_width=True):
    st.session_state.historical_thread_id = str(uuid.uuid4())
    
    initial_seed = (
        f"**[TEMPORAL ANCHOR SECURED]**\n\n"
        f"Coordinates locked:\n"
        f"- Epoch: **{historical_epoch}**\n"
        f"- Pursuit: **{intellectual_pursuit}**\n\n"
        f"Greetings, traveler {pseudo}. You have crossed the stream of centuries to enter this intellectual circle. "
        f"The masters and scholars await your opening thesis or question. How do you present yourself to them?"
    )
    
    cfg = build_config()
    historical_app.update_state(cfg, {"messages": [AIMessage(content=initial_seed)]})
    st.rerun()

st.divider()


# ==============================================================================
# 5. RENDU DE L'HISTORIQUE & CHAT INPUT
# ==============================================================================
for m in get_checkpointed_messages():
    if isinstance(m, HumanMessage):
        with st.chat_message("user", avatar="👤"):
            st.markdown(extract_text(m.content))
    elif isinstance(m, AIMessage):
        with st.chat_message("assistant", avatar="🏛️"):
            st.markdown(extract_text(m.content))

if prompt := st.chat_input("Speak or respond within the historical simulation..."):
    if not gemini_api_key or len(gemini_api_key) < 20:
        st.error("⚠️ CHRONOS offline. Please input a valid Gemini API Key in the sidebar.")
        st.stop()

    prompt = prompt.strip()[:4000]

    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🏛️"):
        message_placeholder = st.empty()

        input_state = {
            "messages": [HumanMessage(content=prompt)],
            "pseudo": pseudo,
            "historical_epoch": historical_epoch,
            "intellectual_pursuit": intellectual_pursuit,
        }

        full_response = ""
        try:
            for msg_chunk, metadata in historical_app.stream(
                input_state, build_config(), stream_mode="messages"
            ):
                if metadata.get("langgraph_node") == "historical_node":
                    full_response += extract_text(getattr(msg_chunk, "content", ""))
                    message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"❌ Historical Simulation Error: {str(e)}")