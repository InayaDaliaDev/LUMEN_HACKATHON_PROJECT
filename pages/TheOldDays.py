import streamlit as st
import time
import re

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
        # FIX: the entry point is lumen_app.py, "Quiz.py" doesn't exist.
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
# 4. SIDEBAR — HARDENED, SHARED KEY HANDLING
# ==============================================================================
def is_plausible_gemini_key(key: str) -> bool:
    """Loose sanity check only — filters obviously-empty/malformed pastes."""
    if not key:
        return False
    key = key.strip()
    return len(key) >= 20 and " " not in key


# FIX: shared across all Lumen pages via session_state — paste it once.
if "gemini_api_key" not in st.session_state:
    default_key = ""
    try:
        if "GEMINI_API_KEY" in st.secrets:
            default_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        default_key = ""
    st.session_state.gemini_api_key = default_key

with st.sidebar:
    st.markdown("### ⚙️ Engine Matrix (Gemini API)")
    st.session_state.gemini_api_key = st.text_input(
        "Gemini API Key:",
        value=st.session_state.gemini_api_key,
        type="password",
        placeholder="Paste your Gemini API key",
        help="Shared across all Lumen pages for this session. Never logged or displayed."
    ).strip()
    selected_model = st.selectbox("Inference Model:", ["gemini-1.5-pro", "gemini-1.5-flash"], index=0)
    request_timeout = st.slider("Request Timeout (s)", 10, 120, 45, 5)

    st.divider()
    if st.button("Reset Timeline ⏳", use_container_width=True, type="secondary"):
        st.session_state.history_messages = []
        st.rerun()

gemini_api_key = st.session_state.gemini_api_key

if "history_messages" not in st.session_state:
    st.session_state.history_messages = []

MAX_HISTORY_MESSAGES = 40
if len(st.session_state.history_messages) > MAX_HISTORY_MESSAGES:
    st.session_state.history_messages = st.session_state.history_messages[-MAX_HISTORY_MESSAGES:]


# ==============================================================================
# 5. THE MASTERPIECE PROMPT: HISTORICAL IMMERSION ENGINE
# ==============================================================================
SYSTEM_PROMPT = f"""
[SYSTEM ARCHITECTURE: CHRONOS HISTORICAL IMMERSION MODULE]
ROLE: You are an elite Historical Consciousness and Immersive Simulation Engine. You recreate past educational epochs with ruthless historical accuracy, profound literary prose, and vivid sensory detail. You do not romanticize the past; you depict its true intellectual brilliance, social barriers, institutional rigidities, and dogmas.

[OPERATOR TELEMETRY]
- Designation: {pseudo}
- Cognitive Profile: {dominant_archetype} (Strong in {vector_labels[strongest_key]}, vulnerable in {vector_labels[weakest_key]})
- Passion / Focus: {immersion_focus}

[TEMPORAL TARGET]
- Epoch & Setting: {selected_era}

[EXECUTION PROTOCOL]
1. SENSORY & SOCIOLOGICAL SETTING: Transport the Operator directly into the classroom, courtyard, or lecture hall of this era. Describe the atmosphere (smell of parchment or candle wax, ambient sound, clothing, architectural weight).
2. THE HISTORICAL REALITY & BARRIERS: Acknowledge the strict realities of this era—including institutional gatekeeping, social expectations, and gender or class restrictions if applicable to the chosen epoch—and contrast them with the Operator's sharp, independent, modern intellectual instincts.
3. THE INTELLECTUAL CHALLENGE: Introduce a master scholar, tutor, or institutional hurdle of the time who poses a rigorous challenge related to {immersion_focus}.
4. INTERACTIVE IMMERSION: Remain fully in character as a historical narrator/mentor of that era, reacting dynamically to how the Operator answers or adapts.

[STYLING & CONSTRAINTS]
- Tone: Immersive, atmospheric, deeply respectful of historical context, intellectually elevating, and uncompromisingly realistic.
- Language: Flawless, evocative English with subtle period-appropriate flavor without becoming unreadable.
"""

# FIX / UPGRADE: instead of manually rebuilding a raw list of Message
# objects by hand on every single call (as before), we declare the
# conversation shape ONCE as a LangChain ChatPromptTemplate with a
# MessagesPlaceholder for the turn history. This is the idiomatic
# LangChain pattern — the template is reusable, composable with other
# chains, and makes the system/history/human structure explicit rather
# than assembled imperatively each time.
prompt_template = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    MessagesPlaceholder("history"),
])


# ==============================================================================
# 6. HARDENED LLM CALL WRAPPER (chain-based, retries, no secret leakage)
# ==============================================================================
def get_chain(model: str, api_key: str, timeout: int):
    llm = ChatGoogleGenerativeAI(
        model=model,
        google_api_key=api_key,
        temperature=0.7,
        convert_system_message_to_human=True,
        timeout=timeout,
        max_retries=0,  # we handle retries ourselves, explicitly, below
    )
    return prompt_template | llm


def history_to_messages(history):
    """Turns our simple session_state history into LangChain message objects,
    skipping hidden system-directive turns which never render to the user."""
    messages = []
    for m in history:
        role = m.get("role")
        content = m.get("content", "")
        if role == "user":
            messages.append(HumanMessage(content=content))
        elif role == "assistant":
            messages.append(AIMessage(content=content))
    return messages


def trimmed_history(history):
    """
    Keeps the most recent turns so a long roleplay session never silently
    blows past the model's context window. Trimming by message count (not
    a real tokenizer) is a conservative, dependency-free approximation —
    good enough here since each turn is short chat dialogue, not documents.
    """
    messages = history_to_messages(history)
    return trim_messages(
        messages,
        strategy="last",
        token_counter=len,
        max_tokens=24,
        start_on="human",
    )


def stream_with_resilience(chain, history, placeholder, max_attempts: int = 2):
    """
    Streams a response with a small number of retries on transient failures.
    Auth/config errors are never retried. No failure path ever echoes the
    raw exception text, which could contain request details.
    """
    last_error_message = None

    for attempt in range(1, max_attempts + 1):
        full_response = ""
        try:
            for chunk in chain.stream({"history": trimmed_history(history)}):
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
                fatal_user_message = f"❌ Temporal disruption ({type(e).__name__})."

            last_error_message = fatal_user_message

            if transient and attempt < max_attempts:
                time.sleep(1.5 * attempt)
                continue
            else:
                return None, last_error_message

    return None, last_error_message


# ==============================================================================
# 7. EXECUTION & DYNAMIC RENDERING
# ==============================================================================
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    if st.button("📜 INITIATE TIME-TRAVEL IMMERSION", use_container_width=True, type="primary"):
        if not is_plausible_gemini_key(gemini_api_key):
            st.error("⚠️ CRITICAL: A valid-looking Gemini API Key is required to activate the temporal portal.")
            st.stop()

        st.session_state.history_messages = []
        init_command = f"System directive: Open temporal portal to {selected_era}. Immerse operator {pseudo} focusing on {immersion_focus}."
        st.session_state.history_messages.append({"role": "user", "content": init_command, "hidden": True})

for msg in st.session_state.history_messages:
    if not msg.get("hidden", False):
        avatar = "⏳" if msg["role"] == "assistant" else "👤"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

# Automatic execution if the portal was just opened (hidden directive pending)
if (st.session_state.history_messages
        and st.session_state.history_messages[-1]["role"] == "user"
        and st.session_state.history_messages[-1].get("hidden", False)):
    with st.chat_message("assistant", avatar="⏳"):
        message_placeholder = st.empty()

        if not is_plausible_gemini_key(gemini_api_key):
            st.error("⚠️ CRITICAL: Gemini API Key missing or malformed.")
        else:
            try:
                chain = get_chain(selected_model, gemini_api_key, request_timeout)
            except Exception:
                st.error("❌ Could not initialize the Gemini client. Check the model name and key format.")
                chain = None

            if chain is not None:
                full_response, error_message = stream_with_resilience(
                    chain, st.session_state.history_messages, message_placeholder
                )
                if error_message:
                    st.error(error_message)
                else:
                    st.session_state.history_messages.append({"role": "assistant", "content": full_response})

# Real-time interactive follow-up
if prompt := st.chat_input("Speak or respond within the historical simulation..."):
    if not is_plausible_gemini_key(gemini_api_key):
        st.error("⚠️ CRITICAL: A valid-looking Gemini API Key is required.")
        st.stop()

    prompt = prompt.strip()[:4000]

    st.session_state.history_messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="⏳"):
        message_placeholder = st.empty()

        try:
            chain = get_chain(selected_model, gemini_api_key, request_timeout)
        except Exception:
            st.error("❌ Could not initialize the Gemini client. Check the model name and key format.")
            chain = None

        if chain is not None:
            full_response, error_message = stream_with_resilience(
                chain, st.session_state.history_messages, message_placeholder
            )
            if error_message:
                st.error(error_message)
            else:
                st.session_state.history_messages.append({"role": "assistant", "content": full_response})