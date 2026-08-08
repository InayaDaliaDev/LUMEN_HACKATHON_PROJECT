# ==============================================================================
# CORE/UTILS.PY : FONCTIONS PARTAGÉES ENTRE LES MODULES IA
# ==============================================================================
# FIX: ce fichier doit s'appeler "utils.py" en minuscule — un import
# "from core.utils import ..." sur un fichier nommé "Utils.py" fonctionne sur
# Windows (insensible à la casse) mais casse avec un ModuleNotFoundError sur
# Linux, qui est ce que Streamlit Community Cloud utilise pour héberger l'app.
# extract_text() et is_plausible_gemini_key() étaient copiées-collées dans
# 03_Mr.Brown.py, 04_What_If.py et 05_TheOldDays.py — centralisées ici.
# extract_json_block() est utilisée par 06_Quiz_Generator.py et
# 07_Planning_Generator.py pour parser la sortie JSON de Gemini.


def extract_text(content) -> str:
    """Extrait uniquement le texte affichable d'un message LLM de manière sécurisée."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict) and block.get("type", "text") == "text":
                parts.append(block.get("text", ""))
        return "".join(parts)
    return str(content) if content else ""


def is_plausible_gemini_key(key: str) -> bool:
    """Vérification superficielle (pas cryptographique) qu'une chaîne
    ressemble à une clé API Gemini valide, avant de dépenser un appel réseau."""
    if not key:
        return False
    key = key.strip()
    return len(key) >= 20 and " " not in key


def extract_json_block(text: str):
    """
    Extrait un objet ou une liste JSON depuis une réponse LLM, même si le
    modèle a entouré le JSON de ```json ... ``` ou de texte parasite.
    Retourne None si aucun JSON valide n'a pu être extrait — à toujours
    vérifier côté appelant avant d'utiliser le résultat.
    Utilisé par 06_Quiz_Generator.py et 07_Planning_Generator.py.
    """
    import json
    import re

    if not text:
        return None

    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
    cleaned = re.sub(r"\s*```$", "", cleaned)

    try:
        return json.loads(cleaned)
    except (json.JSONDecodeError, ValueError):
        pass

    # Repli : cherche le premier bloc { ... } ou [ ... ] dans le texte brut.
    for opener, closer in (("{", "}"), ("[", "]")):
        start = cleaned.find(opener)
        end = cleaned.rfind(closer)
        if start != -1 and end != -1 and end > start:
            candidate = cleaned[start:end + 1]
            try:
                return json.loads(candidate)
            except (json.JSONDecodeError, ValueError):
                continue

    return None