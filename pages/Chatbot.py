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
# 2. COGNITIVE TELEMETRY ENGINE
# ==============================================================================
# We mathematically process the user's test results to feed the LLM's Context.
all_labels = []
vector_totals = {
    "information_bandwidth": 0.0,
    "execution_rigor": 0.0,
    "chaos_tolerance": 0.0,
    "cognitive_endurance": 0.0
}
detailed_choices = []

for q in ALL_QUESTIONS:
    q_id = q.get('id')
    if q_id in answers:
        choice_key = answers[q_id]
        opt = q["options"].get(choice_key, {})
        
        label = opt.get("label", "Unmapped")
        all_labels.append(label)
        
        q_title = q.get('title', f"Query {q_id}")
        opt_text = opt.get('text', choice_key)
        detailed_choices.append(f"- **{q_title}**: {opt_text} (*Signaling {label}*)")
        
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
# 3. THE MASTERPIECE PROMPT ENGINE (HACKATHON WINNER)
# ==============================================================================
# This prompt uses advanced psychometric framing to force the LLM into a hyper-intelligent, 
# deeply empathetic mentor role.

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
- **Primary Strength**: {vector_labels[strongest_key]} ({vector_totals[strongest_key]:.1f})
- **Critical Growth Axis**: {vector_labels[weakest_key]} ({vector_totals[weakest_key]:.1f})

*Operator's Specific Neural Footprint (Recent Decisions):*
{chr(10).join(detailed_choices)}

[EXAMPLES]
User: "I am feeling overwhelmed studying a new language and complex math theorems. I don't know how to memorize everything."
SYNAPSE: "I hear you, {pseudo}. The sheer volume of data is causing a bottleneck in your working memory. But look at your profile: you are a **{dominant_archetype}**. This means your brain doesn't just memorize; it *architects*. 
Let's drop the standard methods. For the math theorems, we are employing **Concept Mapping**: don't memorize the formula, reverse-engineer the proof until the logic feels like a second language. For the new language, abandon phonetic crutches entirely. Focus on the raw visual and structural anatomy of the characters. Your high **{vector_labels[strongest_key]}** allows you to see patterns where others see chaos. You don't need to work harder, {pseudo}. We just need to align your study vectors with your natural cognitive engine. Here is your 3-step protocol for tonight..."

[NOTES]
Always filter your advice through the lens of their `{dominant_archetype}` and their Critical Growth Axis (`{vector_labels[weakest_key]}`). If they ask a generic question, reframe it into a masterclass on personalized metacognition. Maintain your majestic, supportive, and brilliant persona at all costs.
"""


# ==============================================================================
# 4. NEURAL UI INTERFACE & LLM STREAMING (GROQ)
# ==============================================================================
# Custom CSS for a breathtaking, sleek aesthetic
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
<div class='metric-pill'>⚡ Core Advantage: <b>{vector_labels[strongest_key]}</b></div>
""", unsafe_allow_html=True)
st.divider()

# Sidebar: Core Engine Configuration
with st.sidebar:
    st.markdown("### 🎛️ Engine Matrix (Groq API)")
    
    # Auto-fetch from secrets if available
    default_key = st.secrets.get("GROQ_API_KEY", "") if "GROQ_API_KEY" in st.secrets else ""
    groq_api_key = st.text_input("Groq Authentication Key:", value=default_key, type="password")
    
    selected_model = st.selectbox(
        "Language Model Topology:",
        options=["llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "mixtral-8x7b-32768"],
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
    
    if not groq_api_key:
        st.error("⚠️ SYNAPSE offline. Please input your Groq API Key in the Engine Matrix.")
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
            llm = ChatGroq(
                model=selected_model,
                api_key=groq_api_key,
                temperature=temperature,
                streaming=True
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