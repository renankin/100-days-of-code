from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

# Scrape the website to get the item price and title
amazon_url = ("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_"
              "=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
              "*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 "
                  "Safari/605.1.15",
}
response = requests.get(url=amazon_url, headers=header)
soup = BeautifulSoup(markup=response.content, features="html.parser")
item_title = soup.find(id="productTitle").getText().strip()
price_text = soup.find(class_="a-offscreen").getText()
price_as_float = float(price_text.split("$")[1])

# Send email notification
BUY_PRICE = 100
if price_as_float < BUY_PRICE:
    message = f"{item_title} is now {price_text}"
    with smtplib.SMTP(os.environ.get("SMTP_ADDRESS")) as connection:
        connection.starttls()
        connection.login(user=os.environ.get("MY_EMAIL"),
                         password=os.environ.get("MY_PASSWORD"))
        connection.sendmail(from_addr=os.environ.get("MY_EMAIL"),
                            to_addrs=os.environ.get("MY_EMAIL"),
                            msg=f"Subject:Amazon Price Alert!\n\n"
                                f"{message}\n{amazon_url}".encode("utf-8"))
