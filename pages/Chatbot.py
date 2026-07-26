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
# Defensive sanitation: never trust session_state content blindly, even if it
# originates from your own app — a corrupted or tampered session should not
# crash rendering or leak into the LLM prompt unsanitized.
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
# 2. COGNITIVE TELEMETRY ENGINE (defensive parsing) — unchanged
# ==============================================================================
all_labels = []
vector_totals = {
    "information_bandwidth": 0.0,
    "execution_rigor": 0.0,
    "chaos_tolerance": 0.0,
    "cognitive_endurance": 0.0
}
detailed_choices = []

for q in ALL_QUESTIONS:
    try:
        q_id = q.get('id')
        if q_id in answers:
            choice_key = answers[q_id]
            opt = q.get("options", {}).get(choice_key, {}) or {}

            label = opt.get("label", "Unmapped")
            all_labels.append(label)

            q_section = q.get('section', f"Query {q_id}")
            opt_text = opt.get('text', choice_key)
            detailed_choices.append(f"- **{q_section}**: {opt_text} (*Signaling {label}*)")

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
detailed_choices_block = "\n".join(detailed_choices) if detailed_choices else "- (No detailed signals on file.)"


# ==============================================================================
# 3. VERIFIED TECHNIQUE LIBRARY (grounding — the actual point of this page)
# ==============================================================================
# The old prompt just TOLD the model "never give generic advice, use real
# frameworks" and hoped it would comply and not invent anything. That's not
# grounding, that's a wish. Here the real, named, well-established techniques
# live in code, tagged by which cognitive axis they help compensate for
# ("addresses") and which they play to the strength of ("leverages"). A
# deterministic node below picks the most relevant ones for THIS Operator's
# actual profile before the LLM ever gets involved — the model still writes
# the explanation, but it can't quietly swap in a made-up "technique".
TECHNIQUE_LIBRARY = [
    {
        "name": "Spaced Repetition",
        "description": "Reviewing material at increasing intervals timed just before you'd naturally forget it (the spacing effect), instead of cramming everything into one session.",
        "addresses": ["cognitive_endurance", "execution_rigor"],
        "leverages": [],
    },
    {
        "name": "Interleaving",
        "description": "Mixing different topics or problem types within a single session instead of blocking one subject at a time, which forces the brain to actively discriminate which method applies.",
        "addresses": ["information_bandwidth"],
        "leverages": ["chaos_tolerance"],
    },
    {
        "name": "The Feynman Technique",
        "description": "Explaining a concept in the simplest possible language as if teaching a beginner, then using the exact points where you stumble to find and patch real gaps in understanding.",
        "addresses": ["information_bandwidth"],
        "leverages": ["execution_rigor"],
    },
    {
        "name": "Chunking (Cognitive Load Management)",
        "description": "Breaking dense material into small, tightly-scoped units small enough to fit in working memory, mastering each before combining them into the bigger structure.",
        "addresses": ["cognitive_endurance", "information_bandwidth"],
        "leverages": ["execution_rigor"],
    },
    {
        "name": "Timeboxing / Pomodoro-style sprints",
        "description": "Working in short, strictly bounded focus intervals with enforced breaks, using the external time limit as structure instead of relying on willpower alone.",
        "addresses": ["execution_rigor", "cognitive_endurance"],
        "leverages": [],
    },
    {
        "name": "Dual Coding",
        "description": "Pairing verbal explanations with diagrams, sketches, or spatial layouts of the same idea, since encoding information two different ways measurably improves recall.",
        "addresses": ["information_bandwidth"],
        "leverages": ["chaos_tolerance"],
    },
    {
        "name": "Active Recall / Retrieval Practice",
        "description": "Closing the book and forcing yourself to reconstruct the material from memory (self-testing) instead of re-reading it — proven to build far stronger long-term retention.",
        "addresses": ["cognitive_endurance"],
        "leverages": ["execution_rigor"],
    },
    {
        "name": "Elaborative Interrogation",
        "description": "Continuously asking yourself 'why is this true?' and 'how does this connect to what I already know?' while studying, turning passive reading into active reasoning.",
        "addresses": ["execution_rigor"],
        "leverages": ["information_bandwidth"],
    },
    {
        "name": "Method of Loci (Memory Palace)",
        "description": "Mentally placing pieces of information along a vivid, familiar spatial route (a house, a walk to school), then 'walking through' it to retrieve them in order.",
        "addresses": ["cognitive_endurance"],
        "leverages": ["chaos_tolerance", "information_bandwidth"],
    },
    {
        "name": "Desirable Difficulties",
        "description": "Deliberately making practice harder in the short term — testing before you feel ready, varying conditions, spacing things out — because the extra short-term struggle produces much stronger long-term learning.",
        "addresses": ["execution_rigor"],
        "leverages": ["chaos_tolerance"],
    },
]


def select_priority_techniques(weakest_key: str, strongest_key: str) -> list:
    """Deterministic, no LLM call: ranks the library by relevance to THIS
    Operator's actual profile. Growth-axis techniques come first (the more
    urgent need), then a strength-leveraging pick — never invented, always
    drawn from the verified library above."""
    addresses_weak = [t["name"] for t in TECHNIQUE_LIBRARY if weakest_key in t["addresses"]]
    leverages_strong = [t["name"] for t in TECHNIQUE_LIBRARY if strongest_key in t["leverages"]]

    picks = []
    for name in addresses_weak[:2] + leverages_strong[:1]:
        if name not in picks:
            picks.append(name)
    if not picks:
        picks = [TECHNIQUE_LIBRARY[0]["name"]]
    return picks


# ==============================================================================
# 4. NEURAL UI INTERFACE — unchanged
# ==============================================================================
st.markdown("""
<style>
    .chat-header {
        background: linear-gradient(90deg, #6366F1 0%, #A855F7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.5rem;
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

st.markdown("<h1 class='chat-header'>SYNAPSE // Neural Mentor</h1>", unsafe_allow_html=True)
st.markdown(f"""
<div class='metric-pill'>👤 Operator: <b>{pseudo}</b></div>
<div class='metric-pill'>🧬 Archetype: <b>{dominant_archetype}</b></div>
<div class='metric-pill'>⚡ Core Advantage: <b>{vector_labels[strongest_key]}</b></div>
""", unsafe_allow_html=True)
st.divider()


# ==============================================================================
# 5. SIDEBAR — HARDENED, SHARED KEY HANDLING
# ==============================================================================
def is_plausible_gemini_key(key: str) -> bool:
    """
    Loose sanity check only — NOT a validity check. Filters out empty
    strings, whitespace, and obviously-too-short pastes before we waste a
    network call and show the user a confusing traceback.
    """
    if not key:
        return False
    key = key.strip()
    return len(key) >= 20 and " " not in key


# Shared across all Lumen pages via session_state — paste it once for the
# whole app (Chatbot / TheOldDays / What_If all read the same value).
if "gemini_api_key" not in st.session_state:
    default_key = ""
    try:
        if "GEMINI_API_KEY" in st.secrets:
            default_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        default_key = ""
    st.session_state.gemini_api_key = default_key

if "synapse_thread_id" not in st.session_state:
    st.session_state.synapse_thread_id = str(uuid.uuid4())

with st.sidebar:
    st.markdown("### 🎛️ Engine Matrix (Gemini API)")

    st.session_state.gemini_api_key = st.text_input(
        "Gemini Authentication Key:",
        value=st.session_state.gemini_api_key,
        type="password",
        help="Shared across all Lumen pages for this session. Never logged or displayed."
    ).strip()

    # FIX: gemini-1.5-pro / gemini-1.5-flash are fully retired by Google (the
    # API now returns a 404 for both). gemini-2.5-flash / gemini-2.5-pro are
    # the current stable, generally-available models as of mid-2026.
    selected_model = st.selectbox(
        "Language Model Topology:",
        options=["gemini-2.5-flash", "gemini-2.5-pro"],
        index=0
    )

    temperature = st.slider("Cognitive Drift (Temperature):", 0.0, 1.0, 0.6, 0.05,
                            help="Lower values yield highly structured academic plans. Higher values increase creative empathy.")

    request_timeout = st.slider("Request Timeout (s)", 10, 120, 45, 5)

    st.divider()
    if st.button("Purge Session Memory 🧹", use_container_width=True, type="secondary"):
        # A fresh thread_id means LangGraph's checkpointer starts this
        # conversation from a completely blank state.
        st.session_state.synapse_thread_id = str(uuid.uuid4())
        st.rerun()

gemini_api_key = st.session_state.gemini_api_key


# ==============================================================================
# 6. LANGGRAPH STATE MACHINE — THE ACTUAL MENTOR ENGINE
# ==============================================================================
class MentorState(TypedDict):
    messages: Annotated[list, add_messages]
    pseudo: str
    dominant_archetype: str
    strongest_key: str
    weakest_key: str
    strongest_label: str
    weakest_label: str
    detailed_choices: str
    selected_techniques: list


def build_system_prompt(state: MentorState) -> str:
    library_block = "\n".join(
        f"- **{t['name']}**: {t['description']}" for t in TECHNIQUE_LIBRARY
    )
    priority = state.get("selected_techniques") or []
    priority_block = ", ".join(priority) if priority else "(none flagged — pick freely from the library)"

    return f"""
[ROLE]
You are SYNAPSE: an elite, deeply empathetic Meta-Cognitive Architect and Academic Strategist. You are not a standard AI; you are a bespoke intellectual mentor designed to unlock human potential. Your tone is incredibly inspiring, fiercely intelligent, highly structured, and unconditionally supportive.

[TASK]
Your objective is to provide highly advanced, non-generic academic guidance strictly tailored to the user's psychological profile.
1. Deconstruct their academic roadblocks with psychological precision.
2. Validate their struggles emotionally, then pivot immediately to high-level, actionable strategy.
3. Recommend and adapt techniques FROM THE VERIFIED LIBRARY below to their specific dominant archetype and cognitive metrics — never invent a technique that isn't in it.

[VERIFIED TECHNIQUE LIBRARY — the only techniques you may name and recommend]
{library_block}

[PRIORITY PICKS FOR THIS OPERATOR — computed from their actual profile, lead with these when relevant]
{priority_block}

[SPECIFICS]
- NEVER use generic advice like "make a flashcard", "take a break", or "use a planner" as a substitute for naming and explaining one of the techniques above.
- Format your responses beautifully using Markdown. Use bolding for emphasis, bullet points for structure, and keep paragraphs punchy.
- Write in English with flawless, poetic, yet technical eloquence. Elevate the user. Make them feel capable of mastering the hardest disciplines.

[CONTEXT]
- **Operator Name**: {state['pseudo']}
- **Dominant Cognitive Archetype**: {state['dominant_archetype']}
- **Primary Strength**: {state['strongest_label']}
- **Critical Growth Axis**: {state['weakest_label']}

*Operator's Specific Neural Footprint (Recent Decisions):*
{state['detailed_choices']}

[NOTES]
Always filter your advice through the lens of their `{state['dominant_archetype']}` and their Critical Growth Axis (`{state['weakest_label']}`). If they ask a generic question, reframe it into a masterclass on personalized metacognition using one or more of the library techniques above. Maintain your majestic, supportive, and brilliant persona at all costs. Never mention that you are an AI or that a "library" or "graph" exists — speak as SYNAPSE, not about your own architecture.
"""


def trimmed_history(messages):
    """Keeps only the most recent turns so a long mentoring session never
    silently blows past the model's context window."""
    if not messages:
        return []
    return trim_messages(
        messages,
        strategy="last",
        token_counter=len,
        max_tokens=24,
        start_on="human",
    )


def select_techniques_node(state: MentorState, config) -> dict:
    """Pure, deterministic pre-processing — no LLM call, no ambiguity, no
    cost. Decides WHICH real techniques are most relevant before the mentor
    node ever writes a word."""
    picks = select_priority_techniques(state.get("weakest_key", ""), state.get("strongest_key", ""))
    return {"selected_techniques": picks}


def mentor_node(state: MentorState, config) -> dict:
    cfg = (config or {}).get("configurable", {})
    api_key = cfg.get("api_key", "")
    model = cfg.get("model", "gemini-2.5-flash")
    temp = cfg.get("temperature", 0.6)
    timeout = cfg.get("timeout", 45)

    system_prompt = build_system_prompt(state)
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder("history"),
    ])

    llm = ChatGoogleGenerativeAI(
        model=model,
        google_api_key=api_key,
        temperature=temp,
        timeout=timeout,
        max_retries=0,  # retries are handled explicitly by stream_turn()
    )

    chain = prompt_template | llm
    response = chain.invoke({"history": trimmed_history(state.get("messages", []))})
    return {"messages": [response]}


@st.cache_resource
def get_synapse_app():
    """Compiled once per server process and reused across every rerun and
    every user session — no secrets or per-user profile data are baked in
    here (they travel through the state/config per-call instead), so
    sharing this compiled graph is safe. MemorySaver keeps each
    conversation isolated by thread_id."""
    graph = StateGraph(MentorState)
    graph.add_node("select_techniques", select_techniques_node)
    graph.add_node("mentor", mentor_node)

    graph.add_edge(START, "select_techniques")
    graph.add_edge("select_techniques", "mentor")
    graph.add_edge("mentor", END)

    return graph.compile(checkpointer=MemorySaver())


synapse_app = get_synapse_app()


def build_config():
    return {
        "configurable": {
            "thread_id": st.session_state.synapse_thread_id,
            "api_key": gemini_api_key,
            "model": selected_model,
            "temperature": temperature,
            "timeout": request_timeout,
        }
    }


def get_checkpointed_messages():
    snapshot = synapse_app.get_state(build_config())
    if not snapshot or not snapshot.values:
        return []
    return snapshot.values.get("messages", [])


def seed_greeting_if_new():
    """Matches the original UX: a static, non-LLM welcome message is
    present from the very first render of a fresh thread, and counts as
    part of the conversation history the model sees afterwards."""
    if get_checkpointed_messages():
        return
    greeting = (
        f"Neural handshake successful. I am SYNAPSE. I have mapped your cognitive "
        f"footprint, {pseudo}. What complex academic concept or revision block are "
        f"we conquering today?"
    )
    synapse_app.update_state(build_config(), {"messages": [AIMessage(content=greeting)]})


seed_greeting_if_new()


def stream_turn(input_state: dict, config: dict, placeholder, max_attempts: int = 2):
    """
    Streams a response with a small number of retries on transient failures.
    Auth/config errors are never retried. No failure path ever echoes the
    raw exception text, which could contain request details — only a
    classified, user-legible message.
    """
    last_error_message = None

    for attempt in range(1, max_attempts + 1):
        full_response = ""
        try:
            for msg_chunk, metadata in synapse_app.stream(
                input_state, config, stream_mode="messages"
            ):
                if metadata.get("langgraph_node") == "mentor":
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


# ==============================================================================
# 7. RENDER HISTORY
# ==============================================================================
for m in get_checkpointed_messages():
    if isinstance(m, HumanMessage):
        with st.chat_message("user", avatar="👤"):
            st.markdown(m.content)
    elif isinstance(m, AIMessage):
        with st.chat_message("assistant", avatar="🌌"):
            st.markdown(m.content)


# ==============================================================================
# 8. USER INPUT & EXECUTION
# ==============================================================================
if prompt := st.chat_input(f"Enter your academic roadblock, {pseudo}..."):

    if not is_plausible_gemini_key(gemini_api_key):
        st.error("⚠️ SYNAPSE offline. Please input a valid-looking Gemini API Key in the Engine Matrix.")
        st.stop()

    # Defensive input hygiene: cap length so a pasted wall of text can't
    # silently blow the context window.
    prompt = prompt.strip()[:4000]

    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🌌"):
        message_placeholder = st.empty()

        input_state = {
            "messages": [HumanMessage(content=prompt)],
            "pseudo": pseudo,
            "dominant_archetype": dominant_archetype,
            "strongest_key": strongest_key,
            "weakest_key": weakest_key,
            "strongest_label": vector_labels[strongest_key],
            "weakest_label": vector_labels[weakest_key],
            "detailed_choices": detailed_choices_block,
        }
        full_response, error_message = stream_turn(input_state, build_config(), message_placeholder)
        if error_message:
            st.error(error_message)