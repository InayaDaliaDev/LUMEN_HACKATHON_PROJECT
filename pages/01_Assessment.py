import streamlit as st
from data.question import ALL_QUESTIONS

# ==============================================================================
# PHASE 1: QUESTIONNAIRE ENGINE & SESSION INITIALIZATION
# ==============================================================================

# Initialisation des états de session
if "current_q_idx" not in st.session_state:
    st.session_state.current_q_idx = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "flags" not in st.session_state:
    st.session_state.flags = {}

if "user_profile" not in st.session_state:
    st.session_state.user_profile = {"pseudo": "Builder"}

# Boucle du questionnaire (s'exécute tant que toutes les questions ne sont pas traitées)
if st.session_state.current_q_idx < len(ALL_QUESTIONS):
    idx = st.session_state.current_q_idx
    q = ALL_QUESTIONS[idx]

    # En-tête de progression
    progress = idx / len(ALL_QUESTIONS)
    st.progress(progress)
    st.caption(f"Question {idx + 1} sur {len(ALL_QUESTIONS)}")

    # Affichage de la question
    st.subheader(q.get("text", "Question sans titre"))

    # Gestion flexible des options (liste ou dictionnaire)
    options_list = list(q["options"].keys()) if isinstance(q["options"], dict) else q["options"]
    
    selected_option = st.radio(
        "Choisissez l'option qui vous correspond le mieux :",
        options=options_list,
        key=f"radio_q_{idx}"
    )

    # Bouton de validation
    if st.button("Valider et continuer →", type="primary"):
        # Sauvegarde de la réponse
        st.session_state.answers[q["id"]] = selected_option
        
        # Passage à la question suivante
        st.session_state.current_q_idx += 1
        
        # DÉBLOCAGE SÉCURITÉ : Si la dernière question vient d'être complétée
        if st.session_state.current_q_idx >= len(ALL_QUESTIONS):
            st.session_state.flags["scan_completed"] = True
            st.session_state.flags["chatbot_unlocked"] = True
            
        st.rerun()

    # Bloque le chargement du tableau de bord tant que le test n'est pas terminé
    st.stop()


# ==============================================================================
# PARANOIA ENGINE: ACCESS CONTROL & STATE VALIDATION
# ==============================================================================
# Vérification de sécurité si accès direct par URL sans avoir fini le test
if not st.session_state.flags.get("scan_completed"):
    st.error("🛑 SECURITY BREACH: Assessment incomplete or session expired.")
    st.markdown("You must complete the telemetry scan before accessing the Builder Profile.")
    
    if st.button("⬅️ Return to Entry Protocol"):
        st.switch_page("lumen_app.py")
        
    st.stop() 

if not st.session_state.answers:
    st.error("⚠️ DATA CORRUPTION: No answers found in memory. Rebooting required.")
    st.stop()


# ==============================================================================
# PHASE 2: NEURAL DATA AGGREGATION
# ==============================================================================
st.markdown("<p style='color: #8B5CF6; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: -10px;'>Step 02 / Decryption</p>", unsafe_allow_html=True)
pseudo = st.session_state.user_profile.get("pseudo", "Unknown Builder")
st.title(f"🧬 Profile Decrypted: {pseudo}")
st.write("Cross-referencing your choices with the global hackathon database...")

# Initialisation des vecteurs
core_vectors = {
    "information_bandwidth": 0.0,
    "execution_rigor": 0.0,
    "chaos_tolerance": 0.0,
    "cognitive_endurance": 0.0
}

# Calcul des scores
rendered_advices = []
for q in ALL_QUESTIONS:
    qid = q["id"]
    user_choice_key = st.session_state.answers.get(qid)
    
    if user_choice_key and user_choice_key in q["options"]:
        option_data = q["options"][user_choice_key]
        
        if isinstance(option_data, dict):
            for vec_key in core_vectors.keys():
                core_vectors[vec_key] += option_data.get("vectors", {}).get(vec_key, 0.0)
                
            rendered_advices.append({
                "qid": qid,
                "label": option_data.get("label", "Unknown Pattern"),
                "advice": option_data.get("advice", "Keep coding.")
            })

# Sauvegarde des vecteurs aggregés pour injection dans les Chatbots
st.session_state["core_vectors"] = core_vectors


# ==============================================================================
# PHASE 3: DASHBOARD
# ==============================================================================
st.subheader("📊 Cognitive Loadout Matrix")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Information Bandwidth", f"{int(core_vectors['information_bandwidth'])} pts")
col2.metric("Execution Rigor", f"{int(core_vectors['execution_rigor'])} pts")
col3.metric("Chaos Tolerance", f"{int(core_vectors['chaos_tolerance'])} pts")
col4.metric("Cognitive Endurance", f"{int(core_vectors['cognitive_endurance'])} pts")

st.divider()


# ==============================================================================
# PHASE 4: TACTICAL DEPLOYMENT (ADVICES)
# ==============================================================================
st.subheader("💡 Tactical Briefing")
st.markdown("Based on your neural patterns, here is your custom survival guide for your next build/hackathon:")

for item in rendered_advices:
    with st.expander(f"Pattern Detected: {item['label']} (Q-{item['qid'].upper()})"):
        st.info(f"**Directive:** {item['advice']}")

st.write("")
st.write("")
if st.session_state.flags.get("chatbot_unlocked"):
    st.success("🔓 NEW FEATURE UNLOCKED: AI Mentor Access Granted.")
    if st.button("Initiate Chatbot Protocol 🤖", type="primary", use_container_width=True):
        st.switch_page("pages/Chatbot.py")