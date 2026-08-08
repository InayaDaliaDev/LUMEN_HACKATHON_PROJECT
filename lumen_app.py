import streamlit as st
from core.centralstate import init_session_state  # FIX: était "core.state" (fichier inexistant -> ModuleNotFoundError)
from core.disclaimer import render_lumen_disclaimer

# 1. Initialisation de l'état
init_session_state()

# 2. Affichage du disclaimer tout en haut de la page principale
render_lumen_disclaimer()
# ------------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Lumen - Mind Scan",
    page_icon="🧠",
    layout="wide"
)

# ------------------------------------------------------------------------------
# 2. SESSION STATE INITIALIZATION
# ------------------------------------------------------------------------------
# UPGRADE : ce bloc dupliquait à la main exactement ce que
# core.centralstate.init_session_state() fait déjà (appelé plus haut), mais
# avec un schéma qui pouvait diverger silencieusement de celui-ci au fil du
# temps. init_session_state() est désormais l'unique source de vérité —
# voir core/centralstate.py pour la liste complète des clés initialisées
# (user_profile, answers, current_q_idx, core_vectors, flags,
# history_messages, gemini_api_key).

# ------------------------------------------------------------------------------
# 3. HOME / INTRODUCTION VIEW
# ------------------------------------------------------------------------------
def home_view():
    st.title("👋 Welcome to Lumen")
    st.subheader("We need to know who we're talking to. Set up your profile before diving in.")

    st.markdown("""
    > **Quick heads-up:** Our system adapts its tone, advice, and responses based on your age and all.  
    > Be honest. Or don't. But we *will* notice if something feels off... 👁️
    """)

    st.divider()

    with st.form("user_profile_form"):
        col1, col2 = st.columns(2)

        with col1:
            pseudo = st.text_input(
                "Your Nickname / Alias:",
                value=st.session_state.user_profile.get("pseudo", ""),
                placeholder="e.g. Alex, Operator, CookingMaster"
            )

            age = st.number_input(
                "Your Age:",
                min_value=1,
                max_value=120,
                value=int(st.session_state.user_profile.get("age", 25))
            )

        with col2:
            current_gender = st.session_state.user_profile.get("gender", "Alien 🛸")
            gender_options = ["Female 👩", "Male 👨", "Alien 🛸"]
            gender_idx = gender_options.index(current_gender) if current_gender in gender_options else 2

            gender = st.selectbox(
                "Gender / Identity:",
                options=gender_options,
                index=gender_idx
            )

        submitted = st.form_submit_button("Save Profile & Lock It In 🔒")

        if submitted:
            if not pseudo.strip():
                st.error("Please enter a nickname! We need something to call you.")
            else:
                st.session_state.user_profile["pseudo"] = pseudo.strip()
                st.session_state.user_profile["age"] = age
                st.session_state.user_profile["gender"] = gender
                st.success(f"Profile saved! Welcome, {pseudo}. You can now start the Scan or talk to the ChatBot in the sidebar menu.")

    st.divider()
    if st.session_state.user_profile["pseudo"]:
        st.info(f"👤 **Current Profile:** {st.session_state.user_profile['pseudo']} | **Age:** {st.session_state.user_profile['age']} | **Identity:** {st.session_state.user_profile['gender']}")

# ---------------------------------------------------------
# ROUTING CONFIGURATION (Arborescence)
# ---------------------------------------------------------
# Vue d'accueil liée à la fonction home_view
home_page = st.Page(home_view, title="00 // Entry Protocol", icon="🚨", default=True)

# Pages secondaires (fichiers dans le dossier pages/)
# FIX: chemins remis à jour après ton renommage de fichiers
# (05_What_If→04, 06_TheOldDays→05, 07_Quiz_Generator→06, 08_Planning_Generator→07).
assessment_page = st.Page("pages/01_Assessment.py", title="01 // Neural Assessment", icon="🔍")
advices_page = st.Page("pages/02_Advices.py", title="02 // Strategic Countermeasures", icon="📊")
chatbot_page = st.Page("pages/03_Mr.Brown.py", title="03 // Containment AI", icon="💬")
what_if_page = st.Page("pages/04_What_If.py", title="04 // Simulation Engine", icon="🔮")
old_days_page = st.Page("pages/05_TheOldDays.py", title="05 // Temporal Logs", icon="⏳")
quiz_page = st.Page("pages/06_Quiz_Generator.py", title="06 // Quiz Generator", icon="🧩")
planning_page = st.Page("pages/07_Planning_Generator.py", title="07 // Neural Roadmap", icon="📅")

# Initialisation du menu de navigation
pg = st.navigation([
    home_page,
    assessment_page,
    advices_page,
    chatbot_page,
    what_if_page,
    old_days_page,
    quiz_page,
    planning_page,
])

pg.run()