# ==============================================================================
# CORE/CENTRALSTATE.PY : GESTIONNAIRE D'ÉTAT CENTRALISÉ (INVARIANT DE SESSION)
# ==============================================================================
#
# UPGRADE : ce fichier définissait auparavant un schéma (raw_vectors,
# normalized_vectors, chat_messages, assessment_completed...) que PERSONNE
# n'utilisait — toutes les pages initialisaient leurs propres clés à la main
# (user_profile, answers, current_q_idx, core_vectors, flags...).
# DEFAULT_STATE reflète maintenant le schéma réellement utilisé partout dans
# le projet, ce qui fait de ce module la vraie source de vérité unique.
#
# gemini_api_key a aussi été ajouté ici : il était réinitialisé en double dans
# 03_Mr.Brown.py, 05_What_If.py et 06_TheOldDays.py avec le même bloc
# "if not in session_state / lire st.secrets". Comme init_session_state()
# tourne à chaque navigation (lumen_app.py est le script routeur exécuté
# avant chaque pg.run()), le centraliser ici supprime cette triplication.
from typing import Dict, Any
import streamlit as st

DEFAULT_STATE: Dict[str, Any] = {
    # --- Profil utilisateur (défini sur l'écran d'accueil) ---
    "user_profile": {
        "pseudo": "",
        "age": 25,
        "gender": "Alien 🛸",
    },

    # --- Module Assessment (01_Assessment.py) ---
    "answers": {},                 # Dict[str, str] : {question_id: option_key}
    "current_q_idx": 0,            # Int : index de la question courante

    # --- Vecteurs cognitifs calculés en fin de questionnaire ---
    "core_vectors": {
        "information_bandwidth": 0.0,
        "execution_rigor": 0.0,
        "chaos_tolerance": 0.0,
        "cognitive_endurance": 0.0,
    },

    # --- Drapeaux d'état ---
    "flags": {
        "scan_completed": False,
        "chatbot_unlocked": True,
    },

    # --- Historique de discussion générique (réservé si besoin futur) ---
    "history_messages": [],

    # --- Clé API Gemini, partagée par toutes les pages IA ---
    "gemini_api_key": "",
}


def init_session_state() -> None:
    """
    Initialise l'espace d'état de Streamlit de manière idempotente.
    À appeler une seule fois tout en haut de `lumen_app.py`.
    Les dicts imbriqués sont copiés pour éviter que deux sessions ne
    partagent accidentellement le même objet mutable.
    """
    for key, default_value in DEFAULT_STATE.items():
        if key not in st.session_state:
            if isinstance(default_value, dict):
                st.session_state[key] = default_value.copy()
            else:
                st.session_state[key] = default_value

    # Pré-remplissage de la clé Gemini depuis secrets.toml si elle existe et
    # que l'utilisateur ne l'a pas encore saisie manuellement.
    if not st.session_state.get("gemini_api_key"):
        try:
            if "GEMINI_API_KEY" in st.secrets:
                st.session_state["gemini_api_key"] = st.secrets["GEMINI_API_KEY"]
        except Exception:
            pass


def reset_assessment_state() -> None:
    """
    Réinitialise uniquement le sous-espace lié au test cognitif
    (utile pour un bouton "Refaire le test"), sans toucher au profil
    utilisateur ni à la clé API déjà saisie.
    """
    st.session_state["answers"] = {}
    st.session_state["current_q_idx"] = 0
    st.session_state["core_vectors"] = DEFAULT_STATE["core_vectors"].copy()
    st.session_state["flags"] = {
        "scan_completed": False,
        "chatbot_unlocked": False,
    }


def get_state(key: str, default: Any = None) -> Any:
    """Accesseur sécurisé pour lire une variable d'état."""
    return st.session_state.get(key, default)