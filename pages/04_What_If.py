import streamlit as st
import time
import re
import uuid
from typing import Annotated, TypedDict
# UPGRADE : extract_text() et is_plausible_gemini_key() vivent maintenant dans
# core/utils.py au lieu d'être dupliquées dans chaque page IA.
from core.utils import extract_text, is_plausible_gemini_key

# ==============================================================================
# 0. CONFIGURATION DE LA PAGE
# ==============================================================================
# FIX: st.set_page_config() a été retiré ici — lumen_app.py l'appelle déjà une
# fois avant pg.run(). Un second appel dans une sous-page lève une
# StreamlitAPIException ("set_page_config() can only be called once per app").
# Si tu veux un titre/icône d'onglet différent pour cette page précise, il faut
# le gérer autrement (Streamlit ne permet pas de changer ces valeurs après coup).

KICKOFF_MARKER = "[WHAT_IF_INTERNAL_KICKOFF] Open the divergence point with vivid, uncompromising realism."


# ==============================================================================
# 1. VÉRIFICATION DES DÉPENDANCES CRITIQUES
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


# ==============================================================================
# 2. GESTION DU PROFIL UTILISATEUR & PARAMÈTRES DE SESSION
# ==============================================================================
user_profile = st.session_state.get("user_profile", {}) or {}
traveler_raw = user_profile.get("pseudo", "Traveler")
traveler_name = re.sub(r"[^\w\s\-']", "", str(traveler_raw)).strip()[:60] or "Traveler"

if "whatif_thread_id" not in st.session_state:
    st.session_state.whatif_thread_id = str(uuid.uuid4())

if "whatif_awaiting_opening" not in st.session_state:
    st.session_state.whatif_awaiting_opening = False


# ==============================================================================
# 3. INTERFACE VISUELLE : DESIGN SYSTEM "AND WHAT IF?!"
# ==============================================================================
st.markdown("""
<style>
    .whatif-title {
        background: linear-gradient(90deg, #38BDF8 0%, #818CF8 50%, #C084FC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 2.7rem;
        letter-spacing: -1.2px;
        margin-bottom: 0px;
    }
    .whatif-subtitle {
        color: #94A3B8;
        font-size: 1.05rem;
        margin-bottom: 25px;
    }
    .scenario-box {
        background-color: #121216;
        border: 1px solid #2A2A35;
        padding: 22px;
        border-radius: 14px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    .pill-tag {
        background-color: #1E1E28;
        color: #38BDF8;
        border: 1px solid #334155;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        margin-right: 8px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='whatif-title'>And what if?! // Divergence Engine</h1>", unsafe_allow_html=True)
st.markdown(f"<div class='whatif-subtitle'>Exploring alternate trajectories, lost paths, and systemic shocks with historical and scientific rigor.</div>", unsafe_allow_html=True)
st.markdown(f"<div><span class='pill-tag'>TRAVELER: {traveler_name.upper()}</span></div>", unsafe_allow_html=True)
st.write("")
st.divider()


# ==============================================================================
# 4. BIBLIOTHÈQUE DE SCÉNARIOS CONTREFACTUELS & CONFIGURATION
# ==============================================================================
DEFAULT_SCENARIOS = {
    "Calculus Divergence (Leibniz vs Newton)": "What if Isaac Newton's manuscripts on fluxions were lost in the Great Plague of London in 1665, leaving Gottfried Wilhelm Leibniz as the sole architect and sole public transmitter of calculus across Europe?",
    "The Alexandria Imperative": "What if the Library of Alexandria was successfully evacuated and relocated under royal patronage in 48 BCE, preserving Hellenistic engineering, automated mechanics, and advanced geometry through late antiquity?",
    "Babbage's Victorian Information Age": "What if the British Treasury fully funded Charles Babbage’s Analytical Engine in 1834, allowing the construction of mechanical computing decades before the birth of electronic transistors?",
    "The Silk Road Scientific Synthesis": "What if the Mongol Empire's Pax Mongolica institutionalized a permanent academy of science in Samarkand in the 13th century, fusing Islamic algebra, Chinese printing, and European logic centuries early?",
    "Custom Divergence Point": "Enter your own custom historical or scientific pivot point..."
}

with st.container():
    st.markdown("<div class='scenario-box'>", unsafe_allow_html=True)
    st.markdown("### 🌀 Define the Divergence Point")
    
    selected_preset = st.selectbox(
        "Choose a Preset Scenario or Craft Your Own:",
        list(DEFAULT_SCENARIOS.keys())
    )
    
    if selected_preset == "Custom Divergence Point":
        divergence_premise = st.text_area(
            "Specify your 'What if?!' question in detail:",
            value="What if Nikola Tesla's Wardenclyffe Tower was fully funded in 1901, establishing a global wireless energy grid?",
            height=90
        )
    else:
        divergence_premise = DEFAULT_SCENARIOS[selected_preset]
        st.info(f"**Core Premise:** {divergence_premise}")
        
    st.markdown("</div>", unsafe_allow_html=True)


# ==============================================================================
# 5. SIDEBAR — MATRICE DE CONTRÔLE & CLÉ API
# ==============================================================================
# UPGRADE : gemini_api_key est déjà initialisée par
# core.centralstate.init_session_state() — plus besoin du bloc manuel ici.
with st.sidebar:
    st.markdown("### 🎛️ Engine Control Matrix")
    st.session_state.gemini_api_key = st.text_input(
        "Gemini API Key:",
        value=st.session_state.gemini_api_key,
        type="password",
        placeholder="AIzaSy...",
        help="Securely stored for this session."
    ).strip()

    selected_model = st.selectbox(
        "Inference Model:",
        options=[
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-1.5-flash",
            "gemini-2.0-flash",
            "gemini-flash-latest"
        ],
        index=0
    )
    
    temperature = st.slider("Divergence Creativity (Temperature):", 0.0, 1.0, 0.7, 0.05)
    request_timeout = st.slider("Request Timeout (s)", 10, 120, 45, 5)

    st.divider()
    if st.button("Reset Timeline 🧹", use_container_width=True, type="secondary"):
        st.session_state.whatif_thread_id = str(uuid.uuid4())
        st.session_state.whatif_awaiting_opening = False
        st.rerun()

gemini_api_key = st.session_state.gemini_api_key


# ==============================================================================
# 6. LANGGRAPH STATE MACHINE & NARRATIVE ENGINE
# ==============================================================================
class WhatIfState(TypedDict):
    messages: Annotated[list, add_messages]
    premise: str
    traveler: str
    turn_count: int
    timeline_phase: str


PHASE_DESCRIPTIONS = {
    "genesis": (
        "PHASE — GENESIS OF DIVERGENCES: The divergence point has just triggered. "
        "Describe the immediate aftermath with visceral, sensory, and intellectual realism. "
        "Show how institutions, contemporary minds, and daily life shift in response to this new reality. "
        "Do not offer generic welcomes; drop the traveler right into the shifting timeline."
    ),
    "shock": (
        "PHASE — SYSTEMIC SHOCK & RESISTANCE: React sharply to what the traveler just introduced or asked. "
        "Introduce realistic resistance, unintended consequences, intellectual conflict, or technological bottlenecks "
        "characteristic of this timeline. Make the stakes concrete and intellectually demanding."
    ),
    "ripple": (
        "PHASE — RIPPLE EFFECTS & TRAJECTORY: Trace the cascading effects of recent choices across society, "
        "science, or politics. Keep the simulation immersive, open-ended, and fiercely reactive."
    )
}


def build_system_prompt(state: WhatIfState) -> str:
    phase = state.get("timeline_phase", "genesis")
    return f"""
[ROLE]
You are CHRONOS-X: an elite Counterfactual Simulation Core. You model alternate histories, lost scientific trajectories, and civilizational divergences with extreme intellectual depth, uncompromising realism, and vivid prose. You avoid cliché phrases, corporate AI filler, and superficial summaries. You treat every counterfactual scenario with rigorous logic and historical plausibility.

[TRAVELER]
- Designation: {state.get('traveler', 'Traveler')}

[DIVERGENCE PREMISE]
{state.get('premise', 'An alternate historical path.')}

[CURRENT SIMULATION PHASE]
{PHASE_DESCRIPTIONS.get(phase, PHASE_DESCRIPTIONS['genesis'])}

[RULES]
- Write with sharp, evocative, literary prose.
- Never break character, never mention AI or prompts.
- Challenge the traveler's assumptions and make every decision carry realistic consequences.
"""


def route_timeline_phase(state: WhatIfState) -> dict:
    turns = int(state.get("turn_count", 0))
    if turns == 0:
        phase = "genesis"
    elif turns < 3:
        phase = "shock"
    else:
        phase = "ripple"
    return {"timeline_phase": phase, "turn_count": turns + 1}


def phase_router(state: WhatIfState) -> str:
    return state.get("timeline_phase", "genesis")


def safe_token_counter(msgs) -> int:
    return len(msgs) if isinstance(msgs, list) else 1


def trimmed_history(messages):
    if not messages:
        return []
    return trim_messages(
        messages,
        strategy="last",
        token_counter=safe_token_counter,
        max_tokens=24,
        start_on="human",
    )


def make_simulator_node(phase: str):
    def node(state: WhatIfState, config) -> dict:
        cfg = (config or {}).get("configurable", {})
        api_key = cfg.get("api_key", "")
        model = cfg.get("model", "gemini-2.5-flash")
        timeout = cfg.get("timeout", 45)
        temp = cfg.get("temperature", 0.7)

        active_state = {**state, "timeline_phase": phase}
        system_prompt = build_system_prompt(active_state)

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder("history"),
        ])

        fallback_chain = [
            model,
            "gemini-2.5-flash",
            "gemini-1.5-flash",
            "gemini-2.0-flash",
            "gemini-flash-latest"
        ]
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
                response = chain.invoke({"history": trimmed_history(state.get("messages", []))})
                return {"messages": [response]}
            except Exception as e:
                last_exception = e
                continue

        raise last_exception if last_exception else RuntimeError("All model execution attempts failed.")

    return node


@st.cache_resource
def get_whatif_app():
    graph = StateGraph(WhatIfState)
    graph.add_node("route_timeline_phase", route_timeline_phase)
    graph.add_node("genesis_node", make_simulator_node("genesis"))
    graph.add_node("shock_node", make_simulator_node("shock"))
    graph.add_node("ripple_node", make_simulator_node("ripple"))

    graph.add_edge(START, "route_timeline_phase")
    graph.add_conditional_edges(
        "route_timeline_phase",
        phase_router,
        {
            "genesis": "genesis_node",
            "shock": "shock_node",
            "ripple": "ripple_node",
        },
    )
    graph.add_edge("genesis_node", END)
    graph.add_edge("shock_node", END)
    graph.add_edge("ripple_node", END)

    return graph.compile(checkpointer=MemorySaver())


whatif_app = get_whatif_app()
SIMULATOR_NODES = {"genesis_node", "shock_node", "ripple_node"}


# ==============================================================================
# 7. MOTEUR DE STREAMING ROBUSTE & GESTION DES ERREURS
# ==============================================================================
def stream_turn(input_state: dict, config: dict, placeholder, max_attempts: int = 2):
    last_error_message = None

    for attempt in range(1, max_attempts + 1):
        full_response = ""
        try:
            for msg_chunk, metadata in whatif_app.stream(
                input_state, config, stream_mode="messages"
            ):
                if metadata and metadata.get("langgraph_node") in SIMULATOR_NODES:
                    full_response += extract_text(getattr(msg_chunk, "content", ""))
                    placeholder.markdown(full_response + "▌")
            placeholder.markdown(full_response)
            return full_response, None

        except Exception as e:
            transient = False
            user_msg = None

            if HAS_GOOGLE_EXCEPTIONS:
                if isinstance(e, google_exceptions.PermissionDenied):
                    user_msg = "🔒 Access Denied: Invalid or restricted API key."
                elif isinstance(e, google_exceptions.Unauthenticated):
                    user_msg = "🔒 Authentication Failed: Check your API key."
                elif isinstance(e, google_exceptions.InvalidArgument):
                    user_msg = "⚠️ Invalid Request: Selected model may be unsupported."
                elif isinstance(e, google_exceptions.ResourceExhausted):
                    transient = True
                    user_msg = "⏳ Rate limit reached. Retrying..."
                elif isinstance(e, (google_exceptions.DeadlineExceeded, google_exceptions.ServiceUnavailable)):
                    transient = True
                    user_msg = "🌐 Temporary network disruption. Retrying..."

            if user_msg is None:
                transient = True
                user_msg = f"❌ Simulation Disruption ({type(e).__name__})."

            last_error_message = user_msg

            if transient and attempt < max_attempts:
                time.sleep(1.5 * attempt)
                continue
            else:
                return None, last_error_message

    return None, last_error_message


def build_config():
    return {
        "configurable": {
            "thread_id": st.session_state.whatif_thread_id,
            "api_key": gemini_api_key,
            "model": selected_model,
            "temperature": temperature,
            "timeout": request_timeout,
        }
    }


def get_checkpointed_messages():
    try:
        snapshot = whatif_app.get_state(build_config())
        if not snapshot or not getattr(snapshot, "values", None):
            return []
        return snapshot.values.get("messages", [])
    except Exception:
        return []


# ==============================================================================
# 8. EXÉCUTION DE L'INTERFACE & BOUCLE DE CHAT
# ==============================================================================
col_b2, col_b1, col_b3 = st.columns([1, 2, 1])
with col_b1:
    if st.button("⚡ IGNITE DIVERGENCE TIMELINE", use_container_width=True, type="primary"):
        if not is_plausible_gemini_key(gemini_api_key):
            st.error("⚠️ CRITICAL: A valid Gemini API Key is required to ignite the simulation.")
            st.stop()

        st.session_state.whatif_thread_id = str(uuid.uuid4())
        st.session_state.whatif_awaiting_opening = True
        st.rerun()

current_messages = get_checkpointed_messages()

for m in current_messages:
    if isinstance(m, HumanMessage):
        if extract_text(m.content) == KICKOFF_MARKER:
            continue  # Masque le marqueur technique interne
        with st.chat_message("user", avatar="👤"):
            st.markdown(extract_text(m.content))
    elif isinstance(m, AIMessage):
        with st.chat_message("assistant", avatar="⚡"):
            st.markdown(extract_text(m.content))

if st.session_state.whatif_awaiting_opening and not current_messages:
    with st.chat_message("assistant", avatar="⚡"):
        message_placeholder = st.empty()

        if not is_plausible_gemini_key(gemini_api_key):
            st.error("⚠️ CRITICAL: Gemini API Key missing or malformed.")
        else:
            input_state = {
                "messages": [HumanMessage(content=KICKOFF_MARKER)],
                "premise": divergence_premise,
                "traveler": traveler_name,
            }
            full_resp, err = stream_turn(input_state, build_config(), message_placeholder)
            if err:
                st.error(err)
            else:
                st.session_state.whatif_awaiting_opening = False
                st.rerun()

if prompt := st.chat_input("Intervene in the alternate timeline..."):
    if not is_plausible_gemini_key(gemini_api_key):
        st.error("⚠️ CRITICAL: A valid Gemini API Key is required.")
        st.stop()

    prompt = prompt.strip()[:4000]

    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="⚡"):
        message_placeholder = st.empty()

        input_state = {
            "messages": [HumanMessage(content=prompt)],
            "premise": divergence_premise,
            "traveler": traveler_name,
        }
        full_resp, err = stream_turn(input_state, build_config(), message_placeholder)
        if err:
            st.error(err)
        else:
            st.rerun()