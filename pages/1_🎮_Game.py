import streamlit as st
import base64
from mutagen.mp3 import MP3
from uuid import uuid4
from time import sleep

# Set up page appearance
page_title = "Game"
st.set_page_config(page_title, '💻', 'wide', 'collapsed')

# # Config globals
# global stage
# stage = 'init'
# global money
# money = 50
# global points
# points = 10

# Project 1
st.markdown("### Project 1: Make a game")
st.markdown("**Project description:** Here is the description of the project.")
st.markdown("**Challenges:** Here is the description of the challenges with creating the project.")
st.divider()

# # Chat element for the game code

# def play(file_path: str, file_extension: str):
#     with open(file_path, "rb") as f:
#         # Convert the file's bytes into base64
#         data = f.read()
#         b64 = base64.b64encode(data).decode()

#         # Unique identifier for each audio element
#         unique_id = str(uuid4())[:4]

#         # HTML code to auto play the audio, hide the player
#         md = f"""
#             <audio id="{unique_id}" controls autoplay="true" style="display: none;">
#             <source src="data:audio/mp3;base64,{b64}" type="audio/{file_extension}">
#             </audio>
#             """

#         # Creates a temporary holder for the player
#         audio_player = st.empty()

#         # Runs the player element
#         audio_player.markdown(
#             md,
#             unsafe_allow_html=True
#         )

#         # Wait for sound to finish
#         sleep(MP3(file_path).info.length + 0.1) # Wait 0.1 extra seconds to allow for loading times

#         # Delete the audio player
#         audio_player.empty()

# def sound_manager(name):
#     if name == "cow":
#         play("src/moo.mp3", "mp3")
#     else:
#         return

# # Simple respond function that echoes the user input
# def respond(user_input):
#     sound_manager(user_input)
#     return f"Bot: {user_input}"  # This can be replaced with any response generation logic

# # Manages the game
# def game_logic(do_stage, usr_input=None):
#     ui = usr_input
#     ds = do_stage
#     m = money
#     p = points

#     if ds == 'init':
#         pack = {
#             "respond": "Welcome to the shopping game! What is your name?",
#             "money": 50,
#             "points": 10
#         }
#     elif ds == 'name':
#         pass
#     elif ds == 'age':
#         pass
#     elif ds == 'cart':
#         pass
#     elif ds == 'beans':
#         pass
#     elif ds == 'eggs':
#         pass
#     elif ds == 'milk':
#         pass
#     elif ds == 'bread':
#         pass
#     elif ds == 'coffee':
#         pass
#     elif ds == 'fruit':
#         pass
#     elif ds == 'veggies':
#         pass
#     elif ds == 'candy':
#         pass
#     elif ds == 'book':
#         pass
#     elif ds == 'phone':
#         pass
#     elif ds == 'budget':
#         pass
#     elif ds == 'points':
#         pass
#     elif ds == 'drive':
#         pass
#     elif ds == 'unpack':
#         pass
#     else:
#         pass # win

#     return pack

# # Function to handle new messages
# def add_to_chat():
#     user_input = st.session_state.user_input
#     if user_input:  # Ensure non-empty input
#         # Append user input to chat history
#         st.session_state.chat_history.append(f"You: {user_input}")
#         # Get response from the bot
#         response = game_logic(user_input)
#         # Append bot's response to chat history
#         st.session_state.chat_history.append(response)
#         # Clear the current input
#         st.session_state.user_input = ""

# # Initialize session state attributes if not already present
# if 'chat_history' not in st.session_state:
#     st.session_state.chat_history = [] #["*:green[      Welcome! Type anything to begin!]*"]

# if 'user_input' not in st.session_state:
#     st.session_state.user_input = ""

# # Play game text
# st.markdown("<h2 style='text-align: center; color: blue;'>Play the game here!</h2>", unsafe_allow_html=True)

# col1, col2 = st.columns(2)

# with col2:
#     # Create a container for chat messages
#     chat_container = st.container(border=True)
#     # Initialize the first message to show the container - shows as nothing
#     st.session_state.chat_history.append("")

# with col1:
#     with st.container(border=True):
#         # Text input for user input
#         user_input = st.text_input("Type here:", key="user_input", on_change=add_to_chat)
#         st.markdown("<p style='text-align: center; color: grey;'>Press enter to send</p>", unsafe_allow_html=True)


# # Display the chat history in the dedicated container
# if st.session_state.chat_history:
#     with chat_container:
#         st.markdown("<h3 style='text-align: center; color: black;'>Game Log</h3>", unsafe_allow_html=True)
#         st.divider()
#         for message in st.session_state.chat_history:
#             message: str
#             if "Bot: " in message:
#                 st.markdown(f"*:green[      {message.removeprefix("Bot: ")}]*")
#             elif "You: " in message:
#                 st.markdown(f"**:black[>>  {message.removeprefix("You: ")}]**")