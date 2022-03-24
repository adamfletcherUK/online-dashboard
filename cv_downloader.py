import streamlit as st


def cv_downloader():
    with open("./data/2022 Adam Fletcher CV.pdf", "rb") as cv_file:
        st.download_button(label='Download CV',
                           data=cv_file,
                           file_name="Adam Fletcher CV.pdf"
                           )


def sidebar_cv_downloader():
    with open("./data/2022 Adam Fletcher CV.pdf", "rb") as cv_file:
        st.sidebar.download_button(label='Download CV',
                                   data=cv_file,
                                   file_name="Adam Fletcher CV.pdf"
                                   )
