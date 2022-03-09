import streamlit as st

def app():
    st.image('./data/images/me_and_nat_cropped.jpg')

    page_file= open('./docs/home.md', 'r')
    st.markdown(page_file.read())


