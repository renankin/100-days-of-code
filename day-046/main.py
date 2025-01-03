import requests
from bs4 import BeautifulSoup

date = input(
    "Which year do you want to travel to? Type the date in this format "
    "YYYY-MM-DD:"
)

url = f"https://www.billboard.com/charts/hot-100/{date}/"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) "
                  "Gecko/20100101 Firefox/131.0"}

response = requests.get(url=url, headers=header)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
title_tags = soup.select(selector="li ul li h3")
song_titles = [tag.getText().strip() for tag in title_tags]
print(song_titles)
