import streamlit as st

st.header("Contact Me")

with st.form('Contact_Form'):
    email = st.text_input("Your email address")
    message = st.text_input("Your message")
    st.form_submit_button("Submit")
