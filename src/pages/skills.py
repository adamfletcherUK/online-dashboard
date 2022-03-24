import streamlit as st


def write():
    """Render the Skills Page"""
    with open('./content/skills.md', 'r',
              encoding="utf-8") as file_contents:
        st.markdown(file_contents.read())
