"""Main module for the streamlit app"""
import awesome_streamlit as ast
import streamlit as st

import src.pages.arcade
import src.pages.case_study
import src.pages.deployment
import src.pages.education
import src.pages.home
import src.pages.machine_learning
import src.pages.personal
import src.pages.skills
# import src.pages.exp
from cv_downloader import sidebar_cv_downloader

st.set_page_config(layout='wide', page_title="Adam Fletcher, Ph.D")

PAGES = {
    "Home": src.pages.home,
    "Skills Overview": src.pages.skills,
    "Case Studies": src.pages.case_study,
    "Education": src.pages.education,
    # "Skill, Experience & Education": src.pages.exp,
    "Machine Learning": src.pages.machine_learning,
    "Personal": src.pages.personal,
    "Arcade Machine": src.pages.arcade,
    "Deploying This Website": src.pages.deployment,
}


def main():
    """Main function of the App"""
    # st.sidebar.image('./data/images/me_and_nat_cropped.jpg')
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)
    st.sidebar.title("My CV")
    st.sidebar.info("""Feel free to download my CV.
        But the webpage serves to act as an expanded version of my skill set & experience """)
    sidebar_cv_downloader()
    st.sidebar.title("About")
    st.sidebar.info(
        "If you are interested in the codebase for this multi-page Streamlit site, \n"
        "it's on [Github.com](https://github.com/adamfletcherUK/online-dashboard). \n\n"
        "[![Build Status](https://travis-ci.com/adamfletcherUK/online-dashboard.svg?branch=main)](https://travis-ci.com/adamfletcherUK/online-dashboard)")  # pylint: disable=line-too-long


if __name__ == "__main__":
    main()
