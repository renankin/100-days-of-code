import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.select(selector="h2 strong")
movie_titles = [movie.getText() for movie in reversed(all_movies)]

with open("movie.txt", mode="w") as file:
    for title in movie_titles:
        file.write(f"{title}\n")
