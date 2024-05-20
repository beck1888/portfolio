import streamlit as st

# Set up page appearance
page_title = "Flashcards"
st.set_page_config(page_title, '💻', 'wide', 'collapsed')

# Project 3
st.markdown("### Project 3: Make some flashcards")
st.markdown("**Project description:** Here is the description of the project.")
st.markdown("**Challenges:** Here is the description of the challenges with creating the project.")
# st.markdown("**See the project in action**")
st.divider()

st.markdown("""This project was designed to show off my skills with file I/O, especially for json data.
            It is a set of flashcards that use key:value pairs to store a question and its correct answer. 
            It cycles through the questions and asks the user the question. If the user responds with the correct response, it marks it as correct, otherwise it marks it as wrong.
            It stores these stats in another file for the user to view. There are two sets of flashcards for the user to pick from. Each has its own stats.
            This project also has sound effects and uses escape codes to make the terminal look more pretty while playing the game.
            It shows the questions randomly and has some level of mistake processing so some typos can be made it will accept the answer. It also has a settings file that can be used to adjust speech and sound effects.""")

st.link_button(":blue[See GitHub Repo]", "https://github.com/beck1888/Flashcard_app")

st.divider()
st.title("Main flashcard feature")
st.video("src/flashcards_1a.mp4")

st.title("User stats feature")
st.video("src/flashcards_2.mov")