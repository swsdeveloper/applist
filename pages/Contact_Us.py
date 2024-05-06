import streamlit as st


def send_email(email, email_body):
    to_email = 'sshatz@aesopscorp.com'
    subject = "Email sent from Contact us page of Portfolio web page"
    pass


st.header("Contact Me")

with st.form(key='email_form'):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        send_email(user_email, message)
