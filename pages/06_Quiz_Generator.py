import streamlit as st
from core.utils import is_plausible_gemini_key, extract_json_block

# ==============================================================================
# 0. HARDENED DEPENDENCY INJECTION (même pattern que 03_Mr.Brown.py)
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
# 1. STYLE
# ==============================================================================
st.markdown("""
<style>
    .quiz-header {
        background: linear-gradient(90deg, #8B5CF6 0%, #06B6D4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.3rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="quiz-header">🧩 Neural Quiz Generator</p>', unsafe_allow_html=True)
st.write("Glisse un texte ou un document, et Lumen génère un quiz d'évaluation personnalisé basé sur ton contenu.")
st.divider()


# ==============================================================================
# 2. SIDEBAR — CLÉ API & MODÈLE (même convention que les autres pages IA)
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
        index=0,
        help="gemini-2.5-flash offre le meilleur compromis qualité/fiabilité."
    )

    num_questions = st.slider("Nombre de questions", 3, 10, 5, 1)
    request_timeout = st.slider("Request Timeout (s)", 10, 120, 45, 5)

gemini_api_key = st.session_state.get("gemini_api_key", "")


# ==============================================================================
# 3. SAISIE DU CONTENU SOURCE
# ==============================================================================
uploaded_file = st.file_uploader("Dépose un fichier texte (.txt ou .md)", type=["txt", "md"])
raw_text = st.text_area("Ou colle ton contenu directement ici :", height=200)

content = ""
if uploaded_file is not None:
    try:
        content = uploaded_file.read().decode("utf-8", errors="ignore")
    except Exception:
        st.error("Impossible de lire ce fichier. Vérifie qu'il s'agit bien d'un fichier texte valide.")
elif raw_text:
    content = raw_text.strip()

# Garde-fou : un texte trop long gaspille des tokens et augmente le risque de
# timeout. On tronque proprement plutôt que de planter en pleine génération.
MAX_CHARS = 12000
if len(content) > MAX_CHARS:
    st.warning(f"Le contenu dépasse {MAX_CHARS} caractères — seul le début sera utilisé pour générer le quiz.")
    content = content[:MAX_CHARS]


# ==============================================================================
# 4. GÉNÉRATION DU QUIZ (avec fallback de modèles, même logique que les autres pages)
# ==============================================================================
def generate_quiz(source_text: str, api_key: str, model: str, timeout: int, n_questions: int):
    prompt = f"""À partir du texte suivant, génère exactement {n_questions} questions à choix multiples (QCM) qui testent la compréhension du contenu, pas juste la mémorisation de détails superficiels.

Réponds STRICTEMENT en JSON valide, sans aucun texte avant ou après, au format suivant :
{{
  "questions": [
    {{
      "question": "texte de la question",
      "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
      "correct": "A",
      "explanation": "courte explication de la bonne réponse"
    }}
  ]
}}

TEXTE:
{source_text}"""

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
                temperature=0.4,
                timeout=timeout,
                max_retries=1,
            )
            response = llm.invoke([HumanMessage(content=prompt)])
            return response.content, None
        except Exception as e:
            last_exception = e
            continue

    return None, last_exception


if st.button("Générer le Quiz 🚀", type="primary", use_container_width=True):
    if not is_plausible_gemini_key(gemini_api_key):
        st.error("⚠️ Renseigne une clé API Gemini valide dans la barre latérale avant de continuer.")
    elif not content:
        st.warning("Fournis un texte ou un fichier avant de générer le quiz.")
    else:
        with st.spinner("Analyse du contenu et génération des questions en cours..."):
            raw_response, error = generate_quiz(content, gemini_api_key, selected_model, request_timeout, num_questions)

        if error is not None:
            if HAS_GOOGLE_EXCEPTIONS and isinstance(error, google_exceptions.PermissionDenied):
                st.error("❌ Clé API rejetée. Vérifie qu'elle est correcte et active.")
            elif HAS_GOOGLE_EXCEPTIONS and isinstance(error, google_exceptions.ResourceExhausted):
                st.error("❌ Quota Gemini dépassé. Réessaie dans quelques instants.")
            else:
                st.error(f"❌ La génération a échoué sur tous les modèles disponibles : {error}")
        else:
            quiz_data = extract_json_block(raw_response)
            if quiz_data and isinstance(quiz_data, dict) and quiz_data.get("questions"):
                st.session_state["generated_quiz_data"] = quiz_data
                st.session_state["quiz_answers"] = {}
                st.session_state["quiz_graded"] = False
                st.success("Quiz généré avec succès !")
            else:
                # Repli : le JSON n'a pas pu être parsé, on garde quand même le
                # texte brut plutôt que de perdre la génération.
                st.session_state["generated_quiz_data"] = None
                st.session_state["generated_quiz_raw"] = raw_response
                st.warning("Le quiz a été généré mais le format JSON attendu n'a pas pu être analysé — affichage brut ci-dessous.")


# ==============================================================================
# 5. AFFICHAGE INTERACTIF DU QUIZ
# ==============================================================================
quiz_data = st.session_state.get("generated_quiz_data")

if quiz_data:
    st.divider()
    st.subheader("📝 Ton Quiz Personnalisé")

    questions = quiz_data.get("questions", [])
    quiz_answers = st.session_state.setdefault("quiz_answers", {})

    for i, q in enumerate(questions):
        st.markdown(f"**Q{i + 1}. {q.get('question', '')}**")
        options = q.get("options", {})
        option_keys = list(options.keys())

        selected = st.radio(
            f"question_{i}",
            options=option_keys,
            format_func=lambda k, opts=options: f"{k}) {opts.get(k, '')}",
            index=None,
            key=f"quiz_radio_{i}",
            label_visibility="collapsed"
        )
        quiz_answers[i] = selected
        st.write("")

    if st.button("Corriger ✅", use_container_width=True):
        st.session_state["quiz_graded"] = True

    if st.session_state.get("quiz_graded"):
        score = 0
        for i, q in enumerate(questions):
            correct = q.get("correct")
            user_answer = quiz_answers.get(i)
            if user_answer == correct:
                score += 1
                st.success(f"Q{i + 1} : Correct ✅ — {q.get('explanation', '')}")
            else:
                st.error(f"Q{i + 1} : Incorrect ❌ — Bonne réponse : {correct}) {q.get('options', {}).get(correct, '')}. {q.get('explanation', '')}")

        st.metric("Score final", f"{score} / {len(questions)}")

elif st.session_state.get("generated_quiz_raw"):
    st.divider()
    st.subheader("📝 Résultat brut (non structuré)")
    st.markdown(st.session_state["generated_quiz_raw"])