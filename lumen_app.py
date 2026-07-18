import streamlit as st
st.set_page_config(page_title="LUMEN", page_icon="💡")
st.title("LUMEN: Cognitive Profiler 💡")
st.write("Welcome to the next generation of cognitive mapping.")
if st.button("Enter the Assessment"):
    st.switch_page("pages/Assessment.py")