import streamlit as st
import glob
import os
from cv_downloader import cv_downloader

def trim_filename(input_filename:str, chars_to_skip:int)-> str:
    filename = input_filename[chars_to_skip:-3].replace("_", " ")
    return filename


# def app():
#     st.title('Professional Experience')
#     cv_downloader()
#
#     for file in sorted(glob.glob("./docs/exp/*"), reverse=True): #Display most recent exp first
#         page_file = open(file, 'r')
#         file_title = trim_filename(file)
#         with st.expander(file_title):
#             st.markdown(page_file.read())

def app():
    st.title('Key Skills, Professional Experience and Education')

    cv_downloader()

    st.subheader('Key Skills')
    for file in sorted(glob.glob("./docs/skills/*"), reverse=True): #Display most recent exp first
        skills_file = open(file, 'r')
        file_title = trim_filename(file, 14)
        with st.expander(file_title):
            st.markdown(skills_file.read())


    st.subheader('Professional Experience')
    for file in sorted(glob.glob("./docs/exp/*"), reverse=True): #Display most recent exp first
        page_file = open(file, 'r')
        file_title = trim_filename(file, 16)
        with st.expander(file_title):
            st.markdown(page_file.read())


    st.subheader('Education')
    with st.expander('Education'):
        edu_file = open('./docs/education.md', 'r')
        st.markdown(edu_file.read())

