import streamlit as st
import time
from data.question import ALL_QUESTIONS

# 1. Configuration de la page
st.set_page_config(page_title="Lumen Assessment", page_icon="🧠", layout="centered")

# 2. Initialisation du "Cerveau" de l'application (Session State)
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {"pseudo": "", "gender": ""}

# 3. PHASE 1 : L'Onboarding (Création du profil)
if not st.session_state.user_profile["pseudo"]:
    st.title("Initialize Your Core 🧠")
    st.markdown("Before we map your cognitive architecture, identify yourself.")
    
    with st.form("onboarding_form"):
        pseudo = st.text_input("Enter your Alias (max 20 chars):", max_chars=20)
        gender = st.selectbox("Entity Classification:", ["", "Male", "Female", "Alien 👽"])
        
        submit_profile = st.form_submit_button("Start Mapping")
        
        if submit_profile:
            if pseudo and gender:
                st.session_state.user_profile["pseudo"] = pseudo
                st.session_state.user_profile["gender"] = gender
                st.rerun() # Recharge la page instantanément
            else:
                st.warning("⚠️ All fields are required to proceed.")
    st.stop() # Empêche le reste du code de s'exécuter tant que le profil n'est pas rempli

# 4. PHASE 2 : L'Assessment (Dynamique et Fluide)
total_q = len(ALL_QUESTIONS)
current_index = st.session_state.current_q

# Vérification : Si le test est terminé, on redirige vers les résultats
if current_index >= total_q:
    st.balloons()
    st.title("Scan Complete 🧬")
    st.success(f"Thank you, {st.session_state.user_profile['pseudo']}. Your cognitive data has been processed.")
    
    if st.button("Reveal My Cognitive Signature"):
        # Cette ligne permet de sauter automatiquement vers ta page Advices
        st.switch_page("pages/Advices.py") 
    st.stop()

# --- Les Mécaniques Psychologiques (Gamification) ---

# Calcul de la progression et du temps
progress_percent = current_index / total_q
# On estime 15 secondes par question
time_left_seconds = (total_q - current_index) * 15 
time_left_minutes = max(1, time_left_seconds // 60) # Affiche toujours au moins 1 min

# Messages dynamiques pour stimuler la dopamine
if progress_percent == 0:
    motivation = "Initiating neural scan..."
elif progress_percent < 0.5:
    motivation = "Analyzing behavioral patterns..."
elif progress_percent >= 0.5 and progress_percent < 0.9:
    motivation = "Halfway there! A clear structure is emerging..."
else:
    motivation = "Almost done. Finalizing data intake..."

# Affichage des indicateurs
st.caption(f"⏳ Estimated time remaining: ~{time_left_minutes} minute(s)")
st.progress(progress_percent, text=motivation)
st.divider()

# --- Affichage de la Question Actuelle ---
q_data = ALL_QUESTIONS[current_index]

st.caption(f"MODULE {current_index + 1}/{total_q} | {q_data['section'].upper()}")
st.markdown(f"## {q_data['question']}")

# Le formulaire pour capturer la réponse proprement
with st.form(key=f"q_form_{current_index}"):
    choice = st.radio(
        "Select your instinctive response:",
        options=list(q_data["options"].keys()),
        format_func=lambda k: q_data["options"][k]["text"],
        index=None # Force l'utilisateur à faire un choix actif (pas de sélection par défaut)
    )
    
    # Bouton d'action
    next_button = st.form_submit_button("Confirm & Advance ⚡")
    
    if next_button:
        if choice is None:
            st.error("Please select an option to continue.")
        else:
            # On sauvegarde la réponse dans le dictionnaire
            st.session_state.answers[q_data["id"]] = choice
            # On passe à la question suivante
            st.session_state.current_q += 1
            st.rerun() # Recharge la page pour afficher la question suivante