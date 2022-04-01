import streamlit as st


def write():
    """Render the Personal Page"""
    with open('./content/personal.md', 'r',
              encoding="utf-8") as file_contents:
        st.markdown(file_contents.read())
