import smtplib
import ssl
from email.message import EmailMessage


EMAIL="ENTER YOUR EMAIL HERE"
PASSWORD="ENTERR YOUR APP PASSWORD HERE"
RECEIVER_EMAIL="ENTER RECEIVER EMAIL HERE"
def send_email(subject, body, to_email):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = to_email
    msg.set_content(body)


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

send_email(
    subject="priya mitra ko yaad krte hue",
    body="i miss you priya mitra",
    to_email=RECEIVER_EMAIL
)
print("Email sent successfully!")
