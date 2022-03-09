import streamlit as st

def app():
    page_file= open('./docs/deployment.md', 'r')
    st.markdown(page_file.read())
