import streamlit as st
from send_email import send_email

st.title("Contact Me")

with st.form("email", clear_on_submit=True):
    user_email = st.text_input("Enter your email")
    subject = st.text_input("Subject (optional)")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        send_email(user_email, message, subject)
        st.info("Your email was sent successfully")