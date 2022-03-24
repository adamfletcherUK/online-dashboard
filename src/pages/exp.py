import streamlit as st
import glob

def trim_filename(input_filename:str, chars_to_skip:int)-> str:
    filename = input_filename[chars_to_skip:-3].replace("_", " ")
    return filename


# def app():
#     st.title('Professional Experience')
#     cv_downloader()
#
#     for file in sorted(glob.glob("./content/exp/*"), reverse=True): #Display most recent exp first
#         page_file = open(file, 'r')
#         file_title = trim_filename(file)
#         with st.expander(file_title):
#             st.markdown(page_file.read())

def write():
    st.title('Key Skills, Professional Experience and Education')

    st.subheader('Key Skills')
    for file in sorted(glob.glob("./content/skills/*"),
                       reverse=True):  # Display most recent exp first
        skills_file = open(file, 'r', encoding='utf-8')
        file_title = trim_filename(file, 17)
        with st.expander(file_title):
            st.markdown(skills_file.read())

    st.subheader('Professional Experience')
    for file in sorted(glob.glob("./content/exp/*"),
                       reverse=True):  # Display most recent exp first
        page_file = open(file, 'r', encoding='utf-8')
        file_title = trim_filename(file, 19)
        with st.expander(file_title):
            st.markdown(page_file.read())

    st.subheader('Education')
    with st.expander('Education'):
        edu_file = open('./content/education.md', 'r', encoding='utf-8')
        st.markdown(edu_file.read())

    # show_source_code = st.sidebar.checkbox("Show Source Code", False)
    #
    # if show_source_code:
    #     st.header("Source code")
    #     # Fetch the content
    #     with open('./src/pages/exp.py') as f:
    #         lines = f.readlines()
    #     st.code(open('./src/pages/exp.py'), language='Python')
