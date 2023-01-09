import smtplib, ssl
import os

def send_email(message, receiver):
    host = 'smtp.gmail.com'
    port = 465

    username = "weatherforecast32@gmail.com"

    password = "qjcpxtkcohvhyscd"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
