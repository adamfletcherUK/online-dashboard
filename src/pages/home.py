import streamlit as st


def write():
    """Render the Main Homepage of the App"""
    # st.image('./data/images/me_and_nat_cropped.jpg')
    with open('./content/home/home_intro.md', 'r',
              encoding="utf-8") as file_contents:
        st.markdown(file_contents.read())

    col1, col2, col3 = st.columns(3)

    with col1:
        with open('./content/home/academic.md', 'r',
                  encoding="utf-8") as file_contents:
            st.markdown(file_contents.read())

    with col2:
        with open('./content/home/professional.md', 'r',
                  encoding="utf-8") as file_contents:
            st.markdown(file_contents.read())

    with col3:
        with open('./content/home/personal.md', 'r',
                  encoding="utf-8") as file_contents:
            st.markdown(file_contents.read())
