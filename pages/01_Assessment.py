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
    st.markdown("<p style='color: #6366F1; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: -10px;'>Step 01 / Diagnostics</p>", unsafe_allow_html=True)
    st.title("Metacognitive Baseline Registration")
    st.markdown("""
    Before mapping your data-absorption thresholds, the engine requires calibration parameters. 
    Provide real, unembellished identifiers. Sophistry here invalidates the downstream analysis.
    """)
    st.write("")

    with st.form("onboarding_secure_form"):
        col_input1, col_input2 = st.columns(2)
        
        with col_input1:
            pseudo = st.text_input(
                "User Alias / Identification Label:", 
                max_chars=20, 
                placeholder="e.g., Architect_01"
            ).strip()
            
        with col_input2:
            gender = st.selectbox(
                "Gender:", 
                ["", "Male ", "Female ", "Alien"]
            )
            
        st.write("")
        submit_profile = st.form_submit_button("Lock Baseline & Begin Scan ⚡", use_container_width=True)
        
        if submit_profile:
            if pseudo and gender:
                st.session_state.user_profile["pseudo"] = pseudo
                st.session_state.user_profile["gender"] = gender
                st.session_state.user_profile["initialized"] = True
                st.rerun()
            else:
                st.error("Telemetry Rejection: Both profiles vectors must be declared to anchor the session state.")
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
    st.markdown("<p style='color: #10B981; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: -10px;'>Sequence Achieved</p>", unsafe_allow_html=True)
    st.title("Cognitive Ingestion Complete")
    st.success(f"Telemetry stream locked. Profile associated with Subject: {st.session_state.user_profile['pseudo']}.")
    
    st.markdown("""
    Your behavioral choices have been compiled into a localized vector matrix. 
    The raw data has successfully converged. You can now pass this token to the diagnostic interpreter.
    """)
    st.write("")
    
    if st.button("Decompress Architectural Blueprint 🧬", type="primary", use_container_width=True):
        st.switch_page("pages/Advices.py")
    st.stop()


# ==============================================================================
# PHASE 3: INDUSTRIAL GAMIFICATION & LOAD METRICS
# ==============================================================================
if total_q == 0:
    st.error("Fatal Exception: Context repository 'ALL_QUESTIONS' is structurally empty.")
    st.stop()

# Compute live psychometric metrics
progress_percent = current_index / total_q

# REALISTIC METRICS (The Neural Stress Index formula scales with progress and answers)
# Starts at 14% baseline, rises naturally as cognitive accumulation increases
simulated_stress_index = int(14 + (progress_percent * 72) + (len(st.session_state.answers) % 3))

# Profound, non-robotic commentary reflecting real cognitive monitoring
if progress_percent == 0:
    telemetry_status = "Establishing clean cognitive baseline... Neutral load."
elif progress_percent < 0.35:
    telemetry_status = "Mapping standard logical sorting. Observing early biases."
elif progress_percent < 0.70:
    telemetry_status = "Complexity scale increased. Forcing behavioral trade-offs..."
else:
    telemetry_status = "Sustained focus threshold reached. Compiling late-stage exhaustion markers."

# The Real-time Telemetry Dashboard (Visually stunning for the 2-minute demo video)
metric_col1, metric_col2, metric_col3 = st.columns(3)
with metric_col1:
    st.metric(label="EVALUATED NODES", value=f"{current_index} / {total_q}", delta=None if current_index == 0 else "+1 Node")
with metric_col2:
    st.metric(label="NEURAL ACCUMULATION INDEX", value=f"{simulated_stress_index}%", delta="Elevating" if progress_percent > 0 else None)
with metric_col3:
    st.metric(label="METRIC DIVERGENCE", value="STABLE" if simulated_stress_index < 60 else "CONVERGING")

st.progress(progress_percent, text=telemetry_status)
st.divider()


# ==============================================================================
# PHASE 4: RECURSIVE QUESTION INGESTION ENGINE
# ==============================================================================
q_data = ALL_QUESTIONS[current_index]

# Modular layout to minimize visual fatigue
st.caption(f"SUBSYSTEM CORE LAYER: {q_data.get('section', 'UNASSIGNED').upper()}")
st.markdown(f"### {q_data.get('question', 'Telemetry query string corrupted.')}")
st.write("")

# Dynamic key architecture prevents cached selection retention across page reruns
with st.form(key=f"dynamic_cognitive_node_form_{current_index}"):
    choice = st.radio(
        "Isolate your authentic operational fallback option:",
        options=list(q_data["options"].keys()),
        format_func=lambda key_code: q_data["options"][key_code]["text"],
        index=None,
        key=f"isolated_radio_widget_node_{current_index}"
    )
    
    st.write("")
    advance_button = st.form_submit_button("Commit Choice to Memory Array ⚡", use_container_width=True)
    
    if advance_button:
        if choice is None:
            st.error("Decision required: Action cannot be bypassed without corrupting metrics consistency.")
        else:
            # Atomic state updates
            st.session_state.answers[q_data["id"]] = choice
            st.session_state.current_q += 1
            st.rerun()