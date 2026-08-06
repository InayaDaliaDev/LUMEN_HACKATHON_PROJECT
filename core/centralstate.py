# ==============================================================================
# CORE/STATE.PY : GESTIONNAIRE D'ÉTAT CENTRALISÉ (INVARIANT DE SESSION)
# ==============================================================================
from typing import Dict, Any, List
import streamlit as st

# Schéma contractuel de l'état global de Lumen.
# Toute nouvelle variable globale DOIT être déclarée ici avec sa valeur neutre.
DEFAULT_STATE: Dict[str, Any] = {
    # --- Module Assessment (01_Assessment.py) ---
    "answers": {},                 # Dict[str, str] : {question_id: option_key}
    "assessment_completed": False, # Bool : Verrou de validation du questionnaire
    
    # --- Module Scoring & Algèbre (core/scoring.py -> Advices.py) ---
    "raw_vectors": {               # Scores cognitifs bruts
        "information_bandwidth": 0.0,
        "execution_rigor": 0.0,
        "chaos_tolerance": 0.0,
        "cognitive_endurance": 0.0,
    },
    "normalized_vectors": {        # Scores normalisés (0 à 100%) pour le radar
        "information_bandwidth": 0,
        "execution_rigor": 0,
        "chaos_tolerance": 0,
        "cognitive_endurance": 0,
    },
    "advices_list": [],            # List[Dict[str, str]] : Conseils extraits
    
    # --- Module Synapse IA (Chatbot.py) ---
    "chat_messages": [],           # List[Dict[str, str]] : Historique conversationnel
    "synapse_system_prompt": "",   # Prompt contextuel généré après l'assessment
}


def init_session_state() -> None:
    """
    Initialise l'espace d'état de Streamlit de manière idempotente.
    À appeler une seule fois tout en haut de `lumen_app.py`.
    """
    for key, default_value in DEFAULT_STATE.items():
        if key not in st.session_state:
            st.session_state[key] = default_value


def reset_assessment_state() -> None:
    """
    Réinitialise uniquement le sous-espace lié au test cognitif,
    sans détruire l'historique global si l'utilisateur veut refaire le test.
    """
    st.session_state["answers"] = {}
    st.session_state["assessment_completed"] = False
    st.session_state["raw_vectors"] = DEFAULT_STATE["raw_vectors"].copy()
    st.session_state["normalized_vectors"] = DEFAULT_STATE["normalized_vectors"].copy()
    st.session_state["advices_list"] = []
    st.session_state["synapse_system_prompt"] = ""


def get_state(key: str, default: Any = None) -> Any:
    """Accesseur sécurisé pour lire une variable d'état."""
    return st.session_state.get(key, default)