import streamlit as st


def write():
    """Render the Education Page"""
    with open('./content/education.md', 'r',
              encoding="utf-8") as file_contents:
        st.markdown(file_contents.read())
