# ==============================================================================
# CORE/SCORING.PY : MOTEUR ALGÉBRIQUE ET DE TRAITEMENT DES RÉSULTATS
# ==============================================================================
from typing import Dict, List, Any
from data.question import ALL_QUESTIONS

# Définition explicite des 4 axes cognitifs de Lumen
COGNITIVE_AXES: List[str] = [
    "information_bandwidth",
    "execution_rigor",
    "chaos_tolerance",
    "cognitive_endurance"
]


def compute_profile_vectors(
    answers: Dict[str, str], 
    questions_db: List[Dict[str, Any]] = ALL_QUESTIONS
) -> Dict[str, float]:
    """
    Calcule le score brut pour chaque axe cognitif en additionnant 
    les poids des réponses sélectionnées par l'utilisateur.
    """
    raw_vectors = {axis: 0.0 for axis in COGNITIVE_AXES}
    
    for question in questions_db:
        question_id = question.get("id")
        selected_option_key = answers.get(question_id)
        options = question.get("options", {})
        
        if selected_option_key and selected_option_key in options:
            option_data = options[selected_option_key]
            if isinstance(option_data, dict):
                weights = option_data.get("vectors", {})
                for axis in COGNITIVE_AXES:
                    try:
                        raw_vectors[axis] += float(weights.get(axis, 0.0))
                    except (TypeError, ValueError):
                        continue
                        
    return raw_vectors


def compute_theoretical_bounds(
    questions_db: List[Dict[str, Any]] = ALL_QUESTIONS
) -> Dict[str, Dict[str, float]]:
    """
    Calcule dynamiquement les bornes inférieures et supérieures théoriques
    (inf et sup) possibles pour chaque axe d'après la base de questions.
    """
    bounds = {axis: {"min": 0.0, "max": 0.0} for axis in COGNITIVE_AXES}
    
    for question in questions_db:
        options = question.get("options", {})
        if not isinstance(options, dict):
            continue
            
        for axis in COGNITIVE_AXES:
            axis_values = [
                float(opt.get("vectors", {}).get(axis, 0.0))
                for opt in options.values()
                if isinstance(opt, dict)
            ]
            if axis_values:
                bounds[axis]["min"] += min(axis_values)
                bounds[axis]["max"] += max(axis_values)
                
    return bounds


def normalize_scores(
    raw_vectors: Dict[str, float], 
    bounds: Dict[str, Dict[str, float]] = None
) -> Dict[str, int]:
    """
    Projette les scores bruts sur une échelle normalisée de 0 à 100%.
    Intègre une sécurité contre la division par zéro.
    """
    if bounds is None:
        bounds = compute_theoretical_bounds()
        
    normalized_vectors = {}
    for axis, raw_value in raw_vectors.items():
        min_bound = bounds.get(axis, {}).get("min", 0.0)
        max_bound = bounds.get(axis, {}).get("max", 0.0)
        
        # Garde-fou mathématique si l'axe a une variance nulle
        if max_bound == min_bound:
            normalized_vectors[axis] = 50
        else:
            scaled_score = ((raw_value - min_bound) / (max_bound - min_bound)) * 100.0
            # On contraint le résultat entier dans l'intervalle [0, 100]
            normalized_vectors[axis] = int(max(0, min(100, round(scaled_score))))
            
    return normalized_vectors


def extract_user_advices(
    answers: Dict[str, str], 
    questions_db: List[Dict[str, Any]] = ALL_QUESTIONS
) -> List[Dict[str, str]]:
    """
    Extrait les profils et recommandations textuelles associés aux choix.
    Permet aux vues Streamlit d'afficher le texte sans logique de filtrage.
    """
    advices_list = []
    for question in questions_db:
        question_id = question.get("id")
        selected_option_key = answers.get(question_id)
        options = question.get("options", {})
        
        if selected_option_key and selected_option_key in options:
            option_data = options[selected_option_key]
            if isinstance(option_data, dict):
                advices_list.append({
                    "question_id": question_id,
                    "label": option_data.get("label", "Profil Non Déterminé"),
                    "advice": option_data.get("advice", "Aucun conseil disponible pour cette sélection.")
                })
                
    return advices_list