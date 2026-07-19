import streamlit as st
from data.question import ALL_QUESTIONS

# ==========================================
# PARANOÏA #1 : SUPPRESSION DE SET_PAGE_CONFIG
# ==========================================
# ALERTE CRASH : Comme 'lumen_app.py' gère désormais la navigation avec st.navigation,
# appeler st.set_page_config() une seconde fois ici provoquerait une StreamlitAPIException immediate.
# La configuration globale est déléguée en amont au point d'entrée de l'application.


# ==========================================
# PARANOÏA #2 : SÉCURISATION ET CLAMPING DU SESSION STATE
# ==========================================
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {"pseudo": "", "gender": ""}

total_q = len(ALL_QUESTIONS)

# Sécurité anti-corruption : Si 'current_q' est altéré par un rechargement sauvage,
# on force le type Int et on restreint l'index entre 0 et le maximum de questions.
if not isinstance(st.session_state.current_q, int):
    st.session_state.current_q = 0
st.session_state.current_q = max(0, min(st.session_state.current_q, total_q))


# ==========================================
# PHASE 1 : L'ONBOARDING SÉCURISÉ (Nettoyage des entrées)
# ==========================================
if not st.session_state.user_profile.get("pseudo"):
    st.title("Initialize Your Core 🧠")
    st.markdown("Before we map your cognitive architecture, identify yourself.")
    
    with st.form("onboarding_form", clear_on_submit=False):
        # .strip() élimine les espaces vides accidentels qui pourraient fausser les validations
        pseudo = st.text_input("Enter your Alias (max 20 chars):", max_chars=20).strip()
        gender = st.selectbox("Entity Classification:", ["", "Male", "Female", "Alien 👽"])
        
        submit_profile = st.form_submit_button("Start Mapping")
        
        if submit_profile:
            if pseudo and gender:
                st.session_state.user_profile["pseudo"] = pseudo
                st.session_state.user_profile["gender"] = gender
                st.rerun() 
            else:
                st.error("⚠️ All fields are required to proceed.")
    st.stop()


# ==========================================
# PHASE 2 : VÉRIFICATION ET ROUTAGE DE FIN DE TEST
# ==========================================
current_index = st.session_state.current_q

if current_index >= total_q:
    st.balloons()
    st.title("Scan Complete 🧬")
    st.success(f"Thank you, {st.session_state.user_profile['pseudo']}. Your cognitive data has been processed.")
    
    if st.button("Reveal My Cognitive Signature", type="primary"):
        # PARANOÏA #3 : Alignement strict sur la casse du fichier physique pour Windows
        st.switch_page("pages/Advices.py") 
    st.stop()


# ==========================================
# PHASE 3 : COMPOSANTS DE PROGRESSION GRAPHISME
# ==========================================
# Sécurité absolue : Si la base de données de questions est vide, on coupe l'exécution
if total_q == 0:
    st.error("Critical Error: Cognitive query source truth 'ALL_QUESTIONS' is empty.")
    st.stop()

progress_percent = current_index / total_q
time_left_minutes = max(1, ((total_q - current_index) * 15) // 60)

if progress_percent == 0:
    motivation = "Initiating neural scan..."
elif progress_percent < 0.5:
    motivation = "Analyzing behavioral patterns..."
elif progress_percent < 0.9:
    motivation = "Halfway there! A clear structure is emerging..."
else:
    motivation = "Almost done. Finalizing data intake..."

st.caption(f"⏳ Estimated time remaining: ~{time_left_minutes} minute(s)")
st.progress(progress_percent, text=motivation)
st.divider()


# ==========================================
# PHASE 4 : RENDU DE LA QUESTION ET SÉCURISATION DU FORMULAIRE
# ==========================================
q_data = ALL_QUESTIONS[current_index]

st.caption(f"MODULE {current_index + 1}/{total_q} | {q_data['section'].upper()}")
st.markdown(f"## {q_data['question']}")

# Utilisation d'une clé dynamique pour le formulaire liée à l'index de la question
with st.form(key=f"q_form_{current_index}"):
    choice = st.radio(
        "Select your instinctive response:",
        options=list(q_data["options"].keys()),
        format_func=lambda k: q_data["options"][k]["text"],
        index=None,
        # PARANOÏA #4 : Assigner un identifiant unique strict au widget radio par index.
        # Cela évite que Streamlit conserve en cache la sélection de la question précédente.
        key=f"radio_widget_{current_index}"
    )
    
    next_button = st.form_submit_button("Confirm & Advance ⚡")
    
    if next_button:
        if choice is None:
            st.error("Please select an option to continue.")
        else:
            # Enregistrement des données de réponse
            st.session_state.answers[q_data["id"]] = choice
            # Incrémentation de l'index
            st.session_state.current_q += 1
            st.rerun()