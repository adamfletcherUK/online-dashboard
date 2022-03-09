import streamlit as st

def cv_downloader():
    with open("./data/2022 Adam Fletcher CV.pdf", "rb") as cv_file:
        btn = st.download_button(label='Download CV',
                                 data=cv_file,
                                 file_name="Adam Fletcher CV.pdf"
                       )