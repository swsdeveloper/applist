import smtplib
import ssl


def send_email(message):
    """
    Send email to myself containing a user's email address and message.
    This is invoked when user presses "Submit" button on Contact page.
    :param message: a text message (str)
    :return: None
    """
    host = "smtp.gmail.com"
    port = 465

    username = "steven.w.shatz@gmail.com"
    password = "bjcd cajx fbis llqg"  # app password for this Portfolio App

    receiver = username

    context = ssl.create_default_context()  # to send email securely

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
