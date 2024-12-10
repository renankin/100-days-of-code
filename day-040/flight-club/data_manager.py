import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()


class DataManager:
    def __init__(self):
        self._user = os.environ.get("SHEETY_USERNAME")
        self._password = os.environ.get("SHEETY_PASSWORD")
        self.prices_endpoint = os.environ.get("SHEETY_PRICES_ENDPOINT")
        self.users_endpoint = os.environ.get("SHEETY_USERS_ENDPOINT")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(
            url=self.prices_endpoint,
            auth=self._authorization
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
                url=f"{self.prices_endpoint}/{city["id"]}",
                json=new_data,
                auth=self._authorization,
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
                url=f"{self.prices_endpoint}/{price["id"]}",
                json=new_data,
                auth=self._authorization,
            )
            response.raise_for_status()

    def get_customer_data(self):
        response = requests.get(
            url=self.users_endpoint,
            auth=self._authorization
        )

        data = response.json()
        self.customer_data = data["users"]

        return self.customer_data
