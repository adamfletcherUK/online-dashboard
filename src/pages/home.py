# """Home page shown when the user enters the application"""
import streamlit as st


def write():
    # st.image('./data/images/me_and_nat_cropped.jpg')
    with open('./content/home.md', 'r',
              encoding="utf-8") as file_contents:
        st.markdown(file_contents.read())
