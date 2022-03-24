import streamlit as st


def write():
    """Render the Deployment Page"""
    with open('./content/deployment.md', 'r',
              encoding="utf-8") as file_contents:
        st.markdown(file_contents.read())
