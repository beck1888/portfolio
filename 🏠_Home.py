# Start app with
"""
st run 🏠_Home.py
"""

# Import block
import streamlit as st
from PIL import Image
import json

# Set up page appearance
page_title = "Home"
st.set_page_config(page_title, '💻', 'wide', 'expanded')

# Page title
st.title("Beck's Python Portfolio")

# Info box
with st.container(border=True):
    st.markdown("### Portfolio info")
    st.markdown("**Years:** Fall 2023 to Spring 2024 (High School Junior).")
    st.markdown("**Class:** Introduction to computer science and coding.")
    # st.markdown("*This portfolio also contains personal projects I've done outside of class.*""")
    st.page_link(page="https://github.com/beck1888/portfolio", label=":blue[Click here to see the GitHub repo for this page]", icon="🔨")

st.markdown("<h4 style='text-align: center; color: grey;'>Use the links on the left sidebar to see different projects</h4>", unsafe_allow_html=True)