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

st.markdown("""
This project was to show off my skills with conditional logic. It features a shopping game where the user can put items in their basket.
            However, there is a budget the user must stay within, and there are certain 'necessities' the user must spend money on, requiring them to plan ahead.
            To make this even more interactive, I added sound effects using a module called playsound. Later, I switched to using pygame for this
            because Replit does not support playsound.""")

st.link_button(":blue[See GitHub Repo]", "https://github.com/beck1888/comp-sci-game")

st.divider()
st.title("Limited demo")
st.video("src/game.mov")