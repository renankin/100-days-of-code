from twilio.rest import Client
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()


class NotificationManager:

    def __init__(self):
        self._twilio_sid = os.environ.get("TWILIO_SID")
        self._twilio_token = os.environ.get("TWILIO_TOKEN")
        self._twilio_virtual_number = os.environ.get("TWILIO_VIRTUAL_NUMBER")
        self._personal_number = os.environ.get("MY_NUMBER")
        self.client = Client(self._twilio_sid, self._twilio_token)
        self._email = os.environ.get("SMTP_EMAIL")
        self._email_password = os.environ.get("SMTP_PASSWORD")
        self.connection = smtplib.SMTP(
            os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
        )

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
            from_=self._twilio_virtual_number,
            to=self._personal_number,
        )
        print(message.body)

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(
                user=self._email,
                password=self._email_password
            )
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self._email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n"
                        f"\n{email_body}".encode('utf-8')
                )
