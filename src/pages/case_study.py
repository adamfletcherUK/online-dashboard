import glob

import streamlit as st


def write():
    """
    Render the Expertise page
    """
    st.title('Case Studies')
    for file in sorted(glob.glob("./content/exp/*"), reverse=True):
        with open(file, 'r', encoding='utf-8') as page_file:
            st.markdown(page_file.read())
