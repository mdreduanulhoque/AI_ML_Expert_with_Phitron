import streamlit as st

name = st.text_input("Enter your name: ")
age = st.number_input("Enter your age: ", value=None )
gender = st.selectbox("Enter your gender: ", ("Male","Female"),index=None, placeholder="Choose One")

button_click = st.button("Confirm", type="primary")

st.divider()
if button_click == True:
 st.text(f"Hello {name}, you are {age} years old\nYou are {gender}")
