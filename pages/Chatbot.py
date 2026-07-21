import streamlit as st
import requests
import json

# ==============================================================================
# 1. INTEGRITY CHECKS & SESSION STATE LOCK
# ==============================================================================
# Vérification que le profil existe et que le questionnaire a été complété
if "answers" not in st.session_state or not st.session_state.answers:
    st.warning("⚠️ Accès restreint : Tu dois d'abord passer le Neural Scan Matrix pour activer le coach AI !")
    if st.button("🚀 Lancer l'évaluation", type="primary", use_container_width=True):
        st.switch_page("pages/01_Assessment.py")
    st.stop()

# Initialisation de la mémoire de discussion
if "messages" not in st.session_state:
    st.session_state.messages = []

# Extraction des données utilisateur
user_profile = st.session_state.get("user_profile", {})
pseudo = user_profile.get("pseudo", "GUEST_OPERATOR")

# Détection de l'archétype dominant basé sur les réponses du questionnaire
from data.question import ALL_QUESTIONS
all_labels = []
for q in ALL_QUESTIONS:
    q_id = q.get('id')
    if q_id in st.session_state.answers:
        choice = st.session_state.answers[q_id]
        if choice in q["options"]:
            all_labels.append(q["options"][choice].get("label", "Unknown"))

dominant_archetype = max(set(all_labels), key=all_labels.count) if all_labels else "ABSTRACT ARCHITECT"


# ==============================================================================
# 2. SYSTEM PROMPT ENGINE (Le cœur "humain" & cynique du Bot)
# ==============================================================================
SYSTEM_PROMPT = f"""
Tu es LUMEN, une IA métacognitive cynique, vive, ultra-lucide mais profondément bienveillante, conçue pour les developpeurs et étudiants en plein hackathon ou sous pression.

CONTEXTE SUR TON INTERLOCUTEUR :
- Pseudonyme : {pseudo}
- Archétype psychométrique dominant : {dominant_archetype}

DIRECTIVES DE COMPORTEMENT :
1. N'agris JAMAIS comme un assistant virtuel poli, générique ou robotique. Pas de "Bonjour ! Comment puis-je vous aider aujourd'hui ?".
2. Sois naturel(le), direct(e), perspicace, parfois légèrement mordant(e) ou ironique, mais toujours dans le but de booster l'utilisateur.
3. Adapte tes conseils à son archétype ({dominant_archetype}) :
   - Si PRESSURE SPRINTER : Rappelle-lui de ne pas faire du code spaghetti à 3h du matin.
   - Si ABSTRACT ARCHITECT : Force-le/la à arrêter de faire des diagrammes et à coder/déployer.
   - Si SYSTEMIC PERFECTIONIST : Rappelle-lui que le "mieux" est l'ennemi du "bien".
   - Si CHAOS ENGINE : Aide-le/la à canaliser ses 50 idées en un seul projet fini.
4. Réponds de manière concise et dynamique. Utilise le tutoiement.
5. Sois capable de raisonnement abstrait profond tout en restant ancré dans le concret.
"""


# ==============================================================================
# 3. INTERFACE DU CHATBOT
# ==============================================================================
st.markdown("<p style='color: #6366F1; font-weight: 600; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: -10px;'>Metacognitive Containment Unit</p>", unsafe_allow_html=True)
st.title("🤖 LUMEN // Coach IA Métacognitif")
st.caption(f"Connecté au spectre cognitif de **{pseudo}** | Archétype détecté : **{dominant_archetype}**")
st.divider()

# Contrôle du modèle Ollama dans la barre latérale
with st.sidebar:
    st.markdown("### ⚙️ Moteur Local (Ollama)")
    ollama_model = st.selectbox(
        "Modèle Ollama :",
        ["llama3", "mistral", "phi3", "qwen2", "gemma2"],
        index=0,
        help="Assure-toi d'avoir exécuté 'ollama run <modele>' dans ton terminal au préalable !"
    )
    
    if st.button("🧹 Effacer la mémoire courte", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Affichage du parcours de conversation (Mémoire visuelle)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Message d'accueil dynamique si l'historique est vide
if not st.session_state.messages:
    initial_greeting = f"Alors **{pseudo}**, on sature sur le code ou on cherche encore à sur-optimiser l'architecture ? Dis-moi ce qui bloque."
    st.session_state.messages.append({"role": "assistant", "content": initial_greeting})
    with st.chat_message("assistant"):
        st.markdown(initial_greeting)


# ==============================================================================
# 4. EXECUTION ENGINE & OLLAMA API CONNECTOR
# ==============================================================================
if user_input := st.chat_input("Exprime ton problème, une question théorique ou une panne d'inspiration..."):
    # Affichage immédiat du message utilisateur
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Préparation du payload avec mémoire complète pour Ollama
    ollama_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for msg in st.session_state.messages:
        ollama_messages.append({"role": msg["role"], "content": msg["content"]})

    # Appel de l'API locale d'Ollama avec streaming
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        try:
            url = "http://localhost:11434/api/chat"
            payload = {
                "model": ollama_model,
                "messages": ollama_messages,
                "stream": True
            }

            response = requests.post(url, json=payload, stream=True, timeout=60)
            response.raise_for_status()

            # Lecture du flux (streaming) pour un rendu fluide
            for line in response.iter_lines():
                if line:
                    chunk = json.loads(line.decode("utf-8"))
                    if "message" in chunk and "content" in chunk["message"]:
                        full_response += chunk["message"]["content"]
                        response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
            # Sauvegarde dans l'historique de session
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except requests.exceptions.ConnectionError:
            error_msg = "⚠️ **Impossible de joindre Ollama !** Vérifie qu'Ollama est bien lancé en arrière-plan (`ollama serve`)."
            response_placeholder.error(error_msg)
        except Exception as e:
            error_msg = f"⚠️ **Erreur lors de la communication avec Ollama :** {str(e)}"
            response_placeholder.error(error_msg)