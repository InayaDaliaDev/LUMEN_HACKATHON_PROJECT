import os
import streamlit as st
import google.generativeai as genai

# Récupération automatique depuis secrets.toml
try:
    API_KEY = st.secrets["GEMINI_API_KEY"] # Adapte le nom de la clé selon ton secrets.toml
except:
    API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("⚠️ Clé API introuvable dans secrets.toml ou l'environnement !")
else:
    genai.configure(api_key=API_KEY)
    print("✅ Clé configurée avec succès ! Lancement du test...\n")
    
    # Le reste de ton code pour lister les modèles...
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"👉 Nom exact : {m.name}")