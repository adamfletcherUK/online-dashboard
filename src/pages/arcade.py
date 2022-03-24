import streamlit as st


def write():
    """Render the Arcade Page"""
    st.title('My Arcade Machine')
    column_1, column_2 = st.columns((2, 1))

    with column_1:
        st.header('All Things Retro-gaming')
        with open('./content/arcade/retro_games.md', 'r',
                  encoding="utf-8") as file_contents:
            st.markdown(file_contents.read())

    with column_2:
        st.image('./data/images/TNMT_arcade.png', width=300)

    # st.header('Retro Game Projects')
    # c3, c4 = st.columns((1, 2))
    # with c3:
    #     st.subheader('Arcade Control Board')
    #
    # with c4:
    #     st.subheader('Build Process')
