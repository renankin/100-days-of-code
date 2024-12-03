from datetime import datetime
import pandas
from random import randint
import smtplib
import os

MY_EMAIL = "pythonisfun0@gmail.com"
MY_PASSWORD = os.environ.get("GMAIL_PASSWORD")

now = datetime.now()
today_tuple = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (data_row.month, data_row.day): data_row for
    (index, data_row) in data.iterrows()
}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{randint(1, 3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
