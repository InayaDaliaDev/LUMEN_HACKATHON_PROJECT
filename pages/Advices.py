import streamlit as st
from data.question import ALL_QUESTIONS
from collections import Counter

# ==============================================================================
# 1. RUNTIME SECURITY & ENVIRONMENT INTEGRITY LOCK
# ==============================================================================
# CRITICAL SAFETIES: 
# - NO st.set_page_config() allowed here to prevent instantaneous application crash.
# - Immediate URL interceptor if a user bypasses the onboarding sequence.

if 'answers' not in st.session_state or not st.session_state.answers or 'user_profile' not in st.session_state:
    st.warning("⚠️ Whoa there, ninja! You skipped the test. We need your inputs first.")
    if st.button("🚀 Take the Assessment", type="primary", use_container_width=True):
        st.switch_page("pages/01_Assessment.py")
    st.stop()

# Safe extraction layer
user_profile = st.session_state.get("user_profile", {})
pseudo = user_profile.get("pseudo", "Anonymous Builder").strip()
classification = user_profile.get("gender", "Unmapped Human")
answers = st.session_state.answers


# ==============================================================================
# 2. DATA PARSING ENGINE & ARCHETYPE CONVERGENCE
# ==============================================================================
sections_data = {}
all_labels = []

for q in ALL_QUESTIONS:
    q_id = q.get('id')
    if q_id in answers:
        user_choice = answers[q_id]
        
        # Anti-corruption fallback filter
        if "options" not in q or user_choice not in q["options"]:
            continue
            
        option_data = q["options"][user_choice]
        sec_name = q.get('section', 'General Mindset')
        
        if sec_name not in sections_data:
            sections_data[sec_name] = []
            
        sections_data[sec_name].append({
            "question": q.get('question', 'Missing Question'),
            "choice_text": option_data.get('text', 'No selection'),
            "label": option_data.get('label', 'Standard Processing'),
            "advice": option_data.get('advice', 'No direct advice available.')
        })
        all_labels.append(option_data.get('label', 'Standard Processing'))

# Double failure backup
if not all_labels:
    st.error("⚠️ Ghost Town Alert: We couldn't extract any behavioral patterns from your answers.")
    if st.button("🔄 Try Assessment Again"):
        st.switch_page("pages/01_Assessment.py")
    st.stop()

# Extract dominant archetype string
raw_dominant = max(set(all_labels), key=all_labels.count)
dominant_archetype = str(raw_dominant).strip()


# ==============================================================================
# 3. PSYCHOMETRIC MATRIX LOOKUP (The Deep "Psychological Shock" Database)
# ==============================================================================
ARCHETYPE_STRATEGIES = {
    "PRESSURE SPRINTER": {
        "tagline": "Fuelled by deadline panic, energy drinks, and pure willpower.",
        "blind_spots": "You love ship-it-now chaos. Under pressure, 'clean code' and documentation look like useless friction to you. You'll happily deploy spaghetti code at 3 AM because *it works right now*, leaving a ticking tech-debt timebomb for your team to debug during demo time.",
        "crisis_mode": "When stuff hits the fan, you slap duct-tape hotfixes on moving parts. You rarely stop to ask *why* it broke; you just try to outrun the bugs with brute speed.",
        "synergy": "Pair up immediately with an **Abstract Architect** or a **Systemic Perfectionist**. Left alone, you'll build a flashy castle of cards that looks amazing in a 10-second demo but crashes the second a judge touches it."
    },
    "ABSTRACT ARCHITECT": {
        "tagline": "Mastermind behind flawless systems... that might never actually be deployed.",
        "blind_spots": "Analysis paralysis is your nemesis. You get so obsessed with grand architecture, elegant schemas, and modular scalability that you forget the clock is ticking. Newsflash: a messy working prototype beats a half-finished masterpiece every single time.",
        "crisis_mode": "When the deadline shrinks, you freeze or retreat. Instead of shipping a dirty working patch, you’ll spend precious minutes refactoring database relations or tweaking UI padding.",
        "synergy": "You desperately need a **Pressure Sprinter** or a **Pragmatic Executor** next to you to cut your wild scope and force you to hit *Deploy* before time runs out."
    },
    "SYSTEMIC PERFECTIONIST": {
        "tagline": "Zero tolerance for bad code, missing edge cases, or uneven indentation.",
        "blind_spots": "Edge cases haunt your dreams. You’ll spend 3 hours tweaking a secondary sorting function while the main checkout button is still completely broken. Your refusal to ship 'good enough' code turns you into a bottleneck when time is tight.",
        "crisis_mode": "When the plan collapses, you panic or get defensive. You treat quick hacks as personal insults and waste precious minutes fixing code that was supposed to be thrown away anyway.",
        "synergy": "You need a **Chaos Engine** or a **Pressure Sprinter** to drag you out of the weeds and remind you that done is infinitely better than perfect."
    },
    "CHAOS ENGINE": {
        "tagline": "Unfiltered genius idea factory with a total allergy to finish lines.",
        "blind_spots": "You have the tech attention span of a goldfish. Mid-hackathon, you’ll suggest pivoting the entire app because you found a cooler AI framework. You leave behind a graveyard of half-baked features and expect your teammates to wire them together.",
        "crisis_mode": "Under intense stress, you go full wildcard. You’ll randomly swap out core libraries at midnight, totally oblivious to the integration nightmare you just forced on everyone else.",
        "synergy": "You're useless without a **Systemic Perfectionist** or a **Pragmatic Executor** acting as your handler. They turn your crazy ideas into actual working features."
    }
}

# Standardized normalization fallback strategy
norm_key = dominant_archetype.upper()
strategy_block = ARCHETYPE_STRATEGIES.get(norm_key)

# Dynamic fallback generator if a custom label is introduced upstream
if not strategy_block:
    strategy_block = {
        "tagline": f"A hybrid wild-card leaning heavily into the {dominant_archetype} frequency.",
        "blind_spots": "You're highly adaptable, but your main trap is flipping between deep overthinking and frantic rushing without a clear game plan.",
        "crisis_mode": "When stress hits peak level, you lock yourself in a bubble and stop talking to your team. Communication dies, and siloed code follows.",
        "synergy": "You pair best with laser-focused specialists who can give you clear guardrails or raw, uninterrupted momentum."
    }


# ==============================================================================
# 4. HIGH-IMPACT METACOGNITIVE REPORT RENDERING
# ==============================================================================
st.markdown("<p style='color: #6366F1; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: -10px;'>Diagnostic Unlocked</p>", unsafe_allow_html=True)
st.title("🧬 Your Builder Blueprint")
st.divider()

# High-precision identification metrics display
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="BUILDER ALIAS", value=pseudo.upper())
with col2:
    st.metric(label="OPERATIONAL PROFILE", value=classification.upper())
with col3:
    st.metric(label="DOMINANT ARCHETYPE", value=dominant_archetype.upper())

st.write("")
st.write("")

# Asymmetric Split layout: Left = The Shocking Blueprint, Right = Weight Distribution
left_layout, right_layout = st.columns([5, 4], gap="large")

with left_layout:
    st.markdown("### 🛠️ Hackathon Survival Guide")
    st.caption("Tailored tactical advice so you don't accidentally sabotage your team.")
    
    # Premium styled warning callout box with zero corporate fluff
    st.markdown(f"""
    <div style="background-color: #1E1E2E; border-left: 4px solid #6366F1; padding: 18px; border-radius: 6px; margin-bottom: 20px;">
        <div style="font-weight: 700; color: #F3F4F6; font-size: 16px; margin-bottom: 4px;">ARCHETYPE: {dominant_archetype.upper()}</div>
        <div style="font-style: italic; color: #9CA3AF; font-size: 14px;">"{strategy_block['tagline']}"</div>
    </div>
    """, unsafe_allow_html=True)

    # Modular blocks perfectly isolated for clean future PDF/JSON export structures
    with st.container(border=True):
        st.markdown("🚨 **YOUR BIGGEST BLIND SPOTS**")
        st.markdown(strategy_block["blind_spots"])

    st.write("")
    with st.container(border=True):
        st.markdown("🔥 **WHAT HAPPENS IN CRISIS MODE**")
        st.markdown(strategy_block["crisis_mode"])

    st.write("")
    with st.container(border=True):
        st.markdown("🤝 **YOUR DREAM TEAMMATE**")
        st.markdown(strategy_block["synergy"])

with right_layout:
    st.markdown("### 📊 Mindset Breakdown")
    st.caption("The exact blend of traits powering your decisions.")
    st.write("")
    
    label_counts = Counter(all_labels)
    total_metrics = len(all_labels)
    
    # Clean programmatic progress bar distribution rendering
    for label_name, count in label_counts.items():
        percentage = int((count / total_metrics) * 100)
        st.markdown(f"**{label_name}**")
        st.progress(count / total_metrics, text=f"{percentage}% ({count} / {total_metrics} signals)")
        st.write("")


# ==============================================================================
# 5. SUBSYSTEM INSPECTION MATRIX (Granular Node Data Tabs)
# ==============================================================================
st.write("")
st.divider()
st.markdown("### 🔍 The Decision Audit Trail")
st.caption("A deep dive into how your responses shaped this diagnostic.")
st.write("")

# Extract clean tab labels by dropping technical section prefixes
tab_names = [name.split(":")[1].strip() if ":" in name else name for name in sections_data.keys()]

if tab_names:
    tabs = st.tabs(tab_names)
    for tab, (sec_full_name, items) in zip(tabs, sections_data.items()):
        with tab:
            st.write("")
            for index, item in enumerate(items):
                with st.expander(f"Signal #{index + 1:02d} | Trait: {item['label']}"):
                    st.markdown(f"**Scenario:** *{item['question']}*")
                    st.markdown(f"**Your Choice:** `{item['choice_text']}`")
                    st.divider()
                    st.info(f"🧠 **Tactical Remediation:** {item['advice']}")
else:
    st.info("No detailed signals logged yet.")


# ==============================================================================
# 6. SECURE COMPILATION FOOTER
# ==============================================================================
st.write("")
st.divider()
col_foot1, col_foot2 = st.columns([3, 1])

with col_foot1:
    st.caption("LUMEN Metacognitive Profiler • Built for Hackathon Excellence • All sessions local & private")

with col_foot2:
    if st.button("Start Over 🔄", use_container_width=True, type="secondary"):
        st.session_state.answers = {}
        st.session_state.current_q = 0
        st.session_state.flags["scan_completed"] = False
        st.session_state.flags["chatbot_unlocked"] = False
        st.switch_page("pages/01_Assessment.py")