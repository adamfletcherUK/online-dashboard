import streamlit as st


def write():
    """Render the Machine Learning Page"""
    with open('./content/machinelearning.md', 'r',
              encoding="utf-8") as file_contents:
        st.markdown(file_contents.read())
