import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
IATA_ENDPOINT = \
    "https://test.api.amadeus.com/v1/reference-data/locations/cities"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_SEARCH_ENDPOINT = \
    "https://test.api.amadeus.com/v2/shopping/flight-offers"


class FlightSearch:
    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API_KEY")
        self._secret = os.environ.get("AMADEUS_API_SECRET")
        self._token = self._get_new_token()
        self.bearer_header = {
            "Authorization": f"Bearer {self._token}"
        }

    def _get_new_token(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._secret,
        }
        response = requests.post(
            url=TOKEN_ENDPOINT, headers=header, data=body
        )
        access_token = response.json()["access_token"]
        return access_token

    def get_destination_code(self, city_name):
        """
        Retrieves the IATA code for a specified city using the Amadeus
        Location API

        Parameters:
            city_name (str): The name of the city for which to find the IATA
            code.

        Returns:
            str: The IATA code of the first matching city if found; "N/A" if
            no match is found due to an IndexError, or "Not Found" if no
            match is found due to a KeyError.
        """
        search_params = {
            "keyword": city_name,
            "include": "AIRPORTS",
            "max": 1,
        }
        response = requests.get(
            url=IATA_ENDPOINT,
            headers=self.bearer_header,
            params=search_params
        )
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            return "N/A"
        except KeyError:
            return "Not Found"
        else:
            return code

    def find_flights(self, origin_city_code, destination_city_code,
                     from_time, to_time, is_direct=True):
        """
        Searches for flight options between two cities on specified
        departure and return dates using the Amadeus API.

        Parameters:
            origin_city_code (str): The IATA code of the departure city.
            destination_city_code (str): The IATA code of the destination city.
            from_time (datetime): The departure date.
            to_time (datetime): The return date.
            is_direct (bool): Whether the flight is direct or indirect.

        Returns:
            dict or None: A dictionary containing flight offer data if the
            query is successful; None if there is an error.
        """
        search_params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "max": 10,
            "currencyCode": "GBP",
            "nonStop": "true" if is_direct else "false",
        }

        response = requests.get(
            url=FLIGHT_SEARCH_ENDPOINT,
            params=search_params,
            headers=self.bearer_header
        )

        if response.status_code != 200:
            print(response.text)
            return None

        return response.json()
