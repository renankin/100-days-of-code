import smtplib
import random
import datetime as dt
import os

MY_EMAIL = os.environ.get("GMAIL_USERNAME")
MY_PASSWORD = os.environ.get("GMAIL_PASSWORD")

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Quote of the day\n\n{quote}"
        )
