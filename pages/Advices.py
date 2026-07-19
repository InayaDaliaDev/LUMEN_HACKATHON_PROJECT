import streamlit as st
from data.question import ALL_QUESTIONS
from collections import Counter

# ==========================================
# PARANOÏA #1 : DÉLÉGATION DE LA CONFIGURATION
# ==========================================
# ALERTE CRASH : 'st.set_page_config()' a été RETIRÉ. 
# Comme cette page est appelée par 'st.navigation' dans 'lumen_app.py', toute tentative de re-configuration 
# provoquerait l'effondrement instantané de l'application. La configuration globale reste au niveau de la racine.


st.title("🧬 Core Cognitive Architecture Report")
st.markdown("---")


# ==========================================
# PARANOÏA #2 : SÉCURISATION ET CONTRÔLE D'INTEGRITÉ
# ==========================================
# Si un utilisateur tente d'accéder à cette page directement par URL sans faire le test :
if 'answers' not in st.session_state or not st.session_state.answers or 'user_profile' not in st.session_state:
    st.warning("⚠️ Access Denied: No cognitive telemetry data detected in active session state.")
    if st.button("Initialize Assessment Sequence", type="primary"):
        st.switch_page("pages/01_Assessment.py")
    st.stop()

# Extraction sécurisée avec fallbacks pour éviter les erreurs d'attributs manquants
user_profile = st.session_state.get("user_profile", {})
pseudo = user_profile.get("pseudo", "Subject").strip()
classification = user_profile.get("gender", "Undefined")
answers = st.session_state.answers


# ==========================================
# PHASE 1 : PARSING FILTRÉ ET ANALYSE RADICALE
# ==========================================
sections_data = {}
all_labels = []

for q in ALL_QUESTIONS:
    q_id = q.get('id')
    if q_id in answers:
        user_choice = answers[q_id]
        
        # Paranoïa Anti-Corruption : On s'assure que le choix de l'utilisateur correspond 
        # toujours à une option réelle dans la brique de questions d'origine.
        if "options" not in q or user_choice not in q["options"]:
            continue # Saute l'itération si la donnée est altérée ou manquante
            
        option_data = q["options"][user_choice]
        sec_name = q.get('section', 'General Telemetry')
        
        if sec_name not in sections_data:
            sections_data[sec_name] = []
            
        sections_data[sec_name].append({
            "question": q.get('question', 'Missing Query String'),
            "choice_text": option_data.get('text', 'No value text'),
            "label": option_data.get('label', 'Standard Processing'),
            "advice": option_data.get('advice', 'No automated insight generated for this vector.')
        })
        all_labels.append(option_data.get('label', 'Standard Processing'))

# Double-sécurité : Si le parsing n'a extrait aucun label valide
if not all_labels:
    st.error("⚠️ Critical Telemetry Failure: Core analysis engine was unable to synthesize behavioral weights.")
    if st.button("Return to Master Core"):
        st.switch_page("pages/01_Assessment.py")
    st.stop()

# Calcul de l'Archétype Dominant
dominant_archetype = max(set(all_labels), key=all_labels.count)


# ==========================================
# PHASE 2 : RENDU GRAPHIQUE DU DASHBOARD (FORT & IMPACTANT)
# ==========================================

# Row 1 : Métriques d'identifications épurées
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="SYSTEM SUBJECT", value=pseudo.upper())
with col2:
    st.metric(label="ENTITY CLASSIFICATION", value=classification.upper())
with col3:
    st.metric(label="PRIMARY COGNITIVE ARCHETYPE", value=dominant_archetype.upper())

st.write("")
st.markdown("### 📊 Spectrum Distribution Mapping")
st.write("Quantified representation of your behavioral priorities across all evaluated decision vectors.")

# LE COMPOSANT "IMPRESSIONNANT" : Analyse statistique de la personnalité de l'utilisateur
# On compte les occurrences de chaque étiquette pour créer un graphique de répartition natif
label_counts = Counter(all_labels)
total_metrics = len(all_labels)

# Génération de colonnes d'affichage dynamiques basées sur le nombre de profils uniques détectés
dist_cols = st.columns(min(len(label_counts), 4))
for idx, (label_name, count) in enumerate(label_counts.items()):
    col_target = dist_cols[idx % len(dist_cols)]
    with col_target:
        percentage = int((count / total_metrics) * 100)
        st.caption(f"**{label_name}**")
        # Rendu visuel propre avec une barre de progression de poids
        st.progress(count / total_metrics, text=f"{percentage}% ({count} Pts)")

st.markdown("---")
st.markdown("### 🧬 Subsystem Deep Inspection Matrix")

# Row 2 : Isolation structurelle par Onglets (Tabs)
tab_names = [name.split(":")[1].strip() if ":" in name else name for name in sections_data.keys()]

if tab_names:
    tabs = st.tabs(tab_names)
    for tab, (sec_full_name, items) in zip(tabs, sections_data.items()):
        with tab:
            st.markdown(f"#### {sec_full_name}")
            st.caption(f"Decompressing active behavioral data traces for this node layer.")
            st.write("")
            
            for index, item in enumerate(items):
                with st.expander(f"Indicator {index + 1}: {item['label']}"):
                    st.markdown(f"**Trigger Context:** *{item['question']}*")
                    st.markdown(f"**Observed Behavior Pattern:** `{item['choice_text']}`")
                    st.divider()
                    # Rendu ultra net de l'insight pour le jury
                    st.info(f"🧠 **Systemic Insight:** {item['advice']}")
else:
    st.info("No layered partitions compiled yet.")


# ==========================================
# PHASE 3 : FOOTER SÉCURISÉ & LIEN DE FLUX
# ==========================================
st.markdown("---")
col_footer1, col_footer2 = st.columns([3, 1])

with col_footer1:
    st.caption("LUMEN Neural Engine v1.4.0 • Built for Devpost Hackathon Track Execution • Session Environment Secure")

with col_footer2:
    if st.button("Purge Session & Restart", use_container_width=True, type="secondary"):
        # Reset complet et propre du cerveau de l'application
        st.session_state.answers = {}
        st.session_state.current_q = 0
        # Utilisation du chemin exact de la page d'évaluation pour éviter les soucis de routage Windows
        st.switch_page("pages/01_Assessment.py")