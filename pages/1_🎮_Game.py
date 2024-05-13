import streamlit as st

# Set up page appearance
page_title = "Game"
st.set_page_config(page_title, '💻', 'wide', 'expanded')

# Project 1
st.markdown("### Project 1: Make a game")
st.markdown("**Project description:** Here is the description of the project.")
st.markdown("**Challenges:** Here is the description of the challenges with creating the project.")
st.divider()

# Chat element for the game code



# Simple respond function that echoes the user input
def respond(user_input):
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