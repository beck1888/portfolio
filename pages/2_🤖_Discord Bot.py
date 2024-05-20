import streamlit as st

# Set up page appearance
page_title = "Pages"
st.set_page_config(page_title, '💻', 'wide', 'collapsed')

# Project 2
st.markdown("### Project 2: Make a Discord bot")
st.markdown("**Project description:** Here is the description of the project.")
st.markdown("**Challenges:** Here is the description of the challenges with creating the project.")
# st.markdown("**See the project in action**")
st.divider()
st.link_button("🤖 Run Bot", "https://discord.com/oauth2/authorize?client_id=1195290307374366810")
st.link_button(":blue[See code]", "https://github.com/beck1888/Discord-Translator-Bot")