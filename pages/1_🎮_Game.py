import streamlit as st

# Set up page appearance
page_title = "Game"
st.set_page_config(page_title, '💻', 'wide', 'expanded')

# Project 1
with st.container(border=True):
    st.markdown("### Project 1: Make a game")
    st.markdown("**Project description:** Here is the description of the project.")
    st.markdown("**Challenges:** Here is the description of the challenges with creating the project.")
    # st.markdown("**See the project in action**")
    st.divider()
    if st.button("▶️ Run project", key='1', use_container_width=True):
        prompt = st.chat_input("Say something")
        if prompt:
            st.write(f"User has sent the following prompt: {prompt}")
        pass # Game code