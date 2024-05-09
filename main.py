# Import block
import streamlit as st
from PIL import Image

# Set up page appearance
st.set_page_config("Beck's Python Profile", '💻', 'wide', 'collapsed')

# Page title
st.title("Beck's Python Portfolio")

# Info box
with st.expander("ℹ️ About this portfolio", expanded=False):
    st.markdown("### Portfolio info")
    st.markdown("**Years:** Fall 2023 to Spring 2024 (High School Junior).")
    st.markdown("**Class:** Introduction to computer science and coding.")
    st.markdown("*This portfolio also contains personal projects I've done outside of class.*""")
    st.page_link(page="https://github.com/beck1888/portfolio", label=":blue[Click here to see the GitHub repo for this page]", icon="🔨")

# Project 0
with st.container(border=True):
    st.markdown("### Project 0: Make an art")
    st.page_link(page="https://about:blank", label=":blue[GitHub]", icon="↗️")
    st.markdown("**Project description:** Here is the description of the project.")
    st.markdown("**Challenges:** Here is the description of the challenges with creating the project.")
    # st.markdown("**See the project in action**")
    st.divider()
    if st.button("▶️ Run project", key='0', use_container_width=True):
        turtle_draw_video = open('src/Project_0.mp4', 'rb').read()
        st.video(turtle_draw_video, autoplay=True)

# Project 1
with st.container(border=True):
    st.markdown("### Project 1: Make a game")
    st.markdown("**Project description:** Here is the description of the project.")
    st.markdown("**Challenges:** Here is the description of the challenges with creating the project.")
    # st.markdown("**See the project in action**")
    st.divider()
    if st.button("▶️ Run project", key='1', use_container_width=True):
        pass # Game code

# Project 2
with st.container(border=True):
    st.markdown("### Project 2: Make a Discord bot")
    st.markdown("**Project description:** Here is the description of the project.")
    st.markdown("**Challenges:** Here is the description of the challenges with creating the project.")
    # st.markdown("**See the project in action**")
    st.divider()
    if st.button("▶️ Run project", key='2', use_container_width=True):
        pass # Perhaps a chat element to simulate it

# Project 3
with st.container(border=True):
    st.markdown("### Project 3: Make some flashcards")
    st.markdown("**Project description:** Here is the description of the project.")
    st.markdown("**Challenges:** Here is the description of the challenges with creating the project.")
    # st.markdown("**See the project in action**")
    st.divider()
    if st.button("▶️ Run project", key='3', use_container_width=True):
        pass # Simulator

# Project 4
with st.container(border=True):
    st.markdown("### Project 4: Make a graph")
    st.markdown("**Project description:** Here is the description of the project.")
    st.markdown("**Challenges:** Here is the description of the challenges with creating the project.")
    # st.markdown("**See the project in action**")
    st.divider()
    if st.button("▶️ Run project", key='4', use_container_width=True):
        pass # Use the code from other streamlet project