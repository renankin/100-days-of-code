import requests
import os
from twilio.rest import Client

owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("API_KEY")
account_sid = "ACc92ab8dfc63f45ef93a25ab718b0e213"
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 64.226997,
    "lon": 27.728500,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(
    url=owm_endpoint,
    params=parameters
)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+12622057162",
        to="+447985503160",
    )
    print(message.status)
