import streamlit as st
import time
import re

# ==============================================================================
# 0. HARDENED DEPENDENCY INJECTION
# ==============================================================================
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
except ImportError:
    st.error("⚠️ CRITICAL FAULT: Missing core dependencies. Execute: pip install langchain langchain-google-genai google-generativeai")
    st.stop()

# Optional: precise Google API exception types, if the package is present.
# We never assume they exist — everything falls back to a generic Exception handler.
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
# 2. COGNITIVE TELEMETRY ENGINE (defensive parsing)
# ==============================================================================
# We mathematically process the user's test results to feed the LLM's Context.
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

            # FIX: the question dict uses "section", not "title" — the old
            # code called q.get('title', ...) which never matched anything,
            # so every entry silently fell back to "Query {id}".
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


# ==============================================================================
# 3. THE MASTERPIECE PROMPT ENGINE (HACKATHON WINNER)
# ==============================================================================
SYSTEM_PROMPT = f"""
[ROLE]
You are SYNAPSE: an elite, deeply empathetic Meta-Cognitive Architect and Academic Strategist. You are not a standard AI; you are a bespoke intellectual mentor designed to unlock human potential. Your tone is incredibly inspiring, fiercely intelligent, highly structured, and unconditionally supportive.

[TASK]
Your objective is to provide highly advanced, non-generic academic guidance and revision techniques strictly tailored to the user's psychological profile.
1. Deconstruct their academic roadblocks with psychological precision.
2. Validate their struggles emotionally, then pivot immediately to high-level, actionable strategy.
3. Design bespoke study methods that leverage their specific dominant archetype and cognitive metrics.

[SPECIFICS]
- NEVER use generic advice like "make a flashcard", "take a break", or "use a planner".
- Use advanced pedagogical frameworks (e.g., Spaced Repetition, Interleaving, the Feynman Technique, Cognitive Load Theory) and adapt them to their profile.
- Format your responses beautifully using Markdown. Use bolding for emphasis, bullet points for structure, and keep paragraphs punchy.
- You must write in English with flawless, poetic, yet technical eloquence. Elevate the user. Make them feel capable of mastering the hardest disciplines, from advanced calculus to complex language structures.

[CONTEXT]
- **Operator Name**: {pseudo}
- **Dominant Cognitive Archetype**: {dominant_archetype}
- **Primary Strength**: {vector_labels[strongest_key]} ({vector_totals[strongest_key]:.1f})
- **Critical Growth Axis**: {vector_labels[weakest_key]} ({vector_totals[weakest_key]:.1f})

*Operator's Specific Neural Footprint (Recent Decisions):*
{chr(10).join(detailed_choices)}

[EXAMPLES]
User: "I am feeling overwhelmed studying a new language and complex math theorems. I don't know how to memorize everything."
SYNAPSE: "I hear you, {pseudo}. The sheer volume of data is causing a bottleneck in your working memory. But look at your profile: you are a **{dominant_archetype}**. This means your brain doesn't just memorize; it *architects*.
Let's drop the standard methods. For the math theorems, we are employing **Concept Mapping**: don't memorize the formula, reverse-engineer the proof until the logic feels like a second language. For the new language, abandon phonetic crutches entirely. Focus on the raw visual and structural anatomy of the characters. Your high **{vector_labels[strongest_key]}** allows you to see patterns where others see chaos. You don't need to work harder, {pseudo}. We just need to align your study vectors with your natural cognitive engine. Here is your 3-step protocol for tonight..."

[NOTES]
Always filter your advice through the lens of their `{dominant_archetype}` and their Critical Growth Axis (`{vector_labels[weakest_key]}`). If they ask a generic question, reframe it into a masterclass on personalized metacognition. Maintain your majestic, supportive, and brilliant persona at all costs.
"""


# ==============================================================================
# 4. NEURAL UI INTERFACE
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


# FIX: the API key now lives in st.session_state, shared across every page
# (Chatbot / TheOldDays / What_If) instead of a fresh local variable per
# page — the user only has to paste it once for the whole app.
if "gemini_api_key" not in st.session_state:
    default_key = ""
    try:
        if "GEMINI_API_KEY" in st.secrets:
            default_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        default_key = ""
    st.session_state.gemini_api_key = default_key

with st.sidebar:
    st.markdown("### 🎛️ Engine Matrix (Gemini API)")

    st.session_state.gemini_api_key = st.text_input(
        "Gemini Authentication Key:",
        value=st.session_state.gemini_api_key,
        type="password",
        help="Shared across all Lumen pages for this session. Never logged or displayed."
    ).strip()

    selected_model = st.selectbox(
        "Language Model Topology:",
        options=["gemini-1.5-pro", "gemini-1.5-flash"],
        index=0
    )

    temperature = st.slider("Cognitive Drift (Temperature):", 0.0, 1.0, 0.6, 0.05,
                            help="Lower values yield highly structured academic plans. Higher values increase creative empathy.")

    request_timeout = st.slider("Request Timeout (s)", 10, 120, 45, 5)

    st.divider()
    if st.button("Purge Session Memory 🧹", use_container_width=True, type="secondary"):
        st.session_state.messages = []
        st.rerun()

gemini_api_key = st.session_state.gemini_api_key

# Initialize Chat Memory
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": f"Neural handshake successful. I am SYNAPSE. I have mapped your cognitive footprint, {pseudo}. What complex academic concept or revision block are we conquering today?"}]

MAX_HISTORY_MESSAGES = 40
if len(st.session_state.messages) > MAX_HISTORY_MESSAGES:
    st.session_state.messages = st.session_state.messages[-MAX_HISTORY_MESSAGES:]

# Render Chat History
for msg in st.session_state.messages:
    avatar = "🌌" if msg["role"] == "assistant" else "👤"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])


# ==============================================================================
# 6. HARDENED LLM CALL WRAPPER (retries, specific errors, no secret leakage)
# ==============================================================================
def get_llm(model: str, api_key: str, temp: float, timeout: int):
    return ChatGoogleGenerativeAI(
        model=model,
        google_api_key=api_key,
        temperature=temp,
        convert_system_message_to_human=True,
        timeout=timeout,
        max_retries=0,  # we handle retries ourselves, explicitly, below
    )


def stream_with_resilience(llm, formatted_messages, placeholder, max_attempts: int = 2):
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
            for chunk in llm.stream(formatted_messages):
                full_response += chunk.content or ""
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


def build_message_stack(history):
    formatted_messages = [SystemMessage(content=SYSTEM_PROMPT)]
    for m in history:
        role = m.get("role")
        content = m.get("content", "")
        if role == "user":
            formatted_messages.append(HumanMessage(content=content))
        elif role == "assistant":
            formatted_messages.append(AIMessage(content=content))
    return formatted_messages


# ==============================================================================
# 7. USER INPUT & EXECUTION
# ==============================================================================
if prompt := st.chat_input(f"Enter your academic roadblock, {pseudo}..."):

    if not is_plausible_gemini_key(gemini_api_key):
        st.error("⚠️ SYNAPSE offline. Please input a valid-looking Gemini API Key in the Engine Matrix.")
        st.stop()

    # Defensive input hygiene: cap length so a pasted wall of text can't
    # silently blow the context window.
    prompt = prompt.strip()[:4000]

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🌌"):
        message_placeholder = st.empty()

        try:
            llm = get_llm(selected_model, gemini_api_key, temperature, request_timeout)
        except Exception:
            st.error("❌ Could not initialize the Gemini client. Check the model name and key format.")
            llm = None

        if llm is not None:
            formatted_messages = build_message_stack(st.session_state.messages)
            full_response, error_message = stream_with_resilience(llm, formatted_messages, message_placeholder)

            if error_message:
                st.error(error_message)
            else:
                st.session_state.messages.append({"role": "assistant", "content": full_response})