import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "steven.w.shatz@gmail.com"
password = "bjcd cajx fbis llqg"  # app password for this Portfolio App

receiver = username  # for testing

context = ssl.create_default_context()  # to send email securely

# Note: Subject must be 1st line of message
message = """\
Subject: This is a test
Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
