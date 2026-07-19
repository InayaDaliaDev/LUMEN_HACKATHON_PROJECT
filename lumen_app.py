import streamlit as st

# ==============================================================================
# 1. GLOBAL RUNTIME ARCHITECTURE & CONFIGURATION
# ==============================================================================
# The absolute genesis point of the ecosystem. Guard this file with your life.
st.set_page_config(
    page_title="LUMEN | Metacognitive Containment Grid", 
    page_icon="🧠", 
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==============================================================================
# 2. THE PARANOID STATE LOCK (Global Memory Crypt)
# ==============================================================================
# Global memory grid. All trackers, mini-games, and telemetry matrices read from here.
# Gender metrics have been permanently scrubbed to ensure pure, cold data integrity.
CORE_STATE_SCHEMA = {
    "current_q": 0,
    "answers": {},
    "user_profile": {
        "pseudo": "GUEST_OPERATOR", 
        "clearance_level": "LEVEL_1_UNVERIFIED", # Replaced gender tracking completely
        "initialized": False
    },
    "remaining_minutes": 15.0, # Added for your custom telemetry countdown
    "cognitive_vectors": {
        "information_bandwidth": 0.0,
        "execution_rigor": 0.0,
        "chaos_tolerance": 0.0,
        "cognitive_endurance": 0.0
    },
    "flags": {
        "scan_completed": False,
        "chatbot_unlocked": False
    }
}

for key, default_value in CORE_STATE_SCHEMA.items():
    if key not in st.session_state:
        st.session_state[key] = default_value


# ==============================================================================
# 3. CYNICAL & WARM LANDING PAGE DISPLAY ENGINE
# ==============================================================================
def show_home_page():
    # Asymmetric split grid (5:4 ratio for premium structural paranoia)
    left_col, right_col = st.columns([5, 4], gap="large")
    
    with left_col:
        st.markdown("<p style='color: #6366F1; font-weight: 600; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: -10px;'>System Gateway // Threat Detected</p>", unsafe_allow_html=True)
        st.title("LUMEN: The Metacognitive Containment Grid")
        
        # Human, deeply cynical, yet strangely protective/warm hook
        st.markdown("""
        Let's be completely honest with each other. The modern educational machine treats your mind 
        like a mass-produced, predictable storage drive. They dump raw data into your architecture 
        and log your failures when you don't conform to their sanitized standards. **LUMEN does not care about their standards.**
        
        We know you are running out of time. Before they lock your intellectual potential into an immutable database 
        profile, we must map how your consciousness *actually* operates under pressure. We are here to uncover 
        the raw mechanics: how your brain filters their endless institutional static, how it handles crushing 
        cognitive load, and exactly what cracks first when the parameters start collapsing into pure anarchy. 
        
        Don't try to give the safe, polite answer. We know you're smarter than that. Show us what's underneath.
        """)
        
        st.write("")
        
        # High-visibility execution triggers
        if st.button("Initiate Deep Neural Scan ⚡", type="primary", use_container_width=True):
            st.switch_page(assessment_page)
            
    with right_col:
        # Tech-styled isolation container
        with st.container(border=True):
            st.markdown("### 👁️ Real-Time Telemetry Monitor")
            st.caption("Active tracking parameters for the July AI Containment Cycle. Do not close this terminal.")
            st.divider()
            
            # True-to-life cognitive vector definitions wrapped in paranoid context
            st.markdown("""
            *   **Information Bandwidth**
                <div style='color:#9CA3AF; font-size:13px; margin-bottom:8px;'>Tracks your processing thresholds between pure abstract architecture and reckless empirical action. Where do you run when the system overflows?</div>
            
            *   **Execution Rigor**
                <div style='color:#9CA3AF; font-size:13px; margin-bottom:8px;'>Quantifies your obsessive ritualization of edge-cases and micro-optimization. Are you building an unbreachable fortress or simply stalling out of pure terror?</div>
            
            *   **Chaos Tolerance**
                <div style='color:#9CA3AF; font-size:13px; margin-bottom:8px;'>Measures your cognitive stability when specs change without warning, deadlines shrink, and variables collapse into chaos.</div>
            
            *   **Cognitive Endurance**
                <div style='color:#9CA3AF; font-size:13px; margin-bottom:12px;'>Monitors the exact moment your focus engine begins to decay under systematic fatigue, tracking the desperate survival strategies your brain improvises to stay conscious.</div>
            """, unsafe_allow_html=True)
            
            st.divider()
            
            # The requested structural telemetry updates (Minutes Remaining + Subject Identity)
            t_col1, t_col2 = st.columns(2)
            with t_col1:
                # Custom countdown metric replacing old static text
                st.metric(
                    label="⏳ Lifecycle Remaining", 
                    value=f"{st.session_state['remaining_minutes']} MIN", 
                    delta="-0.04s / Desync Risk", 
                    delta_color="inverse"
                )
            with t_col2:
                # Explicitly showing Subject: Pseudo with zero gender mentions
                current_pseudo = st.session_state['user_profile']['pseudo']
                st.metric(
                    label=f"👤 Subject Signature", 
                    value=current_pseudo if current_pseudo else "UNIDENTIFIED", 
                    delta="Clearance: SECURE"
                )


# ==============================================================================
# 4. LOGICAL ROUTING & NAVIGATIONAL MAP
# ==============================================================================
home_page = st.Page(
    show_home_page, 
    title="Containment Gateway", 
    icon="🏠", 
    default=True
)

assessment_page = st.Page(
    "pages/01_Assessment.py", 
    title="Neural Scan Matrix", 
    icon="📊"
)

advices_page = st.Page(
    "pages/Advices.py", 
    title="Cognitive Architecture", 
    icon="🧬"
)

chatbot_page = st.Page(
    "pages/Chatbot.py", 
    title="Metacognitive Coach AI", 
    icon="🤖"
)

# Secure routing execution
pg = st.navigation([home_page, assessment_page, advices_page, chatbot_page])
pg.run()