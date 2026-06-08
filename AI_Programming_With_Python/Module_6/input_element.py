import streamlit as st

name = st.text_input("Enter your name: ")
age = st.number_input("Enter your age: ", value=None )
username = st.text_input("Enter your username: ")
password = st.text_input("Enter tour password: ", type="password")

button_click = st.button("Confirm", type="primary")

st.divider()
if button_click == True:
 st.text(f"Hello {name}, you are {age} years old")
