import streamlit as st
import os

# Secure Dependency Injection for LangChain & Groq
try:
    from langchain_groq import ChatGroq
    from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
except ImportError:
    st.error("⚠️ CRITICAL FAULT: Missing core dependencies. Execute: pip install langchain langchain-groq groq")
    st.stop()

# ==============================================================================
# 1. ARCHITECTURAL SAFEGUARDS & STATE MANAGEMENT
# ==============================================================================
if 'answers' not in st.session_state or not st.session_state.answers:
    st.error("🛑 ACCESS DENIED: Neural baseline not established. Complete the diagnostic scan first.")
    if st.button("🚀 Initiate Assessment", type="primary", use_container_width=True):
        st.switch_page("Quiz.py")
    st.stop()

user_profile = st.session_state.get("user_profile", {})
pseudo = user_profile.get("pseudo", "Operator").strip()
answers = st.session_state.get("answers", {})

try:
    from data.question import ALL_QUESTIONS
except ImportError:
    st.error("⚠️ Missing database connection to `data.question.ALL_QUESTIONS`")
    st.stop()

# ==============================================================================
# 2. COGNITIVE TELEMETRY EXTRACTION ENGINE
# ==============================================================================
all_labels = []
vector_totals = {
    "information_bandwidth": 0.0,
    "execution_rigor": 0.0,
    "chaos_tolerance": 0.0,
    "cognitive_endurance": 0.0
}

for q in ALL_QUESTIONS:
    q_id = q.get('id')
    if q_id in answers:
        choice_key = answers[q_id]
        opt = q["options"].get(choice_key, {})
        all_labels.append(opt.get("label", "Unmapped"))
        for v_key, v_val in opt.get("vectors", {}).items():
            if v_key in vector_totals:
                vector_totals[v_key] += float(v_val)

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
        border: 1px style solid #27272A;
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

# Historical Era Configuration Panel
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

# Sidebar Configuration for Groq API
with st.sidebar:
    st.markdown("### ⚙️ Engine Matrix (Groq API)")
    default_key = st.secrets.get("GROQ_API_KEY", "") if "GROQ_API_KEY" in st.secrets else ""
    groq_api_key = st.text_input("Groq API Key:", value=default_key, type="password", placeholder="gsk_...")
    selected_model = st.selectbox("Inference Model:", ["llama-3.3-70b-versatile", "llama-3.1-70b-versatile"], index=0)
    
    st.divider()
    if st.button("Reset Timeline ⏳", use_container_width=True, type="secondary"):
        st.session_state.history_messages = []
        st.rerun()

# Initialize session state for historical immersion chat
if "history_messages" not in st.session_state:
    st.session_state.history_messages = []


# ==============================================================================
# 4. THE MASTERPIECE PROMPT: HISTORICAL IMMERSION ENGINE
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


# ==============================================================================
# 5. EXECUTION & DYNAMIC RENDERING
# ==============================================================================
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    if st.button("📜 INITIATE TIME-TRAVEL IMMERSION", use_container_width=True, type="primary"):
        if not groq_api_key:
            st.error("⚠️ CRITICAL: Groq API Key required to activate temporal portal.")
            st.stop()
            
        st.session_state.history_messages = []
        init_command = f"System directive: Open temporal portal to {selected_era}. Immerse operator {pseudo} focusing on {immersion_focus}."
        st.session_state.history_messages.append({"role": "user", "content": init_command, "hidden": True})

# Render Visible Chat History
for msg in st.session_state.history_messages:
    if not msg.get("hidden", False):
        avatar = "⏳" if msg["role"] == "assistant" else "👤"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

# Automatic execution if triggered
if st.session_state.history_messages and st.session_state.history_messages[-1]["role"] == "user" and st.session_state.history_messages[-1].get("hidden", False):
    with st.chat_message("assistant", avatar="⏳"):
        message_placeholder = st.empty()
        full_response = ""
        
        formatted_messages = [SystemMessage(content=SYSTEM_PROMPT)]
        for m in st.session_state.history_messages:
            if m["role"] == "user":
                formatted_messages.append(HumanMessage(content=m["content"]))
            else:
                formatted_messages.append(AIMessage(content=m["content"]))
            
        try:
            llm = ChatGroq(
                model=selected_model,
                api_key=groq_api_key,
                temperature=0.7,
                streaming=True
            )
            for chunk in llm.stream(formatted_messages):
                full_response += chunk.content
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            st.session_state.history_messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"❌ Temporal Disruption: {str(e)}")

# Real-time Interactive Follow-up
if prompt := st.chat_input("Speak or respond within the historical simulation..."):
    if not groq_api_key:
        st.error("⚠️ CRITICAL: Groq API Key required.")
        st.stop()
        
    st.session_state.history_messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="⏳"):
        message_placeholder = st.empty()
        full_response = ""

        formatted_messages = [SystemMessage(content=SYSTEM_PROMPT)]
        for m in st.session_state.history_messages:
            if m["role"] == "user":
                formatted_messages.append(HumanMessage(content=m["content"]))
            else:
                formatted_messages.append(AIMessage(content=m["content"]))

        try:
            llm = ChatGroq(
                model=selected_model,
                api_key=groq_api_key,
                temperature=0.7,
                streaming=True
            )
            for chunk in llm.stream(formatted_messages):
                full_response += chunk.content
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            st.session_state.history_messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"❌ Temporal Disruption: {str(e)}")