import streamlit as st
from data.question import ALL_QUESTIONS

# ==============================================================================
# 1. PARANOIA ENGINE: ACCESS CONTROL & STATE VALIDATION
# ==============================================================================
# Prevent direct URL access if the user hasn't finished the test
if "flags" not in st.session_state or not st.session_state.flags.get("scan_completed"):
    st.error("🛑 SECURITY BREACH: Assessment incomplete or session expired.")
    st.markdown("You must complete the telemetry scan before accessing the Builder Profile.")
    if st.button("⬅️ Return to Assessment"):
        st.switch_page("Quiz.py") # Ajuste le nom si ton fichier principal s'appelle autrement
    st.stop()

if "answers" not in st.session_state or not st.session_state.answers:
    st.error("⚠️ DATA CORRUPTION: No answers found in memory. Rebooting required.")
    st.stop()

# ==============================================================================
# PHASE 2: NEURAL DATA AGGREGATION
# ==============================================================================
st.markdown("<p style='color: #8B5CF6; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: -10px;'>Step 02 / Decryption</p>", unsafe_allow_html=True)
pseudo = st.session_state.user_profile.get("pseudo", "Unknown Builder")
st.title(f"🧬 Profile Decrypted: {pseudo}")
st.write("Cross-referencing your choices with the global hackathon database...")

# Initialize zeroed-out vectors
core_vectors = {
    "information_bandwidth": 0.0,
    "execution_rigor": 0.0,
    "chaos_tolerance": 0.0,
    "cognitive_endurance": 0.0
}

# Safely compute scores
rendered_advices = []
for q in ALL_QUESTIONS:
    qid = q["id"]
    # Safely get the user's answer for this specific question
    user_choice_key = st.session_state.answers.get(qid)
    
    if user_choice_key and user_choice_key in q["options"]:
        option_data = q["options"][user_choice_key]
        
        # Aggregate vectors safely using .get() to prevent KeyError
        for vec_key in core_vectors.keys():
            core_vectors[vec_key] += option_data.get("vectors", {}).get(vec_key, 0.0)
            
        # Store for the UI rendering
        rendered_advices.append({
            "qid": qid,
            "label": option_data.get("label", "Unknown Pattern"),
            "advice": option_data.get("advice", "Keep coding.")
        })

# ==============================================================================
# PHASE 3: METRICS DASHBOARD
# ==============================================================================
st.subheader("📊 Cognitive Loadout Matrix")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Information Bandwidth", f"{int(core_vectors['information_bandwidth'])} pts")
col2.metric("Execution Rigor", f"{int(core_vectors['execution_rigor'])} pts")
col3.metric("Chaos Tolerance", f"{int(core_vectors['chaos_tolerance'])} pts")
col4.metric("Cognitive Endurance", f"{int(core_vectors['cognitive_endurance'])} pts")

st.divider()

# ==============================================================================
# PHASE 4: TACTICAL DEPLOYMENT (ADVICES)
# ==============================================================================
st.subheader("💡 Tactical Briefing")
st.markdown("Based on your neural patterns, here is your custom survival guide for your next build/hackathon:")

for item in rendered_advices:
    with st.expander(f"Pattern Detected: {item['label']} (Q-{item['qid'].upper()})"):
        st.info(f"**Directive:** {item['advice']}")

st.write("")
st.write("")
if st.session_state.flags.get("chatbot_unlocked"):
    st.success("🔓 NEW FEATURE UNLOCKED: AI Mentor Access Granted.")
    if st.button("Initiate Chatbot Protocol 🤖", type="primary", use_container_width=True):
        st.switch_page("pages/Chatbot.py")