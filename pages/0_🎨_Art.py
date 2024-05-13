import streamlit as st

# Set up page appearance
page_title = "Art"
st.set_page_config(page_title, '💻', 'wide', 'expanded')

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