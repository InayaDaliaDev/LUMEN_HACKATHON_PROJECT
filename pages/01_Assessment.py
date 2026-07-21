import streamlit as st
from data.question import ALL_QUESTIONS

# ==============================================================================
# 1. PARANOIA ENGINE: RUNTIME INTEGRITY CHECKS
# ==============================================================================
# CRITICAL SAFETIES: 
# - NO st.set_page_config() here to prevent application halting.
# - Strict fallback layers if the master schema in lumen_app.py is bypassed.

if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "user_profile" not in st.session_state:
    st.session_state.user_profile = {"pseudo": "", "gender": "", "initialized": False}
if "flags" not in st.session_state:
    st.session_state.flags = {"scan_completed": False, "chatbot_unlocked": False}

total_q = len(ALL_QUESTIONS)

# Prevent out-of-bounds index interpolation
if not isinstance(st.session_state.current_q, int):
    st.session_state.current_q = 0
st.session_state.current_q = max(0, min(st.session_state.current_q, total_q))


# ==============================================================================
# PHASE 1: CORE PROFILE INITIALIZATION (Onboarding)
# ==============================================================================
if not st.session_state.user_profile.get("initialized"):
    st.markdown("<p style='color: #6366F1; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: -10px;'>Step 01 / Onboarding</p>", unsafe_allow_html=True)
    st.title("⚡ Welcome to the Hackathon Assessment")
    st.markdown("""
    Tell us who you are before we test how your brain handles code, panic, and midnight coffee.  
    *Be honest—our algorithm spots fake answers faster than a broken build.*
    """)
    st.write("")

    with st.form("onboarding_secure_form"):
        col_input1, col_input2 = st.columns(2)
        
        with col_input1:
            pseudo = st.text_input(
                "Builder Handle / Alias:", 
                max_chars=20, 
                placeholder="e.g., CodeNinja_99"
            ).strip()
            
        with col_input2:
            gender = st.selectbox(
                "Player Classification:", 
                ["", "Male", "Female", "Alien / Cybernetic Entity"]
            )
            
        st.write("")
        submit_profile = st.form_submit_button("Lock Profile & Start Assessment 🚀", use_container_width=True)
        
        if submit_profile:
            if pseudo and gender:
                st.session_state.user_profile["pseudo"] = pseudo
                st.session_state.user_profile["gender"] = gender
                st.session_state.user_profile["initialized"] = True
                st.rerun()
            else:
                st.error("⚠️ Hey, no ghosting! Please fill out both fields to unlock the test.")
    st.stop()


# ==============================================================================
# PHASE 2: TELEMETRY EVALUATION ENDPOINT (Test Completion)
# ==============================================================================
current_index = st.session_state.current_q

if current_index >= total_q:
    # Update state flags immediately before rendering to allow cross-page access
    st.session_state.flags["scan_completed"] = True
    st.session_state.flags["chatbot_unlocked"] = True
    
    st.balloons()
    st.markdown("<p style='color: #10B981; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: -10px;'>Mission Accomplished</p>", unsafe_allow_html=True)
    st.title("🎉 Assessment Complete!")
    st.success(f"Nice work, **{st.session_state.user_profile['pseudo']}**! Your responses have been processed.")
    
    st.markdown("""
    We've cross-referenced your choices with our developer psychology matrix.  
    Your customized **Hackathon Survival Report** is ready for decryption.
    """)
    st.write("")
    
    if st.button("Unlock My Builder Profile 🧬", type="primary", use_container_width=True):
        st.switch_page("pages/Advices.py")
    st.stop()


# ==============================================================================
# PHASE 3: INDUSTRIAL GAMIFICATION & LOAD METRICS
# ==============================================================================
if total_q == 0:
    st.error("⚠️ Error: Question bank seems completely empty. Check your data files!")
    st.stop()

# Compute live psychometric metrics
progress_percent = current_index / total_q

# REALISTIC METRICS (The Neural Stress Index formula scales with progress and answers)
# Starts at 14% baseline, rises naturally as cognitive accumulation increases
simulated_stress_index = int(14 + (progress_percent * 72) + (len(st.session_state.answers) % 3))

# Dynamic status text tailored for a fun developer experience
if progress_percent == 0:
    telemetry_status = "Warming up the engine... take a deep breath."
elif progress_percent < 0.35:
    telemetry_status = "Analyzing baseline logic. Looking clean so far!"
elif progress_percent < 0.70:
    telemetry_status = "Pressure rising! Testing your crisis response mechanisms..."
else:
    telemetry_status = "Final stretch! Compiling midnight hackathon fatigue markers..."

# The Real-time Telemetry Dashboard (Visually stunning for the demo)
metric_col1, metric_col2, metric_col3 = st.columns(3)
with metric_col1:
    st.metric(label="QUESTIONS CLEARED", value=f"{current_index} / {total_q}", delta=None if current_index == 0 else "+1 Answered")
with metric_col2:
    st.metric(label="BRAIN LOAD INDEX", value=f"{simulated_stress_index}%", delta="Spiking" if progress_percent > 0 else None)
with metric_col3:
    st.metric(label="PATTERN CONVERGENCE", value="BUILDING" if simulated_stress_index < 60 else "LOCKED IN")

st.progress(progress_percent, text=telemetry_status)
st.divider()


# ==============================================================================
# PHASE 4: RECURSIVE QUESTION INGESTION ENGINE
# ==============================================================================
q_data = ALL_QUESTIONS[current_index]
# Clean layout designed to maintain focus and reduce cognitive load
section_title = q_data.get('section', 'General Overview').upper()
st.caption(f"Category: {section_title}")

current_question = q_data.get('question', 'This question is currently unavailable.')
st.markdown(f"### {current_question}")
st.write("")

# Dynamic form key ensures proper state management across page reruns
with st.form(key=f"response_form_{current_index}"):
    choice = st.radio(
        "Select the option that sounds most like you:",
        options=list(q_data["options"].keys()),
        format_func=lambda key_code: q_data["options"][key_code]["text"],
        index=None,
        key=f"radio_choice_{current_index}"
    )
    
    st.write("")
    advance_button = st.form_submit_button("Confirm & Next Question ➡️", use_container_width=True)
    
    if advance_button:
        if choice is None:
            st.error("⚠️ No option selected! Pick an answer before moving forward.")
        else:
            # Atomic state updates
            st.session_state.answers[q_data["id"]] = choice
            st.session_state.current_q += 1
            st.rerun()