import streamlit as st
import base64
from mutagen.mp3 import MP3
from uuid import uuid4
from time import sleep

# Set up page appearance
page_title = "Game"
st.set_page_config(page_title, '💻', 'wide', 'collapsed')

# Project 1
st.markdown("### Project 1: Make a game")
st.markdown("**Project description:** Here is the description of the project.")
st.markdown("**Challenges:** Here is the description of the challenges with creating the project.")
st.divider()

def main():
    ...