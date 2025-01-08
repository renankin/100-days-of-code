from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

# Load variables for SMTP
load_dotenv()
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
SMTP_ADDRESS = os.environ.get("SMTP_ADDRESS")

# Scrape the website to get the price
amazon_url = "https://appbrewery.github.io/instant_pot/"
response = requests.get(url=amazon_url)
soup = BeautifulSoup(markup=response.content, features="html.parser")
item_title = soup.find(id="productTitle").getText()
price_text = soup.find(class_="a-offscreen").getText()
price_float = float(price_text.split("$")[1])

# Send email notification
if price_float < 100:
    with smtplib.SMTP(SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Amazon Price Alert!\n\n{item_title} is now {price_text} "
                f"{amazon_url}"
        )
