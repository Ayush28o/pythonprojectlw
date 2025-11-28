import twilio
from twilio.rest import Client


account_sid = "ENTER ACCOUNT SID HERE"
auth_token = "ENTER AUTH TOKEN HERE"
TWILIONUMBER = "+13203772421"
RECEIVERPHONENUMBER = "ENTER RECEIVER PHONE NUMBER HERE"
client = Client(account_sid, auth_token)
message = client.messages.create(
    body="Hello from Twilio!",
    from_=TWILIONUMBER,
    to=RECEIVERPHONENUMBER
)
print(f"Message sent with SID: {message.sid}")
print("Email and SMS sent successfully!")

