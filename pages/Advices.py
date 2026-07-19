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
    st.warning("⚠️ Access Denied: No cognitive telemetry data detected in active session state.")
    if st.button("Initialize Assessment Sequence", type="primary", use_container_width=True):
        st.switch_page("pages/01_Assessment.py")
    st.stop()

# Safe extraction layer
user_profile = st.session_state.get("user_profile", {})
pseudo = user_profile.get("pseudo", "Subject").strip()
classification = user_profile.get("gender", "Undefined Mapping")
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
        sec_name = q.get('section', 'General Telemetry Core')
        
        if sec_name not in sections_data:
            sections_data[sec_name] = []
            
        sections_data[sec_name].append({
            "question": q.get('question', 'Query Missing'),
            "choice_text": option_data.get('text', 'No option string'),
            "label": option_data.get('label', 'Standard Processing'),
            "advice": option_data.get('advice', 'No direct vector advice available.')
        })
        all_labels.append(option_data.get('label', 'Standard Processing'))

# Double failure backup
if not all_labels:
    st.error("⚠️ Critical Telemetry Failure: Analysis engine could not compile behavioral weights.")
    if st.button("Return to Ingestion Base"):
        st.switch_page("pages/01_Assessment.py")
    st.stop()

# Extract dominant archetype string
raw_dominant = max(set(all_labels), key=all_labels.count)
dominant_archetype = str(raw_dominant).strip()


# ==============================================================================
# 3. PSYCHOMETRIC MATRIX LOOKUP (The Deep "Psychological Shock" Database)
# ==============================================================================
# Comprehensive structural maps containing raw, witty, and profoundly real tactical advice.
# Flexible matching logic protects against formatting mismatches.
ARCHETYPE_STRATEGIES = {
    "PRESSURE SPRINTER": {
        "tagline": "Velocity is your weaponized default; architectural stability is your ticking time bomb.",
        "blind_spots": "You possess an addiction to immediate, visible progress. Under pressure, your brain treats architectural planning as an obstruction rather than an asset. You will write messy, unsustainable code with the mental justification that 'it works for now,' setting up a catastrophic failure vector for your team in the final hours of execution.",
        "crisis_mode": "When the system crashes, your instinctive defensive reflex is to deploy blunt-force hotfixes at moving targets. You rarely pause to isolate the root cause, preferring to out-pace structural decay through sheer brute execution speed.",
        "synergy": "You require immediate structural anchoring by an **Abstract Architect** or a **Systemic Perfectionist**. Left to your own devices, you will build a non-functional house of cards that looks spectacular in a 30-second loop but collapses under rigorous scrutiny."
    },
    "ABSTRACT ARCHITECT": {
        "tagline": "Elegant conceptual models that risk dying in the vacuum of non-deployment.",
        "blind_spots": "Paralysis by analysis is your primary failure mode. Your cognitive bandwidth is heavily biased toward systemic elegance, modular scalability, and flawless abstract hierarchies. The harsh truth? A messy, functional prototype shipped on time will always beat a flawless, half-finished architectural blueprint.",
        "crisis_mode": "When deadlines shrink or variables break, your defensive mechanism is retreat. You will spend precious hours restructuring database definitions or writing exhaustive documentation instead of deploying a crude, working patch.",
        "synergy": "You must be paired with a **Pressure Sprinter** or a **Pragmatic Executor** who possesses the authority to aggressively cut your scope and force you to ship dirty, raw code before the clock runs out."
    },
    "SYSTEMIC PERFECTIONIST": {
        "tagline": "Uncompromising quality standards that can accidentally throttle delivery pipelines.",
        "blind_spots": "Your cognitive architecture treats edge cases as existential threats. You will spend six hours optimizing a secondary algorithm or cleaning up indentation while the core user workflow remains fundamentally broken. Your inability to compromise on internal execution quality makes you a major liability under compressed timelines.",
        "crisis_mode": "Faced with structural chaos or sudden scope pivots, you freeze or become defensive. You treat necessary shortcuts as personal insults, often wasting time fixing code that is scheduled to be completely deleted.",
        "synergy": "You desperately need a **Chaos Engine** or a **Pressure Sprinter** to yank you out of the micro-details and remind you that a feature doesn't need to be perfect; it just needs to survive the jury's demonstration."
    },
    "CHAOS ENGINE": {
        "tagline": "A non-linear generator of radical insights with a complete disdain for execution continuity.",
        "blind_spots": "You suffer from severe conceptual object-permanence issues. You will advocate for a total concept pivot halfway through a tight schedule because you found a more 'fascinating' angle. You leave a trail of half-finished experimental features, expecting others to handle the grueling work of debugging and integration.",
        "crisis_mode": "In high-stress environments, you thrive on high-risk maneuvers. You will gladly introduce a completely unverified library or tech stack at midnight, entirely blind to the integration bottleneck you've just forced upon your team.",
        "synergy": "You are useless without a **Systemic Perfectionist** or a **Pragmatic Executor** to act as your operational guardrails. They translate your creative explosions into stable, deployable components."
    }
}

# Standardized normalization fallback strategy
norm_key = dominant_archetype.upper()
strategy_block = ARCHETYPE_STRATEGIES.get(norm_key)

# Dynamic fallback generator if a custom label is introduced upstream
if not strategy_block:
    strategy_block = {
        "tagline": f"Hybrid profile mapping heavily into the {dominant_archetype} spectrum.",
        "blind_spots": "Your unique behavioral distribution shows high adaptive flexibility, but your primary danger lies in fluctuating between conceptual depth and execution speed without a clear strategic anchor.",
        "crisis_mode": "Under intense load, your profile reverts to tactical isolationism. You stop communicating your internal state to the team, resulting in siloed data structures.",
        "synergy": "You balance well with hyper-specialized profiles who can provide either rigid technical guardrails or raw, unadulterated execution speed."
    }


# ==============================================================================
# 4. HIGH-IMPACT METAC0GNITIVE REPORT RENDERING
# ==============================================================================
st.markdown("<p style='color: #6366F1; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: -10px;'>Diagnostic Output</p>", unsafe_allow_html=True)
st.title("🧬 Core Cognitive Architecture Report")
st.divider()

# High-precision identification metrics display
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="CORE SUBJECT ALIAS", value=pseudo.upper())
with col2:
    st.metric(label="OPERATIONAL COHORT", value=classification.upper())
with col3:
    st.metric(label="DOMINANT INTELLECTUAL VECTOR", value=dominant_archetype.upper())

st.write("")
st.write("")

# Asymmetric Split layout: Left = The Shocking Blueprint, Right = Weight Distribution
left_layout, right_layout = st.columns([5, 4], gap="large")

with left_layout:
    st.markdown("### 🛠️ Dynamic Blueprint Generator")
    st.caption("Custom-compiled execution guardrails tailored to your dominant cognitive traits.")
    
    # Premium styled warning callout box with zero corporate fluff
    st.markdown(f"""
    <div style="background-color: #1E1E2E; border-left: 4px solid #6366F1; padding: 18px; border-radius: 6px; margin-bottom: 20px;">
        <div style="font-weight: 700; color: #F3F4F6; font-size: 16px; margin-bottom: 4px;">ARCHETYPE ANALYSIS: {dominant_archetype.upper()}</div>
        <div style="font-style: italic; color: #9CA3AF; font-size: 14px;">"{strategy_block['tagline']}"</div>
    </div>
    """, unsafe_allow_html=True)

    # Modular blocks perfectly isolated for clean future PDF/JSON export structures
    with st.container(border=True):
        st.markdown("🚨 **CRITICAL BLIND SPOTS**")
        st.markdown(strategy_block["blind_spots"])

    st.write("")
    with st.container(border=True):
        st.markdown("🔥 **CRISIS MANAGEMENT DEFAULTS**")
        st.markdown(strategy_block["crisis_mode"])

    st.write("")
    with st.container(border=True):
        st.markdown("🤝 **STRATEGIC SYNERGISTIC PARTNERS**")
        st.markdown(strategy_block["synergy"])

with right_layout:
    st.markdown("### 📊 Spectrum Weight Distribution")
    st.caption("Quantified representation of behavioral priorities across all processed nodes.")
    st.write("")
    
    label_counts = Counter(all_labels)
    total_metrics = len(all_labels)
    
    # Clean programmatic progress bar distribution rendering
    for label_name, count in label_counts.items():
        percentage = int((count / total_metrics) * 100)
        st.markdown(f"**{label_name} Metric Weight**")
        st.progress(count / total_metrics, text=f"{percentage}% ({count} / {total_metrics} Nodes)")
        st.write("")


# ==============================================================================
# 5. SUBSYSTEM INSPECTION MATRIX (Granular Node Data Tabs)
# ==============================================================================
st.write("")
st.divider()
st.markdown("### 🔍 Granular Subsystem Data Ledger")
st.caption("Audit trail of trace behaviors recorded by individual question triggers.")
st.write("")

# Extract clean tab labels by dropping technical section prefixes
tab_names = [name.split(":")[1].strip() if ":" in name else name for name in sections_data.keys()]

if tab_names:
    tabs = st.tabs(tab_names)
    for tab, (sec_full_name, items) in zip(tabs, sections_data.items()):
        with tab:
            st.write("")
            for index, item in enumerate(items):
                with st.expander(f"Node Marker {index + 1:02d} | Factor: {item['label']}"):
                    st.markdown(f"**Trigger Context:** *{item['question']}*")
                    st.markdown(f"**Recorded Action Response:** `{item['choice_text']}`")
                    st.divider()
                    st.info(f"🧠 **Vector Remediation Insight:** {item['advice']}")
else:
    st.info("No layered partitions compiled yet.")


# ==============================================================================
# 6. SECURE COMPILATION FOOTER
# ==============================================================================
st.write("")
st.divider()
col_foot1, col_foot2 = st.columns([3, 1])

with col_foot1:
    st.caption("LUMEN Metacognitive Profiler • Core Engine Version v1.4.2-STABLE • Local Architectural State Encrypted")

with col_foot2:
    if st.button("Purge Telemetry & Restart 🔄", use_container_width=True, type="secondary"):
        st.session_state.answers = {}
        st.session_state.current_q = 0
        st.session_state.flags["scan_completed"] = False
        st.session_state.flags["chatbot_unlocked"] = False
        st.switch_page("pages/01_Assessment.py")