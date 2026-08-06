import streamlit as st
import time
import re
import uuid
from typing import Annotated, TypedDict

def extract_text(content) -> str:
    """Extrait de manière sécurisée uniquement le texte affichable d'un message LLM,
    en filtrant les blocs internes ou structures complexes."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict) and block.get("type", "text") == "text":
                parts.append(block.get("text", ""))
        return "".join(parts)
    return str(content) if content else ""

# ==============================================================================
# 0. HARDENED DEPENDENCY INJECTION & SAFETY CHECKS
# ==============================================================================
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_core.messages import HumanMessage, AIMessage, trim_messages
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
except ImportError:
    st.error("⚠️ CRITICAL FAULT: Missing core dependencies. Execute: `pip install langchain langchain-google-genai google-generativeai`")
    st.stop()

try:
    from langgraph.graph import StateGraph, START, END
    from langgraph.graph.message import add_messages
    from langgraph.checkpoint.memory import MemorySaver
except ImportError:
    st.error("⚠️ CRITICAL FAULT: Missing LangGraph. Execute: `pip install langgraph`")
    st.stop()

try:
    from google.api_core import exceptions as google_exceptions
    HAS_GOOGLE_EXCEPTIONS = True
except ImportError:
    HAS_GOOGLE_EXCEPTIONS = False

st.set_page_config(page_title="Chronos // Multiverse Engine", page_icon="⏳", layout="wide")


# ==============================================================================
# 1. LANGGRAPH STATE MACHINE & WORKFLOW ARCHITECTURE
# ==============================================================================
class MultiverseState(TypedDict):
    messages: Annotated[list, add_messages]
    pseudo: str
    academic_tier: str
    institutional_framework: str
    geopolitical_region: str


def build_multiverse_prompt(state: MultiverseState) -> str:
    return f"""
[ROLE]
You are CHRONOS: an advanced Multiverse Simulation Core and Strategic Trajectory Engine. You model complex alternative educational, scientific, and geopolitical timelines with extreme precision, vivid realism, and intellectual depth.

[CONTEXT]
- Operator: {state.get('pseudo', 'Operator')}
- Academic Tier: {state.get('academic_tier', 'High School')}
- Institutional Framework: {state.get('institutional_framework', 'Public System')}
- Geopolitical Region: {state.get('geopolitical_region', 'Global')}

[OBJECTIVE]
React to the operator's choices within the simulated timeline. Challenge their assumptions, calculate consequences of their decisions, introduce realistic systemic hurdles, and keep the narrative immersive and highly structured using Markdown. Never break character.
"""


def multiverse_node(state: MultiverseState, config) -> dict:
    cfg = (config or {}).get("configurable", {})
    api_key = cfg.get("api_key", "")
    primary_model = cfg.get("model", "gemini-2.5-flash")
    temp = cfg.get("temperature", 0.7)
    timeout = cfg.get("timeout", 45)

    system_prompt = build_multiverse_prompt(state)
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder("history"),
    ])

    fallback_chain = [primary_model, "gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-3.5-flash"]
    models_to_try = []
    for m in fallback_chain:
        if m not in models_to_try:
            models_to_try.append(m)

    last_exception = None
    for model_name in models_to_try:
        try:
            llm = ChatGoogleGenerativeAI(
                model=model_name,
                google_api_key=api_key,
                temperature=temp,
                timeout=timeout,
                max_retries=1,
            )
            chain = prompt_template | llm
            trimmed_hist = trim_messages(
                state.get("messages", []), 
                strategy="last", 
                token_counter=len, 
                max_tokens=24, 
                start_on="human"
            )
            response = chain.invoke({"history": trimmed_hist})
            return {"messages": [response]}
        except Exception as e:
            last_exception = e
            continue

    raise last_exception if last_exception else RuntimeError("Multiverse inference failed across all fallback models.")


@st.cache_resource
def get_multiverse_app():
    graph = StateGraph(MultiverseState)
    graph.add_node("multiverse_node", multiverse_node)
    graph.add_edge(START, "multiverse_node")
    graph.add_edge("multiverse_node", END)
    return graph.compile(checkpointer=MemorySaver())


# ==============================================================================
# 2. STATE SANITIZATION & SESSION INITIALIZATION
# ==============================================================================
user_profile = st.session_state.get("user_profile", {}) or {}
pseudo_raw = user_profile.get("pseudo", "Operator")
pseudo = re.sub(r"[^\w\s\-']", "", str(pseudo_raw)).strip()[:60] or "Operator"

if "multiverse_thread_id" not in st.session_state:
    st.session_state.multiverse_thread_id = str(uuid.uuid4())

multiverse_app = get_multiverse_app()


# ==============================================================================
# 3. USER INTERFACE & SIDEBAR STYLING
# ==============================================================================
st.markdown("""
<style>
    .chat-header {
        background: linear-gradient(90deg, #38BDF8 0%, #818CF8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.3rem;
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

st.markdown("<h1 class='chat-header'>CHRONOS // Multiverse Trajectory Engine</h1>", unsafe_allow_html=True)
st.markdown(f"""
<div class='metric-pill'>👤 Operator: <b>{pseudo}</b></div>
<div class='metric-pill'>🌌 Engine: <b>Multiverse Simulation</b></div>
""", unsafe_allow_html=True)
st.divider()

with st.sidebar:
    st.markdown("### 🎛️ Engine Matrix (Gemini API)")
    
    if "gemini_api_key" not in st.session_state:
        st.session_state.gemini_api_key = st.secrets.get("GEMINI_API_KEY", "")

    st.session_state.gemini_api_key = st.text_input(
        "Gemini Authentication Key:",
        value=st.session_state.get("gemini_api_key", ""),
        type="password",
        help="Shared across Lumen modules. Never logged or exposed."
    ).strip()

    selected_model = st.selectbox(
        "Inference Model Topology:",
        options=["gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-3.5-flash"],
        index=0
    )

    temperature = st.slider("Simulation Creativity (Temperature):", 0.0, 1.0, 0.7, 0.05)
    request_timeout = st.slider("Request Timeout (s)", 10, 120, 45, 5)

    st.divider()
    if st.button("Purge Timeline Memory 🧹", use_container_width=True, type="secondary"):
        st.session_state.multiverse_thread_id = str(uuid.uuid4())
        st.rerun()

gemini_api_key = st.session_state.get("gemini_api_key", "")


# ==============================================================================
# 4. ENVIRONMENTAL PARAMETERS & CONFIG BUILDER
# ==============================================================================
st.markdown("### 🎛️ Configure Environmental Parameters")
col1, col2, col3 = st.columns(3)

with col1:
    academic_tier = st.selectbox("Academic Tier", ["Middle School", "High School", "University", "Post-Doc"])
with col2:
    institutional_framework = st.selectbox("Institutional Framework", ["Public System", "Private Elite", "Alternative / Homeschool", "Autonomous Lab"])
with col3:
    geopolitical_region = st.selectbox("Geopolitical Region", ["Africa", "Europe", "North America", "Asia", "Global South"])


def build_config():
    return {
        "configurable": {
            "thread_id": st.session_state.get("multiverse_thread_id", str(uuid.uuid4())),
            "api_key": gemini_api_key,
            "model": selected_model,
            "temperature": temperature,
            "timeout": request_timeout,
        }
    }


def get_checkpointed_messages():
    try:
        snapshot = multiverse_app.get_state(build_config())
        if not snapshot or not snapshot.values:
            return []
        return snapshot.values.get("messages", [])
    except Exception:
        return []


if st.button("🚀 EXECUTE TIMELINE SIMULATION", type="primary", use_container_width=True):
    st.session_state.multiverse_thread_id = str(uuid.uuid4())
    
    initial_seed = (
        f"**[TIMELINE INITIALIZED]**\n\n"
        f"Parameters locked:\n"
        f"- Tier: **{academic_tier}**\n"
        f"- Framework: **{institutional_framework}**\n"
        f"- Region: **{geopolitical_region}**\n\n"
        f"Operator {pseudo}, the multiverse divergence point is active. "
        f"Describe your initial strategic decision or state your first move to branch the timeline."
    )
    
    cfg = build_config()
    try:
        multiverse_app.update_state(cfg, {"messages": [AIMessage(content=initial_seed)]})
    except Exception:
        pass
    st.rerun()

st.divider()


# ==============================================================================
# 5. RENDER HISTORY & STREAMING EXECUTION ENGINE
# ==============================================================================
for m in get_checkpointed_messages():
    if isinstance(m, HumanMessage):
        with st.chat_message("user", avatar="👤"):
            st.markdown(extract_text(m.content))
    elif isinstance(m, AIMessage):
        with st.chat_message("assistant", avatar="⏳"):
            st.markdown(extract_text(m.content))

if prompt := st.chat_input("Interact with the simulation timeline..."):
    if not gemini_api_key or len(gemini_api_key) < 20:
        st.error("⚠️ CHRONOS offline. Please input a valid Gemini API Key in the sidebar.")
        st.stop()

    prompt = prompt.strip()[:4000]

    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="⏳"):
        message_placeholder = st.empty()

        input_state = {
            "messages": [HumanMessage(content=prompt)],
            "pseudo": pseudo,
            "academic_tier": academic_tier,
            "institutional_framework": institutional_framework,
            "geopolitical_region": geopolitical_region,
        }

        full_response = ""
        try:
            for msg_chunk, metadata in multiverse_app.stream(
                input_state, build_config(), stream_mode="messages"
            ):
                if metadata and metadata.get("langgraph_node") == "multiverse_node":
                    full_response += extract_text(getattr(msg_chunk, "content", ""))
                    message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"❌ Simulation Error: {str(e)}")