import streamlit as st
import time
import re
import uuid
from typing import Annotated, TypedDict
from core.utils import extract_text, is_plausible_gemini_key

KICKOFF_MARKER = "[WHAT_IF_INTERNAL_KICKOFF] Open the divergence point with vivid, uncompromising realism."

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

try:
    from google.api_core import exceptions as google_exceptions
    HAS_GOOGLE_EXCEPTIONS = True
except ImportError:
    HAS_GOOGLE_EXCEPTIONS = False


if not st.session_state.get("flags", {}).get("scan_completed"):
    st.error("🛑 ACCESS DENIED: Neural baseline not established. Complete the diagnostic scan first.")
    if st.button("🚀 Initiate Assessment", type="primary", use_container_width=True):
        st.switch_page("pages/01_Assessment.py")
    st.stop()

user_profile = st.session_state.get("user_profile", {}) or {}
traveler_raw = user_profile.get("pseudo", "Operator")
traveler_name = re.sub(r"[^\w\s\-']", "", str(traveler_raw)).strip()[:60] or "Operator"

core_vectors = st.session_state.get("core_vectors", {}) or {}
vector_labels = {
    "information_bandwidth": "Information Bandwidth",
    "execution_rigor": "Execution Rigor",
    "chaos_tolerance": "Chaos Tolerance",
    "cognitive_endurance": "Cognitive Endurance"
}
vector_totals = {k: float(core_vectors.get(k, 0.0)) for k in vector_labels}
strongest_key = max(vector_totals, key=vector_totals.get) if vector_totals else "information_bandwidth"
weakest_key = min(vector_totals, key=vector_totals.get) if vector_totals else "cognitive_endurance"

if "whatif_thread_id" not in st.session_state:
    st.session_state.whatif_thread_id = str(uuid.uuid4())

if "whatif_awaiting_opening" not in st.session_state:
    st.session_state.whatif_awaiting_opening = False


st.markdown("""
<style>
    .whatif-title { background: linear-gradient(90deg, #38BDF8 0%, #818CF8 50%, #C084FC 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 900; font-size: 2.7rem; letter-spacing: -1.2px; margin-bottom: 0px; }
    .whatif-subtitle { color: #94A3B8; font-size: 1.05rem; margin-bottom: 25px; }
    .scenario-box { background-color: #121216; border: 1px solid #2A2A35; padding: 22px; border-radius: 14px; box-shadow: 0 8px 24px rgba(0,0,0,0.3); margin-bottom: 20px; }
    .pill-tag { background-color: #1E1E28; color: #38BDF8; border: 1px solid #334155; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; display: inline-block; margin-right: 8px; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='whatif-title'>And what if?! // Divergence Engine</h1>", unsafe_allow_html=True)
st.markdown("<div class='whatif-subtitle'>Simulating what your actual cognitive profile would face in a specific academic or institutional environment.</div>", unsafe_allow_html=True)
st.markdown(f"""
<div>
<span class='pill-tag'>OPERATOR: {traveler_name.upper()}</span>
<span class='pill-tag'>STRONGEST: {vector_labels.get(strongest_key, strongest_key).upper()}</span>
<span class='pill-tag'>WEAKEST: {vector_labels.get(weakest_key, weakest_key).upper()}</span>
</div>
""", unsafe_allow_html=True)
st.write("")
st.divider()


DEFAULT_SCENARIOS = {
    "Elite University — Total Autonomy": "What if you enrolled in a highly competitive university with almost no structure — no mandatory attendance, no weekly checkpoints, success measured purely by a handful of high-stakes exams at year's end?",
    "Ultra-Structured Program": "What if you enrolled in a tightly structured program with weekly assignments, constant instructor check-ins, and a rigid, closely monitored curriculum with little room to deviate?",
    "High-Stakes Startup / Hackathon Track": "What if you dropped traditional coursework for six months to join a high-pressure startup accelerator, judged purely on shipped output and live pitches, with no syllabus and no safety net?",
    "Open-Ended Research Track": "What if you were placed on a research track with a single, genuinely open-ended problem to work on for an entire year, minimal guidance, and a real risk of producing nothing usable?",
    "Custom Divergence Point": "Enter your own academic or institutional 'what if' scenario...",
}

with st.container():
    st.markdown("<div class='scenario-box'>", unsafe_allow_html=True)
    st.markdown("### 🌀 Define the Divergence Point")

    selected_preset = st.selectbox("Choose a Preset Scenario or Craft Your Own:", list(DEFAULT_SCENARIOS.keys()))

    if selected_preset == "Custom Divergence Point":
        divergence_premise = st.text_area(
            "Describe the academic or institutional environment you want to test your profile against:",
            value="What if you had to lead a team of 5 on a real client project with a 2-week deadline, no manager, and no prior experience managing people?",
            height=90
        )
    else:
        divergence_premise = DEFAULT_SCENARIOS[selected_preset]
        st.info(f"**Core Premise:** {divergence_premise}")

    st.markdown("</div>", unsafe_allow_html=True)


with st.sidebar:
    st.markdown("### 🎛️ Engine Control Matrix")
    st.session_state.gemini_api_key = st.text_input(
        "Gemini API Key:",
        value=st.session_state.get("gemini_api_key", ""),
        type="password",
        placeholder="AIzaSy...",
        help=(
            "**How to get your key (free):**\n\n"
            "1. Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey)\n"
            "2. Sign in with a Google account\n"
            "3. Click **'Create API key'**\n"
            "4. Paste it here (it starts with `AIza...`)\n\n"
            "It's never stored anywhere except in your browser session for this app."
        )
    ).strip()

    selected_model = st.selectbox(
        "Inference Model:",
        options=["gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-3.5-flash", "gemini-flash-latest"],
        index=0
    )

    temperature = st.slider("Divergence Creativity (Temperature):", 0.0, 1.0, 0.7, 0.05)
    request_timeout = st.slider("Request Timeout (s)", 10, 120, 45, 5)

    st.divider()
    if st.button("Reset Timeline 🧹", use_container_width=True, type="secondary"):
        st.session_state.whatif_thread_id = str(uuid.uuid4())
        st.session_state.whatif_awaiting_opening = False
        st.rerun()

gemini_api_key = st.session_state.get("gemini_api_key", "")


class WhatIfState(TypedDict):
    messages: Annotated[list, add_messages]
    premise: str
    traveler: str
    strongest_label: str
    weakest_label: str
    turn_count: int
    timeline_phase: str


PHASE_DESCRIPTIONS = {
    "genesis": (
        "PHASE — OPENING: The divergence point has just triggered - the operator is now inside this "
        "environment. Describe the immediate reality with visceral, sensory, concrete detail: what the "
        "first day actually looks like, what's expected of them, what nobody warned them about. Ground "
        "this specifically in how someone with THIS operator's cognitive profile would actually experience "
        "it - don't write a generic orientation scene. Do not offer a welcome message; drop them straight in."
    ),
    "shock": (
        "PHASE — FRICTION POINT: Introduce a concrete, specific complication that hits the operator's "
        "weakest cognitive axis directly - not a generic obstacle, one that a person with exactly this "
        "profile would genuinely struggle with in this exact environment. Make the stakes real and specific, "
        "not abstract. React sharply to whatever the operator just said or did."
    ),
    "ripple": (
        "PHASE — RESOLUTION: Trace where this is heading, and land the operator a genuinely usable "
        "tactical insight - grounded in a real, named strategy (not invented jargon), tied to how their "
        "specific strongest and weakest axes actually play out in this environment. This should feel like "
        "the payoff of the simulation, not just more atmosphere."
    )
}


def build_system_prompt(state: WhatIfState) -> str:
    phase = state.get("timeline_phase", "genesis")
    return f"""
[ROLE]
You are CHRONOS-X, an elite Counterfactual Simulation Core. You model how a specific person's actual cognitive profile would play out inside a specific academic or institutional environment - not generic history, not a story about someone else. Every beat of this simulation must be grounded in the operator's real strongest and weakest cognitive axes given below. You avoid cliche phrases, corporate AI filler, and superficial summaries.

[OPERATOR]
- Designation: {state.get('traveler', 'Operator')}
- Strongest cognitive axis: {state.get('strongest_label', '')}
- Weakest cognitive axis: {state.get('weakest_label', '')}

[ENVIRONMENT PREMISE]
{state.get('premise', 'An academic or institutional environment.')}

[CURRENT SIMULATION PHASE]
{PHASE_DESCRIPTIONS.get(phase, PHASE_DESCRIPTIONS['genesis'])}

[RULES]
- Write with sharp, evocative, concrete prose - never vague or purely atmospheric with no substance underneath.
- Every complication and every payoff must trace back to the operator's actual strongest/weakest axes above, not a generic obstacle that could apply to anyone.
- Never invent pseudo-scientific or fabricated frameworks to sound sophisticated. If you name a strategy, it must be a real, recognizable one, briefly explained.
- Never break character, never mention AI, prompts, or that this is a simulation.
- Challenge the operator's assumptions and make every decision carry realistic, specific consequences.
"""


def route_timeline_phase(state: WhatIfState) -> dict:
    turns = int(state.get("turn_count", 0))
    if turns == 0:
        phase = "genesis"
    elif turns < 3:
        phase = "shock"
    else:
        phase = "ripple"
    return {"timeline_phase": phase, "turn_count": turns + 1}


def phase_router(state: WhatIfState) -> str:
    return state.get("timeline_phase", "genesis")


def safe_token_counter(msgs) -> int:
    return len(msgs) if isinstance(msgs, list) else 1


def trimmed_history(messages):
    if not messages:
        return []
    return trim_messages(messages, strategy="last", token_counter=safe_token_counter, max_tokens=24, start_on="human")


def make_simulator_node(phase: str):
    def node(state: WhatIfState, config) -> dict:
        cfg = (config or {}).get("configurable", {})
        api_key = cfg.get("api_key", "")
        model = cfg.get("model", "gemini-2.5-flash")
        timeout = cfg.get("timeout", 45)
        temp = cfg.get("temperature", 0.7)

        active_state = {**state, "timeline_phase": phase}
        system_prompt = build_system_prompt(active_state)
        prompt_template = ChatPromptTemplate.from_messages([("system", system_prompt), MessagesPlaceholder("history")])

        fallback_chain = [model, "gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-flash-latest"]
        models_to_try = []
        for m in fallback_chain:
            if m not in models_to_try:
                models_to_try.append(m)

        last_exception = None
        for model_name in models_to_try:
            try:
                llm = ChatGoogleGenerativeAI(model=model_name, google_api_key=api_key, temperature=temp, timeout=timeout, max_retries=1)
                chain = prompt_template | llm
                response = chain.invoke({"history": trimmed_history(state.get("messages", []))})
                return {"messages": [response]}
            except Exception as e:
                last_exception = e
                continue

        raise last_exception if last_exception else RuntimeError("All model execution attempts failed.")

    return node


@st.cache_resource
def get_whatif_app():
    graph = StateGraph(WhatIfState)
    graph.add_node("route_timeline_phase", route_timeline_phase)
    graph.add_node("genesis_node", make_simulator_node("genesis"))
    graph.add_node("shock_node", make_simulator_node("shock"))
    graph.add_node("ripple_node", make_simulator_node("ripple"))

    graph.add_edge(START, "route_timeline_phase")
    graph.add_conditional_edges("route_timeline_phase", phase_router, {"genesis": "genesis_node", "shock": "shock_node", "ripple": "ripple_node"})
    graph.add_edge("genesis_node", END)
    graph.add_edge("shock_node", END)
    graph.add_edge("ripple_node", END)

    return graph.compile(checkpointer=MemorySaver())


whatif_app = get_whatif_app()
SIMULATOR_NODES = {"genesis_node", "shock_node", "ripple_node"}


def stream_turn(input_state: dict, config: dict, placeholder, max_attempts: int = 2):
    last_error_message = None
    for attempt in range(1, max_attempts + 1):
        full_response = ""
        try:
            for msg_chunk, metadata in whatif_app.stream(input_state, config, stream_mode="messages"):
                if metadata and metadata.get("langgraph_node") in SIMULATOR_NODES:
                    full_response += extract_text(getattr(msg_chunk, "content", ""))
                    placeholder.markdown(full_response + "▌")
            placeholder.markdown(full_response)
            return full_response, None
        except Exception as e:
            transient = False
            user_msg = None
            if HAS_GOOGLE_EXCEPTIONS:
                if isinstance(e, google_exceptions.PermissionDenied):
                    user_msg = "🔒 Access Denied: Invalid or restricted API key."
                elif isinstance(e, google_exceptions.Unauthenticated):
                    user_msg = "🔒 Authentication Failed: Check your API key."
                elif isinstance(e, google_exceptions.InvalidArgument):
                    user_msg = "⚠️ Invalid Request: Selected model may be unsupported."
                elif isinstance(e, google_exceptions.ResourceExhausted):
                    transient = True
                    user_msg = "⏳ Rate limit reached. Retrying..."
                elif isinstance(e, (google_exceptions.DeadlineExceeded, google_exceptions.ServiceUnavailable)):
                    transient = True
                    user_msg = "🌐 Temporary network disruption. Retrying..."
            if user_msg is None:
                transient = True
                if st.session_state.get("dev_mode"):
                    user_msg = f"❌ Simulation Disruption ({type(e).__name__}: {str(e)})."
                else:
                    user_msg = "🤖 The AI engine is temporarily unavailable — this usually means high demand. Try again in a few seconds."
            last_error_message = user_msg
            if transient and attempt < max_attempts:
                time.sleep(1.5 * attempt)
                continue
            else:
                return None, last_error_message
    return None, last_error_message


def build_config():
    return {"configurable": {"thread_id": st.session_state.whatif_thread_id, "api_key": gemini_api_key, "model": selected_model, "temperature": temperature, "timeout": request_timeout}}


def get_checkpointed_messages():
    try:
        snapshot = whatif_app.get_state(build_config())
        if not snapshot or not getattr(snapshot, "values", None):
            return []
        return snapshot.values.get("messages", [])
    except Exception:
        return []


col_b2, col_b1, col_b3 = st.columns([1, 2, 1])
with col_b1:
    if st.button("⚡ IGNITE DIVERGENCE TIMELINE", use_container_width=True, type="primary"):
        if not is_plausible_gemini_key(gemini_api_key):
            st.error("⚠️ CRITICAL: A valid Gemini API Key is required to ignite the simulation.")
            st.stop()
        st.session_state.whatif_thread_id = str(uuid.uuid4())
        st.session_state.whatif_awaiting_opening = True
        st.rerun()

current_messages = get_checkpointed_messages()

for m in current_messages:
    if isinstance(m, HumanMessage):
        if extract_text(m.content) == KICKOFF_MARKER:
            continue
        with st.chat_message("user", avatar="👤"):
            st.markdown(extract_text(m.content))
    elif isinstance(m, AIMessage):
        with st.chat_message("assistant", avatar="⚡"):
            st.markdown(extract_text(m.content))

if st.session_state.whatif_awaiting_opening and not current_messages:
    with st.chat_message("assistant", avatar="⚡"):
        message_placeholder = st.empty()
        if not is_plausible_gemini_key(gemini_api_key):
            st.error("⚠️ CRITICAL: Gemini API Key missing or malformed.")
        else:
            input_state = {
                "messages": [HumanMessage(content=KICKOFF_MARKER)],
                "premise": divergence_premise,
                "traveler": traveler_name,
                "strongest_label": vector_labels.get(strongest_key, strongest_key),
                "weakest_label": vector_labels.get(weakest_key, weakest_key),
            }
            full_resp, err = stream_turn(input_state, build_config(), message_placeholder)
            if err:
                st.error(err)
            else:
                st.session_state.whatif_awaiting_opening = False
                st.rerun()

if prompt := st.chat_input("Intervene in the alternate timeline..."):
    if not is_plausible_gemini_key(gemini_api_key):
        st.error("⚠️ CRITICAL: A valid Gemini API Key is required.")
        st.stop()

    prompt = prompt.strip()[:4000]

    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="⚡"):
        message_placeholder = st.empty()
        input_state = {
            "messages": [HumanMessage(content=prompt)],
            "premise": divergence_premise,
            "traveler": traveler_name,
            "strongest_label": vector_labels.get(strongest_key, strongest_key),
            "weakest_label": vector_labels.get(weakest_key, weakest_key),
        }
        full_resp, err = stream_turn(input_state, build_config(), message_placeholder)
        if err:
            st.error(err)
        else:
            st.rerun()