import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

SHEETY_PRICES_ENDPOINT = \
    "https://api.sheety.co/efb4d596bd2fdf48151daec54b42d401/flights/prices"


class DataManager:
    def __init__(self):
        self._user = os.environ.get("SHEETY_USERNAME")
        self._password = os.environ.get("SHEETY_PASSWORD")
        self.authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(
            url=SHEETY_PRICES_ENDPOINT,
            auth=self.authorization
        )
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city["id"]}",
                json=new_data,
                auth=self.authorization,
            )
            response.raise_for_status()

    def update_prices(self):
        for price in self.destination_data:
            new_data = {
                "price": {
                    "lowestPrice": price["lowestPrice"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{price["id"]}",
                json=new_data,
                auth=self.authorization,
            )
            response.raise_for_status()
