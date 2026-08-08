import streamlit as st
import re
from core.utils import is_plausible_gemini_key, extract_json_block

# ==============================================================================
# 0. HARDENED DEPENDENCY INJECTION
# ==============================================================================
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_core.messages import HumanMessage
except ImportError:
    st.error("⚠️ CRITICAL FAULT: Missing core dependencies. Execute: `pip install langchain langchain-google-genai google-generativeai`")
    st.stop()

try:
    from google.api_core import exceptions as google_exceptions
    HAS_GOOGLE_EXCEPTIONS = True
except ImportError:
    HAS_GOOGLE_EXCEPTIONS = False


# ==============================================================================
# 1. ACCÈS CONDITIONNÉ AU SCAN COGNITIF (même garde-fou que 03_Mr.Brown.py)
# ==============================================================================
if not st.session_state.get("flags", {}).get("scan_completed"):
    st.error("🛑 ACCESS DENIED: Neural baseline not established. Complete the diagnostic scan first.")
    if st.button("🚀 Initiate Assessment", type="primary", use_container_width=True):
        st.switch_page("pages/01_Assessment.py")
    st.stop()

user_profile = st.session_state.get("user_profile", {}) or {}
pseudo_raw = user_profile.get("pseudo", "Operator")
pseudo = re.sub(r"[^\w\s\-']", "", str(pseudo_raw)).strip()[:60] or "Operator"

core_vectors = st.session_state.get("core_vectors", {}) or {}


# ==============================================================================
# 2. STYLE
# ==============================================================================
st.markdown("""
<style>
    .roadmap-header {
        background: linear-gradient(90deg, #06B6D4 0%, #8B5CF6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.3rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="roadmap-header">📅 The Neural Roadmap</p>', unsafe_allow_html=True)
st.write(f"Planning stratégique sur 12 jours généré dynamiquement pour **{pseudo}** selon ses forces et faiblesses cognitives.")
st.divider()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Information Bandwidth", f"{int(core_vectors.get('information_bandwidth', 0))} pts")
col2.metric("Execution Rigor", f"{int(core_vectors.get('execution_rigor', 0))} pts")
col3.metric("Chaos Tolerance", f"{int(core_vectors.get('chaos_tolerance', 0))} pts")
col4.metric("Cognitive Endurance", f"{int(core_vectors.get('cognitive_endurance', 0))} pts")
st.divider()


# ==============================================================================
# 3. SIDEBAR — CLÉ API & MODÈLE
# ==============================================================================
with st.sidebar:
    st.markdown("### 🎛️ Engine Control Matrix")
    st.session_state.gemini_api_key = st.text_input(
        "Gemini API Key:",
        value=st.session_state.get("gemini_api_key", ""),
        type="password",
        placeholder="AIzaSy...",
        help="Partagée entre tous les modules Lumen pour cette session."
    ).strip()

    selected_model = st.selectbox(
        "Inference Model:",
        options=["gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-3.5-flash"],
        index=0
    )
    request_timeout = st.slider("Request Timeout (s)", 10, 120, 45, 5)

gemini_api_key = st.session_state.get("gemini_api_key", "")


# ==============================================================================
# 4. GÉNÉRATION DU PLANNING (fallback de modèles, même logique que les autres pages)
# ==============================================================================
def generate_roadmap(pseudo: str, vectors: dict, api_key: str, model: str, timeout: int):
    prompt = f"""En tant qu'IA stratégique de Lumen, crée un planning d'apprentissage et d'exécution optimisé sur exactement 12 jours pour un utilisateur nommé {pseudo}.

Voici ses scores cognitifs (0 à 100) :
- Information Bandwidth: {vectors.get('information_bandwidth', 0)}
- Execution Rigor: {vectors.get('execution_rigor', 0)}
- Chaos Tolerance: {vectors.get('chaos_tolerance', 0)}
- Cognitive Endurance: {vectors.get('cognitive_endurance', 0)}

Adapte le rythme et le style des directives à ces scores : plus un score est bas sur un axe, plus le planning doit compenser explicitement sur cet axe.

Réponds STRICTEMENT en JSON valide, sans aucun texte avant ou après, au format suivant :
{{
  "days": [
    {{"day": 1, "title": "titre court du jour", "directives": ["directive concrète 1", "directive concrète 2", "directive concrète 3"]}}
  ]
}}
Le tableau "days" doit contenir exactement 12 éléments, un par jour."""

    fallback_chain = [model, "gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-flash-latest"]
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
                temperature=0.6,
                timeout=timeout,
                max_retries=1,
            )
            response = llm.invoke([HumanMessage(content=prompt)])
            return response.content, None
        except Exception as e:
            last_exception = e
            continue

    return None, last_exception


if st.button("Générer mon Planning sur 12 Jours ⚡", type="primary", use_container_width=True):
    if not is_plausible_gemini_key(gemini_api_key):
        st.error("⚠️ Renseigne une clé API Gemini valide dans la barre latérale avant de continuer.")
    else:
        with st.spinner("Synthèse des vecteurs cognitifs et construction du planning..."):
            raw_response, error = generate_roadmap(pseudo, core_vectors, gemini_api_key, selected_model, request_timeout)

        if error is not None:
            if HAS_GOOGLE_EXCEPTIONS and isinstance(error, google_exceptions.PermissionDenied):
                st.error("❌ Clé API rejetée. Vérifie qu'elle est correcte et active.")
            elif HAS_GOOGLE_EXCEPTIONS and isinstance(error, google_exceptions.ResourceExhausted):
                st.error("❌ Quota Gemini dépassé. Réessaie dans quelques instants.")
            else:
                st.error(f"❌ La génération a échoué sur tous les modèles disponibles : {error}")
        else:
            roadmap_data = extract_json_block(raw_response)
            if roadmap_data and isinstance(roadmap_data, dict) and roadmap_data.get("days"):
                st.session_state["roadmap_data"] = roadmap_data
                st.session_state["roadmap_raw"] = None
                st.success("Planning généré avec succès !")
            else:
                st.session_state["roadmap_data"] = None
                st.session_state["roadmap_raw"] = raw_response
                st.warning("Le planning a été généré mais le format JSON attendu n'a pas pu être analysé — affichage brut ci-dessous.")


# ==============================================================================
# 5. AFFICHAGE DU PLANNING
# ==============================================================================
roadmap_data = st.session_state.get("roadmap_data")

if roadmap_data:
    st.divider()
    st.subheader("🗺️ Ton planning sur 12 jours")

    for day in roadmap_data.get("days", []):
        day_num = day.get("day", "?")
        title = day.get("title", "")
        with st.expander(f"Jour {day_num} — {title}", expanded=(day_num == 1)):
            for directive in day.get("directives", []):
                st.markdown(f"- {directive}")

elif st.session_state.get("roadmap_raw"):
    st.divider()
    st.subheader("🗺️ Résultat brut (non structuré)")
    st.markdown(st.session_state["roadmap_raw"])