from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWILIO_VIRTUAL_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send_message(self, message_body):
        """
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API
        to send an SMS from a predefined virtual number (provided by Twilio)
        to your own "verified" number. It logs the unique SID (Session ID)
        of the message, which can be used to verify that the message was
        sent successfully.

        Parameters:
        message_body (str): The text content of the SMS message to be sent.
        """
        message = self.client.messages.create(
            body=message_body,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=MY_NUMBER,
        )
        print(message.body)
