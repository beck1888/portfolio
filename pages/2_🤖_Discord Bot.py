import streamlit as st

# Set up page appearance
page_title = "Pages"
st.set_page_config(page_title, '💻', 'wide', 'expanded')

# Project 2
with st.container(border=True):
    st.markdown("### Project 2: Make a Discord bot")
    st.markdown("**Project description:** Here is the description of the project.")
    st.markdown("**Challenges:** Here is the description of the challenges with creating the project.")
    # st.markdown("**See the project in action**")
    st.divider()
    if st.button("▶️ Run project", key='2', use_container_width=True):
        st.toast("Oops! There is nothing here yet!", icon='🛑')
        pass # Perhaps a chat element to simulate it
