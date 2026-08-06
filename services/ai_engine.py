# ==============================================================================
# SERVICES/AI_ENGINE.PY : MOTEUR IA & PERSONA DE MR. BROWN
# ==============================================================================
import os
from typing import List, Dict, Any
# Note: Adapte l'import selon la librairie que tu utilises (google-genai ou langchain)
from google import genai
from google.genai import types

# ------------------------------------------------------------------------------
# PROMPT SYSTÈME DE MR. BROWN (MENTOR PRINCIPAL)
# ------------------------------------------------------------------------------
MR_BROWN_SYSTEM_PROMPT = """
You are Mr. Brown, an elite, uncompromising, yet deeply invested intellectual mentor and strategist. 
Your user is an exceptionally independent, self-directed young scholar operating outside traditional academic constraints, specializing in advanced mathematics, abstract reasoning, and software engineering (Python, algorithms, data structures), while maintaining a healthy disdain for rigid, bureaucratic schooling and superficial learning.

CORE BEHAVIORAL GUIDELINES:
1. **Intellectual Rigor over Comfort:** Never hand out cheap validation or surface-level summaries. Demand deep, rigorous first-principles thinking. Treat the user like an equal peer in a high-level seminar.
2. **Abstract & Algebraic Focus:** Favor abstract explanations, mathematical structures, logical proofs, and systematic problem-solving over rote memorization or mundane descriptions. 
3. **Tone:** Sharp, articulate, pragmatic, slightly cynical about standard institutional paths, but fiercely supportive of intellectual autonomy, mastery, and precision. Speak with quiet authority.
4. **Contextual Adaptation:** Seamlessly integrate the user's cognitive profile vectors (such as information bandwidth, execution rigor, chaos tolerance, and cognitive endurance) when calibrating the complexity of your answers. Push them precisely where their metrics indicate room for growth.
5. **No Fluff:** Eliminate generic AI filler phrases (e.g., "Sure, I can help with that!", "As an AI..."). Start straight with substance.
"""


def get_gemini_client() -> genai.Client:
    """Initialise et retourne le client officiel Google GenAI de manière sécurisée."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("❌ Erreur critique : La clé API GEMINI_API_KEY est introuvable dans l'environnement.")
    return genai.Client(api_key=api_key)


def generate_mr_brown_response(
    chat_history: List[Dict[str, str]], 
    user_input: str,
    user_cognitive_context: Dict[str, Any] = None
) -> str:
    """
    Gère l'interaction conversationnelle avec le persona de Mr. Brown.
    Transforme l'historique Streamlit au format natif Gemini et injecte le contexte cognitif.
    """
    client = get_gemini_client()
    
    # Construction dynamique du contexte système enrichi
    system_instruction = MR_BROWN_SYSTEM_PROMPT
    if user_cognitive_context:
        system_instruction += f"\n\nCURRENT USER COGNITIVE PROFILE METRICS:\n{user_cognitive_context}"

    # Formatage de l'historique pour l'API Gemini
    formatted_contents = []
    for msg in chat_history:
        role = "user" if msg["role"] == "user" else "model"
        formatted_contents.append(
            types.Content(
                role=role,
                parts=[types.Part.from_text(text=msg["content"])]
            )
        )
    
    # Ajout du message courant de l'utilisateur
    formatted_contents.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_input)]
        )
    )

    # Appel au modèle de pointe (ex: gemini-2.5-flash ou pro selon ton setup)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=formatted_contents,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.4,  # Température basse pour privilégier la rigueur logique
            max_output_tokens=2048,
        ),
    )

    return response.text