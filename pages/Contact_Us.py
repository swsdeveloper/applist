import streamlit as st
import send_email as eml

st.header("Contact Me")

with st.form(key='email_form'):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")

    # Note: Subject must be 1st line of message AND must be followed by a CR
    message = f"""\
Subject: Portfolio Contact email from {user_email}

From: {user_email}
{raw_message}
"""

    button = st.form_submit_button("Submit")
    if button:
        eml.send_email(message)
        st.info("Your email was sent successfully!")
