import glob

import streamlit as st


def trim_filename(input_filename: str, chars_to_skip: int) -> str:
    """Trims a filename string by skipping the first n characters and the last 3 characters:
        Parameters:
                input_filename (str): the original name of the file
                chars_to_skip (str): the number of characters to skip

        Returns:
                filename (str): the trimmed filename
    """
    filename = input_filename[chars_to_skip:-3].replace("_", " ")
    return filename


def write():
    """
    Render the Expertise page
    """
    st.title('Key Skills, Professional Experience and Education')

    st.subheader('Key Skills')
    for file in sorted(glob.glob("./content/skills/*"), reverse=True):
        with open(file, 'r', encoding='utf-8') as skills_file:
            file_title = trim_filename(file, 17).capitalize()
            with st.expander(file_title):
                st.markdown(skills_file.read())

    st.subheader('Professional Experience')
    for file in sorted(glob.glob("./content/exp/*"), reverse=True):
        with open(file, 'r', encoding='utf-8') as page_file:
            file_title = trim_filename(file, 19).capitalize()
            with st.expander(file_title):
                st.markdown(page_file.read())

    st.subheader('Education')
    with st.expander('Education'):
        with open('./content/education.md', 'r', encoding='utf-8') as edu_file:
            st.markdown(edu_file.read())
