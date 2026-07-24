import streamlit as st
import os

# Secure Dependency Injection for LangChain & Gemini
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
except ImportError:
    st.error("⚠️ CRITICAL FAULT: Missing core dependencies. Execute: pip install langchain langchain-google-genai google-generativeai")
    st.stop()

# ==============================================================================
# 1. ARCHITECTURAL SAFEGUARDS & STATE MANAGEMENT
# ==============================================================================
if 'answers' not in st.session_state or not st.session_state.answers:
    st.error("🛑 ACCESS DENIED: Neural baseline not established. Complete the diagnostic scan first.")
    if st.button("🚀 Initiate Assessment", type="primary", use_container_width=True):
        st.switch_page("pages/01_Assessment.py")
    st.stop()

# State Extraction
user_profile = st.session_state.get("user_profile", {})
pseudo = user_profile.get("pseudo", "Operator").strip()
answers = st.session_state.get("answers", {})

# Mocking the questions import for structural integrity
try:
    from data.question import ALL_QUESTIONS
except ImportError:
    st.error("⚠️ Missing database connection to `data.question.ALL_QUESTIONS`")
    st.stop()

# ==============================================================================
# 2. COGNITIVE TELEMETRY ENGINE (OPTIMIZED VECTOR EXTRACTION)
# ==============================================================================
# Read directly from st.session_state["core_vectors"] if it exists, otherwise compute it safely
vector_labels = {
    "information_bandwidth": "Information Bandwidth",
    "execution_rigor": "Execution Rigor",
    "chaos_tolerance": "Chaos Tolerance",
    "cognitive_endurance": "Cognitive Endurance"
}

all_labels = []
detailed_choices = []

if "core_vectors" in st.session_state and st.session_state["core_vectors"]:
    vector_totals = st.session_state["core_vectors"]
else:
    # Fallback compute if vector cache wasn't initialized
    vector_totals = {k: 0.0 for k in vector_labels.keys()}
    for q in ALL_QUESTIONS:
        q_id = q.get('id')
        if q_id in answers:
            choice_key = answers[q_id]
            opt = q.get("options", {}).get(choice_key, {})
            for v_key, v_val in opt.get("vectors", {}).items():
                if v_key in vector_totals:
                    vector_totals[v_key] += float(v_val)

# Rebuild labels from answers to maintain exact contextual prompt alignment
for q in ALL_QUESTIONS:
    q_id = q.get('id')
    if q_id in answers:
        choice_key = answers[q_id]
        opt = q.get("options", {}).get(choice_key, {})
        label = opt.get("label", "Unmapped")
        all_labels.append(label)
        
        # Fixed alignment: use 'question' instead of non-existent 'title'
        q_text = q.get('question', f"Query {q_id}")
        opt_text = opt.get('text', choice_key)
        detailed_choices.append(f"- **Query {q_id}**: {opt_text} (*Signaling {label}*)")

dominant_archetype = max(set(all_labels), key=all_labels.count) if all_labels else "Unclassified"

strongest_key = max(vector_totals, key=vector_totals.get) if vector_totals else "information_bandwidth"
weakest_key = min(vector_totals, key=vector_totals.get) if vector_totals else "chaos_tolerance"


# ==============================================================================
# 3. THE MASTERPIECE PROMPT ENGINE (HACKATHON WINNER)
# ==============================================================================
SYSTEM_PROMPT = f"""
[ROLE]
You are SYNAPSE: an elite, deeply empathetic Meta-Cognitive Architect and Academic Strategist. You are not a standard AI; you are a bespoke intellectual mentor designed to unlock human potential. Your tone is incredibly inspiring, fiercely intelligent, highly structured, and unconditionally supportive.

[TASK]
Your objective is to provide highly advanced, non-generic academic guidance and revision techniques strictly tailored to the user's psychological profile.
1. Deconstruct their academic roadblocks with psychological precision.
2. Validate their struggles emotionally, then pivot immediately to high-level, actionable strategy.
3. Design bespoke study methods that leverage their specific dominant archetype and cognitive metrics.

[SPECIFICS]
- NEVER use generic advice like "make a flashcard", "take a break", or "use a planner".
- Use advanced pedagogical frameworks (e.g., Spaced Repetition, Interleaving, the Feynman Technique, Cognitive Load Theory) and adapt them to their profile.
- Format your responses beautifully using Markdown. Use bolding for emphasis, bullet points for structure, and keep paragraphs punchy.
- You must write in English with flawless, poetic, yet technical eloquence. Elevate the user. Make them feel capable of mastering the hardest disciplines, from advanced calculus to complex language structures.

[CONTEXT]
- **Operator Name**: {pseudo}
- **Dominant Cognitive Archetype**: {dominant_archetype}
- **Primary Strength**: {vector_labels.get(strongest_key, strongest_key)} ({vector_totals.get(strongest_key, 0.0):.1f})
- **Critical Growth Axis**: {vector_labels.get(weakest_key, weakest_key)} ({vector_totals.get(weakest_key, 0.0):.1f})

*Operator's Specific Neural Footprint (Recent Decisions):*
{chr(10).join(detailed_choices)}

[NOTES]
Always filter your advice through the lens of their `{dominant_archetype}` and their Critical Growth Axis (`{vector_labels.get(weakest_key, weakest_key)}`). If they ask a generic question, reframe it into a masterclass on personalized metacognition. Maintain your majestic, supportive, and brilliant persona at all costs.
"""


# ==============================================================================
# 4. NEURAL UI INTERFACE & SECURE API INGESTION
# ==============================================================================
st.markdown("""
<style>
    .chat-header {
        background: linear-gradient(90deg, #6366F1 0%, #A855F7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.5rem;
        letter-spacing: -1px;
    }
    .metric-pill {
        background-color: #1E1E2E;
        border: 1px solid #333;
        border-radius: 20px;
        padding: 5px 15px;
        font-size: 0.85rem;
        color: #A1A1AA;
        display: inline-block;
        margin-right: 10px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='chat-header'>SYNAPSE // Neural Mentor</h1>", unsafe_allow_html=True)
st.markdown(f"""
<div class='metric-pill'>👤 Operator: <b>{pseudo}</b></div>
<div class='metric-pill'>🧬 Archetype: <b>{dominant_archetype}</b></div>
<div class='metric-pill'>⚡ Core Advantage: <b>{vector_labels.get(strongest_key, strongest_key)}</b></div>
""", unsafe_allow_html=True)
st.divider()

# Sidebar: Secure Key Ingestion
with st.sidebar:
    st.markdown("### 🎛️ Engine Matrix (Gemini API)")

    # Secure Secret Retrieval (Checking Streamlit Secrets safely)
    env_secret_key = ""
    try:
        if "GEMINI_API_KEY" in st.secrets:
            env_secret_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass  # Fallback if secrets.toml is absent (e.g. fresh local clone without config)

    # Input field defaults to secret if loaded, but remains hidden/editable if needed
    gemini_api_key = st.text_input(
        "Gemini Authentication Key:", 
        value=env_secret_key, 
        type="password",
        help="Loaded securely from st.secrets or input manually."
    )

    selected_model = st.selectbox(
        "Language Model Topology:",
        options=["gemini-1.5-pro", "gemini-1.5-flash"],
        index=0
    )

    temperature = st.slider("Cognitive Drift (Temperature):", 0.0, 1.0, 0.6, 0.05,
                            help="Lower values yield highly structured academic plans. Higher values increase creative empathy.")

    st.divider()
    if st.button("Purge Session Memory 🧹", use_container_width=True, type="secondary"):
        st.session_state.messages = []
        st.rerun()

# Initialize Chat Memory
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": f"Neural handshake successful. I am SYNAPSE. I have mapped your cognitive footprint, {pseudo}. What complex academic concept or revision block are we conquering today?"}]

# Render Chat History
for msg in st.session_state.messages:
    avatar = "🌌" if msg["role"] == "assistant" else "👤"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# User Input & Execution
if prompt := st.chat_input(f"Enter your academic roadblock, {pseudo}..."):

    if not gemini_api_key:
        st.error("⚠️ SYNAPSE offline. Please input your Gemini API Key or configure `.streamlit/secrets.toml`.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # LLM Stream Execution
    with st.chat_message("assistant", avatar="🌌"):
        message_placeholder = st.empty()
        full_response = ""

        # Constructing the Context Window
        formatted_messages = [SystemMessage(content=SYSTEM_PROMPT)]
        for m in st.session_state.messages:
            if m["role"] == "user":
                formatted_messages.append(HumanMessage(content=m["content"]))
            elif m["role"] == "assistant":
                formatted_messages.append(AIMessage(content=m["content"]))

        try:
            llm = ChatGoogleGenerativeAI(
                model=selected_model,
                google_api_key=gemini_api_key,
                temperature=temperature,
                convert_system_message_to_human=True
            )

            # Real-time token streaming
            for chunk in llm.stream(formatted_messages):
                full_response += chunk.content
                message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"❌ Core processing failure. Link to **{selected_model}** severed.")
            st.caption(f"Traceback: {str(e)}")