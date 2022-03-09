import streamlit as st

def app():
    page_file= open('./docs/machinelearning.md', 'r')
    st.markdown(page_file.read())