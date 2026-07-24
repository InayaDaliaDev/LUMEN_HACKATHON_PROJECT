import streamlit as st

# ------------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Lumen - Mind Scan",
    page_icon="🧠",
    layout="wide"
)

# ------------------------------------------------------------------------------
# 2. SESSION STATE INITIALIZATION (Garantie Anti-Crash Global)
# ------------------------------------------------------------------------------
# Profil utilisateur
if "user_profile" not in st.session_state:
    st.session_state.user_profile = {
        "pseudo": "",
        "age": 25,
        "gender": "Alien 🛸"
    }

# Réponses au questionnaire
if "answers" not in st.session_state:
    st.session_state.answers = {}

# Index de la question courante (requis par 01_Assessment.py et Advices.py)
if "current_q_idx" not in st.session_state:
    st.session_state.current_q_idx = 0

# Vecteurs cognitifs (évite les KeyError si accès direct aux pages filles)
if "core_vectors" not in st.session_state:
    st.session_state.core_vectors = {}

# Drapeaux d'état
if "flags" not in st.session_state:
    st.session_state.flags = {
        "scan_completed": False,
        "chatbot_unlocked": True
    }

# Historique de discussion pour Chatbot / TheOldDays
if "history_messages" not in st.session_state:
    st.session_state.history_messages = []

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
assessment_page = st.Page("pages/01_Assessment.py", title="01 // Neural Assessment", icon="🔍")
advices_page = st.Page("pages/Advices.py", title="02 // Strategic Countermeasures", icon="📊")
chatbot_page = st.Page("pages/Chatbot.py", title="03 // Containment AI", icon="💬")
what_if_page = st.Page("pages/What_If.py", title="04 // Simulation Engine", icon="🔮")
old_days_page = st.Page("pages/TheOldDays.py", title="05 // Temporal Logs", icon="⏳")

# Initialisation du menu de navigation
pg = st.navigation([
    home_page, 
    assessment_page, 
    advices_page, 
    chatbot_page, 
    what_if_page, 
    old_days_page
])

pg.run()