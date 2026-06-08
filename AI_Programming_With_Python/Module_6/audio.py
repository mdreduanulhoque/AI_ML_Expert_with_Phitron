import streamlit as st 

st.title("Input your files (audio)",anchor=False)

st.divider()


audio_file = st.file_uploader("Enter your audio",
                 type=['mp3','ogg','flac'],
                 )



print(type(audio_file))

if audio_file:
    st.audio(audio_file)