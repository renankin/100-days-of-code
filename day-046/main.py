import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Load environment variables for Spotipy
load_dotenv()
APP_CLIENT_ID = os.environ.get("APP_CLIENT_ID")
APP_CLIENT_SECRET = os.environ.get("APP_CLIENT_SECRET")
APP_REDIRECT_URI = os.environ.get("APP_REDIRECT_URI")

# Scraping Billboard 100
date = input(
    "Which year do you want to travel to? Type the date in this format "
    "YYYY-MM-DD:"
)
url = f"https://www.billboard.com/charts/hot-100/{date}/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) "
                  "Gecko/20100101 Firefox/131.0"
}
response = requests.get(url=url, headers=header)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
title_tags = soup.select(selector="li ul li h3")
song_titles = [tag.getText().strip() for tag in title_tags]

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=APP_CLIENT_ID,
                              client_secret=APP_CLIENT_SECRET,
                              redirect_uri=APP_REDIRECT_URI,
                              scope="playlist-modify-private")
)
user_id = sp.current_user()["id"]

# Search Spotify for songs by title
songs_uri = []
year = date.split("-")[0]
for song in song_titles:
    result = sp.search(
        q=f"track:{song} year:{year}",
        type="track",
        limit=1
    )
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

# Create playlist for user in private
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False
)

# Add songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uri)
