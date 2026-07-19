import streamlit as st

# ==========================================
# RULE 1 : LA CONFIGURATION ABSOLUE (Paranoïa #1)
# ==========================================
# 'set_page_config' DOIT être la toute première commande Streamlit exécutée.
# Si elle est placée après st.Page ou pg.run(), l'application crash instantanément.
st.set_page_config(page_title="LUMEN", page_icon="💡", layout="wide")


# ==========================================
# RULE 2 : ISOLATION DE L'ACCUEIL (Paranoïa #2)
# ==========================================
# Dans une architecture 'st.navigation', tout code écrit en dehors d'une fonction 
# s'exécute et S'AFFICHE sur TOUTES les pages. 
# Pour éviter que ton titre et ton bouton "Enter the Assessment" polluent le bas 
# de tes pages de diagnostics ou de chatbot, on enferme l'accueil dans une fonction.
def show_home_page():
    st.title("LUMEN: Cognitive Profiler 💡")
    st.write("Welcome to the next generation of cognitive mapping.")
    
    # Paranoïa #3 : Utilisation de l'objet page au lieu d'une chaîne de caractères (string)
    # On ne passe pas la chaîne "Assessment", on passe directement la variable 'assessment_page'.
    if st.button("Enter the Assessment", type="primary"):
        st.switch_page(assessment_page)


# ==========================================
# RULE 3 : DÉCLARATION DU ROUTAGE LOGIQUE
# ==========================================
# On crée nos objets pages. 'home_page' utilise notre fonction ci-dessus.
home_page = st.Page(show_home_page, title="Welcome", icon="🏠", default=True)
assessment_page = st.Page("pages/01_Assessment.py", title="Évaluation", icon="📊")
advices_page = st.Page("pages/Advices.py", title="Conseils", icon="💡")
chatbot_page = st.Page("pages/Chatbot.py", title="Assistant LUMEN", icon="🤖")


# ==========================================
# RULE 4 : SÉCURISATION ET EXÉCUTION
# ==========================================
# La topologie inclut désormais la page d'accueil de manière propre.
pg = st.navigation([home_page, assessment_page, advices_page, chatbot_page])
pg.run()