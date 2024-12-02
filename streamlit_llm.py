#########################
## OpenAI in Streamlit ##
#########################

# Importing Libraries
import streamlit as st
from openai import OpenAI
import os

# Setting up OpenAI


# Windows PS: setx OPENAI_API_KEY "your_api_key_here"
key = 
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

client = OpenAI(api_key=key)

# Streamlit App

st.title('OpenAI Music Assistant')

st.write('This app will allow you to input an artist and a genre and receive a song lyric.')

# We will start with a side bar to ask the user for a genre

genre = st.sidebar.selectbox(
    'Select a genre:', 
    ['pop', 'rock', 'rap', 'country', 'jazz', 'metal', 'blues', 'folk', 'classical', 'reggae']
)

# We will then ask the user for an artist

artist = st.sidebar.text_input('Enter an artist:', 'Sabrina Carpenter')

# Now we need a place to display the lyrics

lyrics = st.empty()

#To choose language:
language = st.sidebar.selectbox(
    'Select a language:',
    ['English', 'Spanish', 'French', 'German', 'Italian']
)

#To choose themeL
custom_theme = st.sidebar.text_input('Enter a theme or topic for the song:', 'love')

# Now we need a button to generate the lyrics

if st.sidebar.button('Generate Lyrics'):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a lyrical genius."},
            {
                "role": "user",
                "content": f"Write a song lyric in the {genre} genre by {artist}, and provide it in {language} about {custom_theme}."
            }
        ]
    )
    lyrics.write(completion.choices[0].message.content)

# Check it out: https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps#build-a-chatgpt-like-app