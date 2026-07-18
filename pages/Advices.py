import streamlit as st
from data.question import ALL_QUESTIONS

st.title("Your Cognitive Profile 🧠")

# Vérification : est-ce que l'utilisateur a fini le test ?
if 'answers' not in st.session_state or not st.session_state.answers:
    st.warning("You haven't completed the assessment yet!")
    if st.button("Go to Assessment"):
        st.switch_page("pages/Assessment.py")
    st.stop()

# Analyse des résultats
answers = st.session_state.answers
st.write(f"Hello {st.session_state.user_profile['pseudo']}! Here is your breakdown:")

# On parcourt les questions pour afficher les conseils
for q in ALL_QUESTIONS:
    q_id = q['id']
    if q_id in answers:
        user_choice = answers[q_id]
        option_data = q['options'][user_choice]
        
        with st.expander(f"{q['section']} - {q['label'] if 'label' in option_data else 'Analysis'}"):
            st.markdown(f"**Your response:** {option_data['text']}")
            st.info(f"**Insight:** {option_data['advice']}")

if st.button("Restart Assessment"):
    st.session_state.answers = {}
    st.session_state.current_q = 0
    st.switch_page("pages/Assessment.py")