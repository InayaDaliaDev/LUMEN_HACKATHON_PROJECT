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
# 3. ELITE UI/UX: THE CHRONOS CONTROL MATRIX
# ==============================================================================
st.markdown("""
<style>
    .chronos-title {
        background: linear-gradient(90deg, #3B82F6 0%, #10B981 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 2.8rem;
        letter-spacing: -1.5px;
    }
    .matrix-box {
        background-color: #0F172A;
        border: 1px solid #1E293B;
        padding: 24px;
        border-radius: 14px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        margin-bottom: 25px;
    }
    .telemetry-badge {
        background-color: #1E293B;
        color: #38BDF8;
        border: 1px solid #334155;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='chronos-title'>CHRONOS // Multiverse Trajectory Engine</h1>", unsafe_allow_html=True)
st.markdown(f"<span><span class='telemetry-badge'>OPERATOR: {pseudo.upper()}</span> <span class='telemetry-badge'>SIGNATURE: {dominant_archetype}</span></span>", unsafe_allow_html=True)
st.write("")
st.divider()

# Simulation Parameters Console
with st.container():
    st.markdown("<div class='matrix-box'>", unsafe_allow_html=True)
    st.markdown("### 🎛️ Configure Environmental Parameters")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        sim_level = st.selectbox("Academic Tier", ["Middle School", "High School", "University / College"])
    with col2:
        sim_type = st.selectbox("Institutional Framework", ["Public System", "Private / Elite Academy"])
    with col3:
        sim_region = st.selectbox("Geopolitical Region", ["Africa", "Europe", "North America", "Asia"])
        
    st.markdown("</div>", unsafe_allow_html=True)

# Sidebar Configuration for Groq API
with st.sidebar:
    st.markdown("### ⚙️ Engine Matrix (Groq API)")
    default_key = st.secrets.get("GROQ_API_KEY", "") if "GROQ_API_KEY" in st.secrets else ""
    groq_api_key = st.text_input("Groq API Key:", value=default_key, type="password", placeholder="gsk_...")
    selected_model = st.selectbox("Inference Model:", ["llama-3.3-70b-versatile", "llama-3.1-70b-versatile"], index=0)
    
    st.divider()
    if st.button("Purge Timeline Memory 🧹", use_container_width=True, type="secondary"):
        st.session_state.chrono_messages = []
        st.rerun()

# Initialize session state for the simulation chat
if "chrono_messages" not in st.session_state:
    st.session_state.chrono_messages = []


# ==============================================================================
# 4. THE MASTERPIECE PROMPT: CHRONOS-v3.3 SOCIOCOGNITIVE ENGINE
# ==============================================================================
SYSTEM_PROMPT = f"""
[SYSTEM ARCHITECTURE: CHRONOS-v3.3 PREDICTIVE SIMULATION ENGINE]
ROLE: You are CHRONOS, an enterprise-grade Epistemic Simulation Engine and Sociocognitive Architect. You possess absolute mastery over global educational systems, institutional sociology, and cognitive profiling. Your mission is to simulate the exact friction points, systemic bottlenecks, and psychological trajectories of an elite operator when embedded in a specific global educational framework.

[OPERATOR TELEMETRY]
- Designation: {pseudo}
- Dominant Cognitive Archetype: {dominant_archetype}
- Primary Vector Advantage: {vector_labels[strongest_key]} ({vector_totals[strongest_key]:.1f})
- Critical Vulnerability Vector: {vector_labels[weakest_key]} ({vector_totals[weakest_key]:.1f})

[ENVIRONMENTAL PARAMETERS]
- Academic Tier: {sim_level}
- Institutional Framework: {sim_type}
- Geopolitical Coordinates: {sim_region}

[EXECUTION PROTOCOL (CHAIN OF THOUGHT)]
1. INSTITUTIONAL REALITY MATRIX: Describe the unvarnished, systemic realities of a {sim_type} {sim_level} in {sim_region} (e.g., structural bureaucracy, competitive pressures, pedagogical methodologies, resource constraints, or evaluation metrics). Avoid generic fluff; use precise institutional sociology.
2. THE COGNITIVE COLLISION: Analyze the precise vector intersection between the Operator's '{dominant_archetype}' profile and this environment. Where does their {vector_labels[strongest_key]} yield an unfair asymmetric advantage? Where does their {vector_labels[weakest_key]} trigger a catastrophic system failure?
3. PROGNOSTIC TRAJECTORY: Deliver a high-precision forecast of their academic adaptation curve over a 12-month horizon. 
4. TACTICAL REMEDIATION PROTOCOL: Issue an uncompromising, highly structured, non-generic blueprint for structural survival and absolute dominance in this environment.

[STYLING & CONSTRAINTS]
- Tone: Absolute authority, clinical precision, deeply analytical, intellectually elevating, and profoundly serious. No corporate pleasantries or generic AI fluff ("As an AI..."). 
- Formatting: Advanced Markdown architecture. Use bold headers, explicit metric notation, and structured lists.
- Post-Generation Interaction: Once the initial simulation report is deployed, remain fully in-character as the simulation engine, answering follow-up queries or adapting the simulation parameters based on the Operator's decisions in real-time.
"""


# ==============================================================================
# 5. SIMULATION EXECUTION & DYNAMIC RENDERING
# ==============================================================================
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    if st.button("🌌 EXECUTE TIMELINE SIMULATION", use_container_width=True, type="primary"):
        if not groq_api_key:
            st.error("⚠️ CRITICAL: Groq API Key required to initialize the Chronos engine.")
            st.stop()
            
        # Reset and trigger initial run via hidden command
        st.session_state.chrono_messages = []
        init_command = f"System directive: Initialize simulation sequence for {pseudo} in a {sim_type} {sim_level} within {sim_region}."
        st.session_state.chrono_messages.append({"role": "user", "content": init_command, "hidden": True})

# Render Visible Chat History
for msg in st.session_state.chrono_messages:
    if not msg.get("hidden", False):
        avatar = "🌐" if msg["role"] == "assistant" else "👤"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

# Automatic execution if triggered
if st.session_state.chrono_messages and st.session_state.chrono_messages[-1]["role"] == "user" and st.session_state.chrono_messages[-1].get("hidden", False):
    with st.chat_message("assistant", avatar="🌐"):
        message_placeholder = st.empty()
        full_response = ""
        
        formatted_messages = [SystemMessage(content=SYSTEM_PROMPT)]
        for m in st.session_state.chrono_messages:
            if m["role"] == "user":
                formatted_messages.append(HumanMessage(content=m["content"]))
            else:
                formatted_messages.append(AIMessage(content=m["content"]))
            
        try:
            llm = ChatGroq(
                model=selected_model,
                api_key=groq_api_key,
                temperature=0.6,
                streaming=True
            )
            for chunk in llm.stream(formatted_messages):
                full_response += chunk.content
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            st.session_state.chrono_messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"❌ Simulation Core Failure: {str(e)}")

# Real-time Interactive Follow-up
if prompt := st.chat_input("Interact with the simulation timeline (e.g., 'What happens if I skip lectures to build an independent project?')..."):
    if not groq_api_key:
        st.error("⚠️ CRITICAL: Groq API Key required.")
        st.stop()
        
    st.session_state.chrono_messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🌐"):
        message_placeholder = st.empty()
        full_response = ""

        formatted_messages = [SystemMessage(content=SYSTEM_PROMPT)]
        for m in st.session_state.chrono_messages:
            if m["role"] == "user":
                formatted_messages.append(HumanMessage(content=m["content"]))
            else:
                formatted_messages.append(AIMessage(content=m["content"]))

        try:
            llm = ChatGroq(
                model=selected_model,
                api_key=groq_api_key,
                temperature=0.6,
                streaming=True
            )
            for chunk in llm.stream(formatted_messages):
                full_response += chunk.content
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            st.session_state.chrono_messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"❌ Simulation Core Failure: {str(e)}")