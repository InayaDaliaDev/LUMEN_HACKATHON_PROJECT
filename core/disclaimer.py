# ==============================================================================
# CORE/DISCLAIMER.PY : AVERTISSEMENT HUMAIN ET DÉCALÉ (DISCLAIMER)
# ==============================================================================
import streamlit as st


def render_lumen_disclaimer() -> None:
    """
    Affiche un avertissement cynique, réaliste et drôle en haut de l'application
    pour rappeler aux utilisateurs que Lumen n'est pas un substitut à l'éducation réelle.
    """
    with st.container():
        st.markdown(
            """
            > 🚨 **System Warning: Not a Life Coach (Yet).** 
            > 
            > Look, Lumen is a brilliant piece of software, but let's be real—it's still software. 
            > This app won't magically do your homework, replace years of actual studying, or fix your sleep schedule. 
            > If you're expecting a certified diploma or professional psychological validation out of a few 
            > click-through buttons, you might want to rethink your life choices. 
            > 
            > Proceed at your own risk, trust your own brain, and don't blame the code if reality hits hard. ☕
            """,
            unsafe_allow_html=True
        )
        st.divider()