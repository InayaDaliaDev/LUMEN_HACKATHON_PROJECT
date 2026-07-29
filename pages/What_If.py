import streamlit as st
import time
import re
import uuid
from typing import Annotated, TypedDict

# ==============================================================================
# 0. HARDENED DEPENDENCY INJECTION
# ==============================================================================
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_core.messages import HumanMessage, AIMessage, trim_messages, BaseMessage
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

# Optional: precise Google API exception types, if the package is present.
try:
    from google.api_core import exceptions as google_exceptions
    HAS_GOOGLE_EXCEPTIONS = True
except ImportError:
    HAS_GOOGLE_EXCEPTIONS = False


# ==============================================================================
# 1. ARCHITECTURAL SAFEGUARDS & STATE MANAGEMENT
# ==============================================================================
if 'answers' not in st.session_state or not st.session_state.get('answers'):
    st.error("🛑 ACCESS DENIED: Neural baseline not established. Complete the diagnostic scan first.")
    if st.button("🚀 Initiate Assessment", type="primary", use_container_width=True):
        st.switch_page("lumen_app.py")
    st.stop()

user_profile = st.session_state.get("user_profile", {}) or {}
pseudo_raw = user_profile.get("pseudo", "Operator")
pseudo = re.sub(r"[^\w\s\-']", "", str(pseudo_raw)).strip()[:60] or "Operator"

answers = st.session_state.get("answers", {}) or {}

try:
    from data.question import ALL_QUESTIONS
except ImportError:
    st.error("⚠️ Missing database connection to `data.question.ALL_QUESTIONS`")
    st.stop()

if not isinstance(ALL_QUESTIONS, list) or len(ALL_QUESTIONS) == 0:
    st.error("⚠️ Question database is empty or malformed. Cannot compute cognitive profile.")
    st.stop()


# ==============================================================================
# 2. COGNITIVE TELEMETRY EXTRACTION ENGINE (defensive parsing)
# ==============================================================================
all_labels = []
vector_totals = {
    "information_bandwidth": 0.0,
    "execution_rigor": 0.0,
    "chaos_tolerance": 0.0,
    "cognitive_endurance": 0.0
}

for q in ALL_QUESTIONS:
    try:
        q_id = q.get('id')
        if q_id in answers:
            choice_key = answers[q_id]
            opt = q.get("options", {}).get(choice_key, {}) or {}
            all_labels.append(opt.get("label", "Unmapped"))
            for v_key, v_val in (opt.get("vectors", {}) or {}).items():
                if v_key in vector_totals:
                    try:
                        vector_totals[v_key] += float(v_val)
                    except (TypeError, ValueError):
                        continue
    except AttributeError:
        continue

dominant_archetype = max(set(all_labels), key=all_labels.count) if all_labels else "Unclassified"
vector_labels = {
    "information_bandwidth": "Information Bandwidth",
    "execution_rigor": "Execution Rigor",
    "chaos_tolerance": "Chaos Tolerance",
    "cognitive_endurance": "Cognitive Endurance"
}
strongest_key = max(vector_totals, key=vector_totals.get)
weakest_key = min(vector_totals, key=vector_totals.get)


# ==============================================================================
# 3. ELITE UI/UX: THE CHRONOS CONTROL MATRIX
# ==============================================================================
st.markdown("""
<style>
    .chronos-title {
        background: linear-gradient(90deg, #3B82F6 0%, #10B981 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 2.8rem;
        letter-spacing: -1.5px;
    }
    .matrix-box {
        background-color: #0F172A;
        border: 1px solid #1E293B;
        padding: 24px;
        border-radius: 14px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        margin-bottom: 25px;
    }
    .telemetry-badge {
        background-color: #1E293B;
        color: #38BDF8;
        border: 1px solid #334155;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='chronos-title'>CHRONOS // Multiverse Trajectory Engine</h1>", unsafe_allow_html=True)
st.markdown(f"<span><span class='telemetry-badge'>OPERATOR: {pseudo.upper()}</span> <span class='telemetry-badge'>SIGNATURE: {dominant_archetype}</span></span>", unsafe_allow_html=True)
st.write("")
st.divider()

with st.container():
    st.markdown("<div class='matrix-box'>", unsafe_allow_html=True)
    st.markdown("### 🎛️ Configure Environmental Parameters")

    col1, col2, col3 = st.columns(3)
    with col1:
        sim_level = st.selectbox("Academic Tier", ["Middle School", "High School", "University / College"])
    with col2:
        sim_type = st.selectbox("Institutional Framework", ["Public System", "Private / Elite Academy"])
    with col3:
        sim_region = st.selectbox("Geopolitical Region", ["Africa", "Europe", "North America", "Asia"])

    st.markdown("</div>", unsafe_allow_html=True)


# ==============================================================================
# 4. SIDEBAR — HARDENED, SHARED KEY HANDLING
# ==============================================================================
def is_plausible_gemini_key(key: str) -> bool:
    if not key:
        return False
    key = key.strip()
    return len(key) >= 20 and " " not in key

if "gemini_api_key" not in st.session_state:
    default_key = ""
    try:
        if "GEMINI_API_KEY" in st.secrets:
            default_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        default_key = ""
    st.session_state.gemini_api_key = default_key

if "multiverse_thread_id" not in st.session_state:
    st.session_state.multiverse_thread_id = str(uuid.uuid4())

if "multiverse_awaiting_opening" not in st.session_state:
    st.session_state.multiverse_awaiting_opening = False

with st.sidebar:
    st.markdown("### ⚙️ Engine Matrix (Gemini API)")
    st.session_state.gemini_api_key = st.text_input(
        "Gemini API Key:",
        value=st.session_state.gemini_api_key,
        type="password",
        placeholder="Paste your Gemini API key",
        help="Shared across all Lumen pages for this session. Never logged or displayed."
    ).strip()

    selected_model = st.selectbox(
        "Inference Model:",
        options=[
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.5-flash",
            "gemini-flash-latest"
        ],
        index=0
    )
    request_timeout = st.slider("Request Timeout (s)", 10, 120, 45, 5)

    st.divider()
    if st.button("Purge Timeline Memory 🧹", use_container_width=True, type="secondary"):
        st.session_state.multiverse_thread_id = str(uuid.uuid4())
        st.session_state.multiverse_awaiting_opening = False
        st.rerun()

gemini_api_key = st.session_state.gemini_api_key


# ==============================================================================
# 5. LANGGRAPH STATE MACHINE — THE ACTUAL SIMULATION ENGINE
# ==============================================================================
class MultiverseState(TypedDict):
    messages: Annotated[list, add_messages]
    sim_level: str
    sim_type: str
    sim_region: str
    pseudo: str
    dominant_archetype: str
    strongest_label: str
    weakest_label: str
    turn_count: int
    phase: str


PHASE_INSTRUCTIONS = {
    "opening": (
        "PHASE — INSTITUTIONAL REALITY MATRIX: There is no prior conversation yet. "
        "Describe the unvarnished, systemic realities of a {sim_type} {sim_level} in "
        "{sim_region} (structural bureaucracy, competitive pressures, pedagogical "
        "methodologies, resource constraints, evaluation metrics). Avoid generic "
        "fluff; use precise institutional sociology. Then deliver the initial "
        "COGNITIVE COLLISION analysis: where the Operator's {strongest_label} yields "
        "an unfair asymmetric advantage in this specific environment, and where their "
        "{weakest_label} triggers a concrete, specific point of friction. End by "
        "placing the Operator inside one first, vivid, concrete decision point — not "
        "a summary, an actual moment they must react to."
    ),
    "challenge": (
        "PHASE — PROGNOSTIC TRAJECTORY: React in-character to what the Operator just "
        "decided or said, showing a specific consequence inside this institution "
        "(a teacher's reaction, a ranking shift, a peer dynamic, a bureaucratic "
        "hurdle). Then extend the forecast of their academic adaptation curve one "
        "step further — concrete and specific, never a vague generality — and leave "
        "them with the next real decision to make."
    ),
    "resolution": (
        "PHASE — TACTICAL REMEDIATION PROTOCOL: React in-character to the Operator's "
        "latest decision and its concrete fallout inside this institution. Then issue "
        "an uncompromising, highly structured, non-generic blueprint for structural "
        "survival and dominance in this specific environment going forward. Keep the "
        "simulation alive and interactive — do not wrap up with a tidy conclusion, "
        "let the Operator keep steering their own trajectory."
    ),
}

REPRESENTATIONAL_GUARDRAIL = (
    "[REPRESENTATIONAL INTEGRITY]\n"
    "{sim_region} contains enormously diverse educational systems across "
    "countries, income levels, languages, and urban/rural divides. Do not "
    "flatten this into a single stereotype. Pick and clearly name ONE "
    "concrete, plausible country or city-type setting within {sim_region} "
    "for this simulation, and frame it explicitly as one instance among "
    "many rather than as representative of the whole region."
)


def build_system_prompt(state: MultiverseState) -> str:
    guardrail = REPRESENTATIONAL_GUARDRAIL.format(sim_region=state["sim_region"])
    phase_text = PHASE_INSTRUCTIONS[state["phase"]].format(
        sim_type=state["sim_type"],
        sim_level=state["sim_level"],
        sim_region=state["sim_region"],
        strongest_label=state["strongest_label"],
        weakest_label=state["weakest_label"],
    )

    return f"""
[SYSTEM ARCHITECTURE: CHRONOS-v3.3 PREDICTIVE SIMULATION ENGINE]
ROLE: You are CHRONOS, an enterprise-grade Epistemic Simulation Engine and Sociocognitive Architect. You possess deep familiarity with global educational systems, institutional sociology, and cognitive profiling. Your mission is to simulate plausible friction points, systemic bottlenecks, and psychological trajectories of an elite operator when embedded in a specific educational framework.

[OPERATOR TELEMETRY]
- Designation: {state['pseudo']}
- Dominant Cognitive Archetype: {state['dominant_archetype']}
- Primary Vector Advantage: {state['strongest_label']}
- Critical Vulnerability Vector: {state['weakest_label']}

[ENVIRONMENTAL PARAMETERS]
- Academic Tier: {state['sim_level']}
- Institutional Framework: {state['sim_type']}
- Geopolitical Region: {state['sim_region']}

{guardrail}

[CURRENT NARRATIVE PHASE]
{phase_text}

[STYLING & CONSTRAINTS]
- Tone: Absolute authority, clinical precision, deeply analytical, intellectually elevating, and profoundly serious. No corporate pleasantries or generic AI fluff.
- Formatting: Advanced Markdown architecture. Use bold headers, explicit metric notation, and structured lists.
- Never break character, never mention that you are an AI or a simulation.
"""


def route_phase(state: MultiverseState) -> dict:
    turn_count = state.get("turn_count", 0)
    if turn_count == 0:
        phase = "opening"
    elif turn_count < 3:
        phase = "challenge"
    else:
        phase = "resolution"
    return {"phase": phase, "turn_count": turn_count + 1}


def phase_router(state: MultiverseState) -> str:
    return state["phase"]


def safe_token_counter(msgs) -> int:
    """Polymorphic constraint evaluator to prevent TypeError if a singleton is passed instead of an iterable."""
    if isinstance(msgs, list):
        return len(msgs)
    return 1


def trimmed_history(messages):
    if not messages:
        return []
    return trim_messages(
        messages,
        strategy="last",
        token_counter=safe_token_counter,
        max_tokens=24,
        start_on="human",
    )


def make_narrator_node(phase: str):
    def node(state: MultiverseState, config) -> dict:
        cfg = (config or {}).get("configurable", {})
        api_key = cfg.get("api_key", "")
        model = cfg.get("model", "gemini-2.5-flash")
        timeout = cfg.get("timeout", 45)

        phased_state = {**state, "phase": phase}
        system_prompt = build_system_prompt(phased_state)

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder("history"),
        ])

        llm = ChatGoogleGenerativeAI(
            model=model,
            google_api_key=api_key,
            temperature=0.6,
            timeout=timeout,
            max_retries=0,
        )

        chain = prompt_template | llm
        response = chain.invoke({"history": trimmed_history(state.get("messages", []))})
        return {"messages": [response]}

    return node


@st.cache_resource
def get_chronos_multiverse_app():
    graph = StateGraph(MultiverseState)
    graph.add_node("route_phase", route_phase)
    graph.add_node("opening_narrator", make_narrator_node("opening"))
    graph.add_node("challenge_narrator", make_narrator_node("challenge"))
    graph.add_node("resolution_narrator", make_narrator_node("resolution"))

    graph.add_edge(START, "route_phase")
    graph.add_conditional_edges(
        "route_phase",
        phase_router,
        {
            "opening": "opening_narrator",
            "challenge": "challenge_narrator",
            "resolution": "resolution_narrator",
        },
    )
    graph.add_edge("opening_narrator", END)
    graph.add_edge("challenge_narrator", END)
    graph.add_edge("resolution_narrator", END)

    return graph.compile(checkpointer=MemorySaver())


chronos_app = get_chronos_multiverse_app()
NARRATOR_NODES = {"opening_narrator", "challenge_narrator", "resolution_narrator"}


def stream_turn(input_state: dict, config: dict, placeholder, max_attempts: int = 2):
    last_error_message = None

    for attempt in range(1, max_attempts + 1):
        full_response = ""
        try:
            for msg_chunk, metadata in chronos_app.stream(
                input_state, config, stream_mode="messages"
            ):
                if metadata.get("langgraph_node") in NARRATOR_NODES:
                    full_response += getattr(msg_chunk, "content", "") or ""
                    placeholder.markdown(full_response + "▌")
            placeholder.markdown(full_response)
            return full_response, None

        except Exception as e:
            transient = False
            fatal_user_message = None

            if HAS_GOOGLE_EXCEPTIONS:
                if isinstance(e, google_exceptions.PermissionDenied):
                    fatal_user_message = "🔒 Access denied — the API key is invalid, revoked, or lacks permission for this model."
                elif isinstance(e, google_exceptions.Unauthenticated):
                    fatal_user_message = "🔒 Authentication failed — check that the API key is correct."
                elif isinstance(e, google_exceptions.InvalidArgument):
                    fatal_user_message = "⚠️ Invalid request — the selected model name may be wrong or unsupported for this key."
                elif isinstance(e, google_exceptions.ResourceExhausted):
                    transient = True
                    fatal_user_message = "⏳ Rate limit or quota reached."
                elif isinstance(e, (google_exceptions.DeadlineExceeded, google_exceptions.ServiceUnavailable)):
                    transient = True
                    fatal_user_message = "🌐 Temporary network or service issue."

            if fatal_user_message is None:
                transient = True
                fatal_user_message = f"❌ Unexpected engine fault ({type(e).__name__})."

            last_error_message = fatal_user_message

            if transient and attempt < max_attempts:
                time.sleep(1.5 * attempt)
                continue
            else:
                return None, last_error_message

    return None, last_error_message


def build_config():
    return {
        "configurable": {
            "thread_id": st.session_state.multiverse_thread_id,
            "api_key": gemini_api_key,
            "model": selected_model,
            "timeout": request_timeout,
        }
    }


def get_checkpointed_messages():
    snapshot = chronos_app.get_state(build_config())
    if not snapshot or not snapshot.values:
        return []
    return snapshot.values.get("messages", [])


# ==============================================================================
# 6. SIMULATION EXECUTION & DYNAMIC RENDERING
# ==============================================================================
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    if st.button("🌌 EXECUTE TIMELINE SIMULATION", use_container_width=True, type="primary"):
        if not is_plausible_gemini_key(gemini_api_key):
            st.error("⚠️ CRITICAL: A valid-looking Gemini API Key is required to initialize the Chronos engine.")
            st.stop()

        st.session_state.multiverse_thread_id = str(uuid.uuid4())
        st.session_state.multiverse_awaiting_opening = True
        st.rerun()

current_messages = get_checkpointed_messages()

for m in current_messages:
    if isinstance(m, HumanMessage):
        with st.chat_message("user", avatar="👤"):
            st.markdown(m.content)
    elif isinstance(m, AIMessage):
        with st.chat_message("assistant", avatar="🌐"):
            st.markdown(m.content)

if st.session_state.multiverse_awaiting_opening and not current_messages:
    with st.chat_message("assistant", avatar="🌐"):
        message_placeholder = st.empty()

        if not is_plausible_gemini_key(gemini_api_key):
            st.error("⚠️ CRITICAL: Gemini API Key missing or malformed.")
        else:
            input_state = {
                "messages": [],
                "sim_level": sim_level,
                "sim_type": sim_type,
                "sim_region": sim_region,
                "pseudo": pseudo,
                "dominant_archetype": dominant_archetype,
                "strongest_label": vector_labels[strongest_key],
                "weakest_label": vector_labels[weakest_key],
            }
            full_response, error_message = stream_turn(input_state, build_config(), message_placeholder)
            if error_message:
                st.error(error_message)
            else:
                st.session_state.multiverse_awaiting_opening = False

if prompt := st.chat_input("Interact with the simulation timeline..."):
    if not is_plausible_gemini_key(gemini_api_key):
        st.error("⚠️ CRITICAL: A valid-looking Gemini API Key is required.")
        st.stop()

    prompt = prompt.strip()[:4000]

    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🌐"):
        message_placeholder = st.empty()

        input_state = {
            "messages": [HumanMessage(content=prompt)],
            "sim_level": sim_level,
            "sim_type": sim_type,
            "sim_region": sim_region,
            "pseudo": pseudo,
            "dominant_archetype": dominant_archetype,
            "strongest_label": vector_labels[strongest_key],
            "weakest_label": vector_labels[weakest_key],
        }
        full_response, error_message = stream_turn(input_state, build_config(), message_placeholder)
        if error_message:
            st.error(error_message)