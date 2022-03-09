import streamlit as st

def app():
    st.title('My Arcade Machine')
    c1, c2 = st.columns((2, 1))

    with c1:
        st.header('All Things Retro-gaming')
        page_file= open('./docs/arcade/retro_games.md', 'r')
        st.markdown(page_file.read())

    with c2:
        st.image('./data/images/TNMT_arcade.png', width=300)

    # st.header('Retro Game Projects')
    # c3, c4 = st.columns((1, 2))
    # with c3:
    #     st.subheader('Arcade Control Board')
    #
    # with c4:
    #     st.subheader('Build Process')