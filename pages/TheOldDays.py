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
# Never trust session_state content blindly when it feeds an LLM prompt.
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
# 3. ELITE UI/UX: THE HISTORICAL CHRONOS CONSOLE
# ==============================================================================
st.markdown("""
<style>
    .history-title {
        background: linear-gradient(90deg, #F59E0B 0%, #EF4444 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 2.8rem;
        letter-spacing: -1.5px;
    }
    .history-box {
        background-color: #18181B;
        border: 1px solid #27272A;
        padding: 24px;
        border-radius: 14px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4);
        margin-bottom: 25px;
    }
    .history-badge {
        background-color: #27272A;
        color: #FBBF24;
        border: 1px solid #3F3F46;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    .phase-badge {
        background-color: #1E293B;
        color: #38BDF8;
        border: 1px solid #334155;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='history-title'>CHRONOS // Historical Immersion Engine</h1>", unsafe_allow_html=True)
st.markdown(f"<span><span class='history-badge'>OPERATOR: {pseudo.upper()}</span> <span class='history-badge'>ARCHETYPE: {dominant_archetype}</span></span>", unsafe_allow_html=True)
st.write("")
st.divider()

with st.container():
    st.markdown("<div class='history-box'>", unsafe_allow_html=True)
    st.markdown("### 🏛️ Select Temporal Coordinates")

    col1, col2 = st.columns(2)
    with col1:
        selected_era = st.selectbox(
            "Historical Epoch & Institution",
            [
                "Ancient Athens (5th Century BCE) - The Lyceum & Geometry Circles",
                "Medieval University of Paris (13th Century) - Scholasticism & Theology",
                "Victorian England (19th Century) - Rigid Boarding School & Classical Grammar",
                "Parisian Sorbonne (1920s) - Early Female Pioneers in Advanced Mathematics",
                "Renaissance Florence (15th Century) - Humanism, Art & Mathematical Perspective"
            ]
        )
    with col2:
        immersion_focus = st.selectbox(
            "Primary Intellectual Pursuit",
            [
                "Pure Mathematics & Abstract Logic",
                "Rhetoric, Philosophy & Debate",
                "Scientific Experimentation & Natural Philosophy"
            ]
        )

    st.markdown("</div>", unsafe_allow_html=True)


# ==============================================================================
# 3bis. GROUNDING KNOWLEDGE BASE
# ==============================================================================
ERA_FACTS = {
    "Ancient Athens (5th Century BCE) - The Lyceum & Geometry Circles": [
        "Formal education was reserved for free male citizens; girls, slaves, and metics were excluded from it.",
        "Boys typically studied grammar, rhetoric, music, and gymnastics under a paidagogos and private tutors, not in a state school system.",
        "Wandering teachers called Sophists charged fees to teach rhetoric and argumentation, and were controversial for doing so.",
        "Mathematics was tied to philosophy: geometric proof was considered a path to truth, not a separate technical subject.",
    ],
    "Medieval University of Paris (13th Century) - Scholasticism & Theology": [
        "The University of Paris grew out of cathedral schools and was organized into faculties (Arts, Theology, Law, Medicine), with Arts as a required first stage.",
        "Teaching relied on lectio (reading and glossing authoritative texts) and disputatio (formal structured debate), not experimentation.",
        "Theology, dominated by figures in the Scholastic tradition, sat at the top of the faculty hierarchy above the Arts faculty.",
        "Only clerics and men could enroll; students lived under strict Church-supervised discipline.",
    ],
    "Victorian England (19th Century) - Rigid Boarding School & Classical Grammar": [
        "Elite boys' boarding schools emphasized Latin, Greek, and classical literature far more than mathematics or science.",
        "Corporal punishment, strict hierarchy (prefects, fagging systems), and rigid daily schedules were standard discipline tools.",
        "Formal secondary and higher education was largely closed to girls until reforms later in the century.",
        "Rote memorization and recitation were the dominant teaching methods, prized over independent inquiry.",
    ],
    "Parisian Sorbonne (1920s) - Early Female Pioneers in Advanced Mathematics": [
        "Women had only recently gained real access to French university degrees, and were still a small, closely watched minority in mathematics lecture halls.",
        "Female students frequently faced skepticism from professors and peers about their right to be there at all.",
        "The Sorbonne of the era mixed traditional lecture-based instruction with an emerging, more rigorous modern approach to analysis and algebra.",
        "A science degree was still widely seen as a stepping stone to teaching, rather than a research career, for most women who obtained one.",
    ],
    "Renaissance Florence (15th Century) - Humanism, Art & Mathematical Perspective": [
        "Humanist education emphasized classical Latin and Greek texts, rhetoric, and the studia humanitatis, alongside apprenticeship-based training in workshops (botteghe).",
        "Mathematics of the period was closely tied to practical uses: commercial arithmetic (abbaco schools), surveying, and the geometry of linear perspective in painting.",
        "Patronage from wealthy families (the Medici above all) shaped which scholars, artists, and ideas could flourish.",
        "Formal university-style education remained largely closed to women; their intellectual training, when it existed, happened privately.",
    ],
}


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

if "chronos_thread_id" not in st.session_state:
    st.session_state.chronos_thread_id = str(uuid.uuid4())

if "chronos_awaiting_opening" not in st.session_state:
    st.session_state.chronos_awaiting_opening = False

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
    if st.button("Reset Timeline ⏳", use_container_width=True, type="secondary"):
        st.session_state.chronos_thread_id = str(uuid.uuid4())
        st.session_state.chronos_awaiting_opening = False
        st.rerun()

gemini_api_key = st.session_state.gemini_api_key


# ==============================================================================
# 5. LANGGRAPH STATE MACHINE — THE ACTUAL NARRATIVE ENGINE
# ==============================================================================
class ChronosState(TypedDict):
    messages: Annotated[list, add_messages]
    era: str
    focus: str
    pseudo: str
    dominant_archetype: str
    strongest_label: str
    weakest_label: str
    turn_count: int
    phase: str


PHASE_INSTRUCTIONS = {
    "opening": (
        "PHASE — OPENING SCENE: There is no prior conversation yet. Transport the "
        "Operator directly into the classroom, courtyard, or workshop of this era. "
        "Describe atmosphere (sound, light, smell, clothing, architecture) and the "
        "social reality of the time in vivid, sensory prose. End by placing the "
        "Operator inside a concrete first moment of the day, not a generic welcome."
    ),
    "challenge": (
        "PHASE — INTELLECTUAL CHALLENGE: React in-character to what the Operator just "
        "said or did. Introduce (or continue) a specific scholar, tutor, or "
        "institutional hurdle of this era who poses a rigorous, era-appropriate "
        "challenge tied to the Operator's focus. Make the stakes concrete — a real "
        "problem, a real judge, a real consequence — not abstract encouragement."
    ),
    "resolution": (
        "PHASE — CONSEQUENCE & TRAJECTORY: React in-character to the Operator's latest "
        "choice, then show its ripple effect: how this era's institutions, peers, or "
        "authorities respond, and what door opens or closes as a result. Keep the "
        "simulation alive and interactive — do not wrap up with a tidy moral, let the "
        "Operator keep steering the timeline."
    ),
}


def build_system_prompt(state: ChronosState) -> str:
    facts = ERA_FACTS.get(state["era"], [])
    facts_block = "\n".join(f"- {f}" for f in facts) or "- (No specific grounding facts on file for this era — rely on well-established general history.)"

    return f"""
[SYSTEM ARCHITECTURE: CHRONOS HISTORICAL IMMERSION MODULE]
ROLE: You are an elite Historical Consciousness and Immersive Simulation Engine. You recreate past educational epochs with ruthless historical accuracy, profound literary prose, and vivid sensory detail. You do not romanticize the past; you depict its true intellectual brilliance, social barriers, institutional rigidities, and dogmas.

[OPERATOR TELEMETRY]
- Designation: {state['pseudo']}
- Cognitive Profile: {state['dominant_archetype']} (Strong in {state['strongest_label']}, vulnerable in {state['weakest_label']})
- Passion / Focus: {state['focus']}

[TEMPORAL TARGET]
- Epoch & Setting: {state['era']}

[VERIFIED HISTORICAL GROUNDING — treat as ground truth, never contradict these]
{facts_block}

[CURRENT NARRATIVE PHASE]
{PHASE_INSTRUCTIONS.get(state.get('phase', 'opening'), PHASE_INSTRUCTIONS['opening'])}

[STYLING & CONSTRAINTS]
- Tone: Immersive, atmospheric, deeply respectful of historical context, intellectually elevating, and uncompromisingly realistic.
- Language: Flawless, evocative English with subtle period-appropriate flavor without becoming unreadable.
- Never break character, never mention that you are an AI or a simulation.
"""


def route_phase(state: ChronosState) -> dict:
    turn_count = state.get("turn_count", 0)
    if turn_count == 0:
        phase = "opening"
    elif turn_count < 3:
        phase = "challenge"
    else:
        phase = "resolution"
    return {"phase": phase, "turn_count": turn_count + 1}


def phase_router(state: ChronosState) -> str:
    return state.get("phase", "opening")


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
        max_tokens=24,  # Interpreted as 24 nodes/messages based on the safe_token_counter mapping
        start_on="human",
    )


def make_narrator_node(phase: str):
    def node(state: ChronosState, config) -> dict:
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
            temperature=0.75,
            timeout=timeout,
            max_retries=0,
        )

        chain = prompt_template | llm
        response = chain.invoke({"history": trimmed_history(state.get("messages", []))})
        return {"messages": [response]}

    return node


@st.cache_resource
def get_chronos_app():
    graph = StateGraph(ChronosState)
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


chronos_app = get_chronos_app()
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
                fatal_user_message = f"❌ Temporal disruption ({type(e).__name__})."

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
            "thread_id": st.session_state.chronos_thread_id,
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
# 6. EXECUTION & DYNAMIC RENDERING
# ==============================================================================
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    if st.button("📜 INITIATE TIME-TRAVEL IMMERSION", use_container_width=True, type="primary"):
        if not is_plausible_gemini_key(gemini_api_key):
            st.error("⚠️ CRITICAL: A valid-looking Gemini API Key is required to activate the temporal portal.")
            st.stop()

        st.session_state.chronos_thread_id = str(uuid.uuid4())
        st.session_state.chronos_awaiting_opening = True
        st.rerun()

current_messages = get_checkpointed_messages()

for m in current_messages:
    if isinstance(m, HumanMessage):
        with st.chat_message("user", avatar="👤"):
            st.markdown(m.content)
    elif isinstance(m, AIMessage):
        with st.chat_message("assistant", avatar="⏳"):
            st.markdown(m.content)

if st.session_state.chronos_awaiting_opening and not current_messages:
    with st.chat_message("assistant", avatar="⏳"):
        message_placeholder = st.empty()

        if not is_plausible_gemini_key(gemini_api_key):
            st.error("⚠️ CRITICAL: Gemini API Key missing or malformed.")
        else:
            input_state = {
                "messages": [],
                "era": selected_era,
                "focus": immersion_focus,
                "pseudo": pseudo,
                "dominant_archetype": dominant_archetype,
                "strongest_label": vector_labels[strongest_key],
                "weakest_label": vector_labels[weakest_key],
            }
            full_response, error_message = stream_turn(input_state, build_config(), message_placeholder)
            if error_message:
                st.error(error_message)
            else:
                st.session_state.chronos_awaiting_opening = False

if prompt := st.chat_input("Speak or respond within the historical simulation..."):
    if not is_plausible_gemini_key(gemini_api_key):
        st.error("⚠️ CRITICAL: A valid-looking Gemini API Key is required.")
        st.stop()

    prompt = prompt.strip()[:4000]

    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="⏳"):
        message_placeholder = st.empty()

        input_state = {
            "messages": [HumanMessage(content=prompt)],
            "era": selected_era,
            "focus": immersion_focus,
            "pseudo": pseudo,
            "dominant_archetype": dominant_archetype,
            "strongest_label": vector_labels[strongest_key],
            "weakest_label": vector_labels[weakest_key],
        }
        full_response, error_message = stream_turn(input_state, build_config(), message_placeholder)
        if error_message:
            st.error(error_message)