import streamlit as st
from collections import Counter
from data.question import ALL_QUESTIONS

# ==============================================================================
# 1. PARANOIA ENGINE: RUNTIME SECURITY & ENVIRONMENT INTEGRITY LOCK
# ==============================================================================
if 'answers' not in st.session_state or not st.session_state.answers:
    st.error("🛑 SECURITY BREACH: No answers detected in session memory.")
    st.markdown("You must complete the assessment before accessing this encrypted report.")
    if st.button("🚀 Return to Assessment", type="primary", use_container_width=True):
        st.switch_page("pages/01_Assessment.py") 
    st.stop()

if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {"pseudo": "Anonymous Builder", "gender": "Unmapped", "initialized": True}

# Safe extraction layer using .get() to prevent hard crashes
user_profile = st.session_state.user_profile
pseudo = user_profile.get("pseudo", "Anonymous Builder").strip() or "Operator"
classification = user_profile.get("gender", "Unmapped Human")
answers = st.session_state.answers


# ==============================================================================
# 2. DATA PARSING ENGINE (STRICT ISOLATION PROTOCOL)
# ==============================================================================
sections_data = {}
all_labels = []

if not ALL_QUESTIONS:
    st.error("⚠️ CRITICAL: The global ALL_QUESTIONS database is empty or missing.")
    st.stop()

for q in ALL_QUESTIONS:
    q_id = q.get('id')
    
    # Safe check to ensure we only process valid IDs
    if q_id and q_id in answers:
        user_choice_key = answers.get(q_id) 
        
        # Deep dictionary validation
        options = q.get("options", {})
        if user_choice_key in options:
            option_data = options[user_choice_key]
            sec_name = q.get('section', 'General Mindset')
            
            if sec_name not in sections_data:
                sections_data[sec_name] = []
                
            sections_data[sec_name].append({
                "q_id": str(q_id),
                "question": q.get('question', 'Missing Question'),
                "choice_text": option_data.get('text', 'No selection'),
                "label": option_data.get('label', 'Standard Processing'),
                "advice": option_data.get('advice', 'No direct advice available.')
            })
            
            all_labels.append(option_data.get('label', 'Standard Processing'))

if not all_labels:
    st.error("⚠️ GHOST TOWN ALERT: We couldn't extract any behavioral patterns. The data matrix is empty.")
    if st.button("🔄 Try Assessment Again"):
        st.switch_page("pages/01_Assessment.py")
    st.stop()

# Deterministic extraction (safer than max(set) in case of ties)
label_counts = Counter(all_labels)
dominant_archetype = str(label_counts.most_common(1)[0][0]).strip()


# ==============================================================================
# 3. PSYCHOMETRIC MATRIX LOOKUP 
# ==============================================================================
ARCHETYPE_STRATEGIES = {
    "PRESSURE SPRINTER": {
        "tagline": "Fuelled by deadline panic, energy drinks, and pure willpower.",
        "blind_spots": "You love ship-it-now chaos. Under pressure, 'clean code' and documentation look like useless friction to you.",
        "crisis_mode": "When stuff hits the fan, you slap duct-tape hotfixes on moving parts. You rarely stop to ask *why* it broke.",
        "synergy": "Pair up immediately with an **Abstract Architect** or a **Systemic Perfectionist**."
    },
    "ABSTRACT ARCHITECT": {
        "tagline": "Mastermind behind flawless systems... that might never actually be deployed.",
        "blind_spots": "Analysis paralysis is your nemesis. You get so obsessed with grand architecture that you forget the clock is ticking.",
        "crisis_mode": "When the deadline shrinks, you freeze or retreat. You’ll spend precious minutes refactoring database relations.",
        "synergy": "You desperately need a **Pressure Sprinter** or a **Pragmatic Executor** next to you to cut your wild scope."
    },
    "SYSTEMIC PERFECTIONIST": {
        "tagline": "Zero tolerance for bad code, missing edge cases, or uneven indentation.",
        "blind_spots": "Edge cases haunt your dreams. You’ll spend hours tweaking a secondary function while the main app is broken.",
        "crisis_mode": "When the plan collapses, you panic or get defensive. You waste time fixing code that was supposed to be thrown away.",
        "synergy": "You need a **Chaos Engine** or a **Pressure Sprinter** to drag you out of the weeds."
    },
    "CHAOS ENGINE": {
        "tagline": "Unfiltered genius idea factory with a total allergy to finish lines.",
        "blind_spots": "Mid-project, you’ll suggest pivoting the entire app because you found a cooler framework.",
        "crisis_mode": "Under intense stress, you go full wildcard. You’ll randomly swap out core libraries at midnight.",
        "synergy": "You're useless without a **Systemic Perfectionist** or a **Pragmatic Executor** acting as your handler."
    }
}

norm_key = dominant_archetype.upper()
strategy_block = ARCHETYPE_STRATEGIES.get(norm_key, {
    "tagline": f"A highly adaptable wildcard leaning heavily into the {dominant_archetype} frequency.",
    "blind_spots": "You flip between deep overthinking and frantic rushing without a clear game plan.",
    "crisis_mode": "When stress hits peak level, communication dies, and siloed code follows.",
    "synergy": "You pair best with laser-focused specialists who provide clear guardrails."
})


# ==============================================================================
# 4. HIGH-IMPACT REPORT RENDERING
# ==============================================================================
st.markdown("<p style='color: #6366F1; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: -10px;'>Diagnostic Unlocked</p>", unsafe_allow_html=True)
st.title("🧬 Your Builder Blueprint")
st.divider()

col1, col2, col3 = st.columns(3)
col1.metric(label="BUILDER ALIAS", value=pseudo.upper())
col2.metric(label="OPERATIONAL PROFILE", value=classification.upper())
col3.metric(label="DOMINANT ARCHETYPE", value=dominant_archetype.upper())

st.write("")
st.write("")

left_layout, right_layout = st.columns([5, 4], gap="large")

with left_layout:
    st.markdown("### 🛠️ Hackathon Survival Guide")
    st.caption("Tailored tactical advice so you don't accidentally sabotage your team.")
    
    st.markdown(f"""
    <div style="background-color: #1E1E2E; border-left: 4px solid #6366F1; padding: 18px; border-radius: 6px; margin-bottom: 20px;">
        <div style="font-weight: 700; color: #F3F4F6; font-size: 16px; margin-bottom: 4px;">ARCHETYPE: {dominant_archetype.upper()}</div>
        <div style="font-style: italic; color: #9CA3AF; font-size: 14px;">"{strategy_block['tagline']}"</div>
    </div>
    """, unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("🚨 **YOUR BIGGEST BLIND SPOTS**")
        st.markdown(strategy_block["blind_spots"])

    with st.container(border=True):
        st.markdown("🔥 **WHAT HAPPENS IN CRISIS MODE**")
        st.markdown(strategy_block["crisis_mode"])

    with st.container(border=True):
        st.markdown("🤝 **YOUR DREAM TEAMMATE**")
        st.markdown(strategy_block["synergy"])

with right_layout:
    st.markdown("### 📊 Mindset Breakdown")
    st.caption("The exact blend of traits powering your decisions.")
    st.write("")
    
    total_metrics = len(all_labels)
    sorted_labels = label_counts.most_common()
    
    for label_name, count in sorted_labels:
        percentage = int((count / total_metrics) * 100)
        st.markdown(f"**{label_name}**")
        st.progress(count / total_metrics, text=f"{percentage}% ({count}/{total_metrics} signals)")
        st.write("")


# ==============================================================================
# 5. SUBSYSTEM INSPECTION MATRIX 
# ==============================================================================
st.write("")
st.divider()
st.markdown("### 🔍 Tactical Advice Archive")
st.caption("Based strictly on your choices, here is the granular breakdown by section.")
st.write("")

if sections_data:
    tab_names = [name.split(":")[1].strip() if ":" in name else name for name in sections_data.keys()]
    # Protection against empty keys generating invalid tabs
    valid_tabs = [name for name in tab_names if name] 
    
    if valid_tabs:
        tabs = st.tabs(valid_tabs)
        for tab, (sec_full_name, items) in zip(tabs, sections_data.items()):
            with tab:
                st.write("")
                for item in items:
                    with st.expander(f"Question {item['q_id']} | Trait Detected: {item['label']}"):
                        st.markdown(f"**Scenario:** *{item['question']}*")
                        st.markdown(f"**Your Choice:** `{item['choice_text']}`")
                        st.divider()
                        st.info(f"💡 **Tactical Remediation:** {item['advice']}")
else:
    st.info("No detailed signals logged yet.")


# ==============================================================================
# 6. SECURE COMPILATION FOOTER
# ==============================================================================
st.write("")
st.divider()
col_foot1, col_foot2 = st.columns([3, 1])

with col_foot1:
    st.caption("LUMEN Metacognitive Profiler • Local & Private Engine")

with col_foot2:
    if st.button("Start Over 🔄", use_container_width=True, type="secondary"):
        st.session_state.answers = {}
        if "current_q_idx" in st.session_state:
            st.session_state.current_q_idx = 0
        if "flags" in st.session_state:
            st.session_state.flags["scan_completed"] = False
            st.session_state.flags["chatbot_unlocked"] = False
        st.switch_page("pages/01_Assessment.py")