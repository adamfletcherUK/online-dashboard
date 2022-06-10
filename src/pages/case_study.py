import streamlit as st

case_studies_dict = {
    'Predicting the Price of Used Machinery': 'content/exp/ee predicting machinery price.md',
    'Generating Realistic Synthetic Data': 'content/exp/ee synthetic data.md',
    'Uses of Data Science in Government': 'content/exp/ee AI in government.md',
    'Guiding Transformation of a Large Government Organisation Through Data': 'content/exp/ee gov transformation.md',
    'Modelling Call Transcripts to determine key Questions': 'content/exp/ee topic modelling conversations.md',
    'Developing Needs Based Personas From User Behavior': 'content/exp/ee needs based personas.md',
    'Determining the Cost of Debt for Delayed Payment Terms': 'content/exp/ee cost of debt.md',
    'Determining Variations in a Cost of Service': 'content/exp/ee cost of variation.md',
    'Identifying markers leading to chemotherapy resistance in lung cancer': 'content/exp/CRUK Postdoc.md',
    'Predicting Chromosomal Abnormalities From Blood Samples': 'content/exp/Premaitha Down Syndrome.md',
    'Post Market Surveillance Using Local Regression': 'content/exp/Premaitha Post Market Surveillance.md',

}


def write():
    """
    Render the Expertise page
    """
    st.title('Case Studies')
    for i, case_study in zip(range(1, len(case_studies_dict) + 1), case_studies_dict):
        with open(case_studies_dict[case_study], 'r', encoding='utf-8') as page_file:
            with st.expander(f'{i}. {case_study}'):
                st.markdown(page_file.read())
