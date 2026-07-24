import streamlit as st
import re
from data.question import ALL_QUESTIONS

# ==============================================================================
# PHASE 1: SESSION STATE INITIALIZATION
# ==============================================================================
if "current_q_idx" not in st.session_state:
    st.session_state.current_q_idx = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "flags" not in st.session_state:
    st.session_state.flags = {}

if "user_profile" not in st.session_state:
    st.session_state.user_profile = {"pseudo": "Builder"}

if not isinstance(ALL_QUESTIONS, list) or len(ALL_QUESTIONS) == 0:
    st.error("⚠️ CRITICAL: Question database is empty or missing. Cannot run the assessment.")
    st.stop()

TOTAL_QUESTIONS = len(ALL_QUESTIONS)
# Defensive clamp: if session state ever ends up out of range (e.g. the
# question bank shrank between two runs), don't crash — just show the report.
if st.session_state.current_q_idx > TOTAL_QUESTIONS:
    st.session_state.current_q_idx = TOTAL_QUESTIONS


# ==============================================================================
# PHASE 2: QUESTIONNAIRE LOOP
# ==============================================================================
if st.session_state.current_q_idx < TOTAL_QUESTIONS:
    idx = st.session_state.current_q_idx
    q = ALL_QUESTIONS[idx]

    st.progress(idx / TOTAL_QUESTIONS)
    st.caption(f"Question {idx + 1} of {TOTAL_QUESTIONS}")

    # FIX: the question bank stores the prompt under "question", not "text" —
    # the old code called q.get("text", ...) which never matched anything,
    # so every single question silently displayed "Untitled question".
    st.subheader(q.get("question", "Untitled question"))

    options = q.get("options", {})
    option_keys = list(options.keys()) if isinstance(options, dict) else list(options)

    # FIX: the radio previously showed raw option keys ("A", "B", "C", "D")
    # with no indication of what each one meant — the user was choosing
    # blind. format_func now renders the actual option text.
    def format_option(key):
        opt = options.get(key, {}) if isinstance(options, dict) else {}
        label_text = opt.get("text", str(key)) if isinstance(opt, dict) else str(key)
        return f"{key}) {label_text}"

    # FIX: index=None means nothing is pre-selected — the previous version
    # defaulted silently to the first option, so a user who clicked "Continue"
    # without reading anything still got an answer recorded as if they'd
    # chosen it on purpose. Now a real choice is required.
    selected_option = st.radio(
        "Pick the option that matches you best:",
        options=option_keys,
        format_func=format_option,
        index=None,
        key=f"radio_q_{idx}"
    )

    nav_col1, nav_col2 = st.columns([1, 1])

    with nav_col1:
        if idx > 0:
            if st.button("← Previous", use_container_width=True):
                st.session_state.current_q_idx -= 1
                st.rerun()

    with nav_col2:
        if st.button("Confirm & continue →", type="primary", use_container_width=True):
            if selected_option is None:
                st.warning("Pick an option before moving on.")
            else:
                st.session_state.answers[q.get("id", idx)] = selected_option
                st.session_state.current_q_idx += 1

                if st.session_state.current_q_idx >= TOTAL_QUESTIONS:
                    st.session_state.flags["scan_completed"] = True
                    st.session_state.flags["chatbot_unlocked"] = True

                st.rerun()

    # Block the dashboard below until the assessment is actually finished.
    st.stop()


# ==============================================================================
# PHASE 3: ACCESS CONTROL
# ==============================================================================
if not st.session_state.flags.get("scan_completed"):
    st.error("🛑 Assessment incomplete or session expired.")
    st.markdown("You need to complete the full scan before viewing your Builder Profile.")
    if st.button("⬅️ Return to start"):
        st.switch_page("lumen_app.py")
    st.stop()

if not st.session_state.answers:
    st.error("⚠️ No answers found in memory. Please retake the assessment.")
    if st.button("🔄 Retake the assessment"):
        st.session_state.current_q_idx = 0
        st.session_state.answers = {}
        st.rerun()
    st.stop()


# ==============================================================================
# PHASE 4: SCORE AGGREGATION
# ==============================================================================
st.markdown("<p style='color: #8B5CF6; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: -10px;'>Step 02 / Decryption</p>", unsafe_allow_html=True)

pseudo_raw = st.session_state.user_profile.get("pseudo", "Unknown Builder")
pseudo = re.sub(r"[^\w\s\-']", "", str(pseudo_raw)).strip()[:60] or "Unknown Builder"

st.title(f"🧬 Profile Decrypted: {pseudo}")
st.write("Turning your 24 answers into an actual cognitive profile...")

core_vectors = {
    "information_bandwidth": 0.0,
    "execution_rigor": 0.0,
    "chaos_tolerance": 0.0,
    "cognitive_endurance": 0.0
}

rendered_advices = []
for q in ALL_QUESTIONS:
    qid = q.get("id")
    user_choice_key = st.session_state.answers.get(qid)
    options = q.get("options", {}) or {}

    if user_choice_key and user_choice_key in options:
        option_data = options[user_choice_key]

        if isinstance(option_data, dict):
            for vec_key in core_vectors:
                try:
                    core_vectors[vec_key] += float(option_data.get("vectors", {}).get(vec_key, 0.0))
                except (TypeError, ValueError):
                    continue

            rendered_advices.append({
                "qid": qid,
                "label": option_data.get("label", "Unknown Pattern"),
                "advice": option_data.get("advice", "Keep building.")
            })

# Cached here so other pages (Advices, Chatbot, TheOldDays, What_If) could
# read this instead of recomputing the same sums from scratch each time —
# available for reuse, doesn't replace their own defensive recomputation.
st.session_state["core_vectors"] = core_vectors


# ==============================================================================
# PHASE 5: DASHBOARD
# ==============================================================================
st.subheader("📊 Cognitive Loadout Matrix")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Information Bandwidth", f"{int(core_vectors['information_bandwidth'])} pts")
col2.metric("Execution Rigor", f"{int(core_vectors['execution_rigor'])} pts")
col3.metric("Chaos Tolerance", f"{int(core_vectors['chaos_tolerance'])} pts")
col4.metric("Cognitive Endurance", f"{int(core_vectors['cognitive_endurance'])} pts")

st.divider()


# ==============================================================================
# PHASE 6: TACTICAL BRIEFING
# ==============================================================================
st.subheader("💡 Tactical Briefing")
st.markdown("Based on your answers, here's your custom survival guide for this build:")

for item in rendered_advices:
    with st.expander(f"Pattern detected: {item['label']} (Q-{str(item['qid']).upper()})"):
        st.info(f"**Directive:** {item['advice']}")

st.write("")
st.write("")

nav_col1, nav_col2 = st.columns(2)
with nav_col1:
    if st.session_state.flags.get("chatbot_unlocked"):
        st.success("🔓 AI Mentor unlocked.")
        if st.button("Talk to SYNAPSE 🤖", type="primary", use_container_width=True):
            st.switch_page("pages/Chatbot.py")
with nav_col2:
    if st.button("See the full Builder Blueprint 🧬", use_container_width=True):
        st.switch_page("pages/Advices.py")