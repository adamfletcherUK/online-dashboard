"""Main module for the streamlit app"""
import awesome_streamlit as ast
import streamlit as st

import src.pages.arcade
import src.pages.deployment
import src.pages.exp
import src.pages.home
import src.pages.machine_learning
from cv_downloader import sidebar_cv_downloader

st.set_page_config(layout='wide', page_title="Adam Fletcher")
ast.core.services.other.set_logging_format()

PAGES = {
    "Home": src.pages.home,
    "Skill, Experience & Education": src.pages.exp,
    "Arcade Machine": src.pages.arcade,
    "Machine Learning": src.pages.machine_learning,
    "Deploying This Website": src.pages.deployment,
}


def main():
    """Main function of the App"""
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
    st.sidebar.info("If you are interested in the codebase for this multi-page Streamlit site, \n"
                    "it's on [github](https://github.com/adamfletcherUK/online-dashboard).")

if __name__ == "__main__":
    main()
