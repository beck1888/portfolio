import streamlit as st
import base64
from mutagen.mp3 import MP3
from uuid import uuid4
from time import sleep

# Set up page appearance
page_title = "Game"
st.set_page_config(page_title, '💻', 'wide', 'expanded')

# Project 1
st.markdown("### Project 1: Make a game")
st.markdown("**Project description:** Here is the description of the project.")
st.markdown("**Challenges:** Here is the description of the challenges with creating the project.")
st.divider()

# Chat element for the game code

def play(file_path: str, file_extension: str):
    with open(file_path, "rb") as f:
        # Convert the file's bytes into base64
        data = f.read()
        b64 = base64.b64encode(data).decode()

        # Unique identifier for each audio element
        unique_id = str(uuid4())[:4]

        # HTML code to auto play the audio, hide the player
        md = f"""
            <audio id="{unique_id}" controls autoplay="true" style="display: none;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/{file_extension}">
            </audio>
            """

        # Creates a temporary holder for the player
        audio_player = st.empty()

        # Runs the player element
        audio_player.markdown(
            md,
            unsafe_allow_html=True
        )

        # Wait for sound to finish
        sleep(MP3(file_path).info.length + 0.1) # Wait 0.1 extra seconds to allow for loading times

        # Delete the audio player
        audio_player.empty()

def sound_manager(name):
    if name == "cow":
        play("src/moo.mp3", "mp3")
    else:
        return

# Simple respond function that echoes the user input
def respond(user_input):
    sound_manager(user_input)
    return f"Bot: {user_input}"  # This can be replaced with any response generation logic

# Function to handle new messages
def add_to_chat():
    user_input = st.session_state.user_input
    if user_input:  # Ensure non-empty input
        # Append user input to chat history
        st.session_state.chat_history.append(f"You: {user_input}")
        # Get response from the bot
        response = respond(user_input)
        # Append bot's response to chat history
        st.session_state.chat_history.append(response)
        # Clear the current input
        st.session_state.user_input = ""

# Initialize session state attributes if not already present
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

# Create a container for chat messages
chat_container = st.container(border=True)

# Text input for user input
user_input = st.text_input("Type your message:", key="user_input", on_change=add_to_chat)

# Display the chat history in the dedicated container
if st.session_state.chat_history:
    with chat_container:
        for message in st.session_state.chat_history:
            st.write(message)