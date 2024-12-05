import os
import requests
from dotenv import load_dotenv

load_dotenv()

IATA_ENDPOINT = \
    "https://test.api.amadeus.com/v1/reference-data/locations/cities"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API_KEY")
        self._secret = os.environ.get("AMADEUS_API_SECRET")
        self._token = self._get_new_token()
        self.bearer_header = {
            "Authorization": f"Bearer {self._token}"
        }

    def _get_new_token(self) -> str:
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
        token_expiration = response.json()["expires_in"]
        # print(f"Your access token is {access_token}")
        # print(f"Your access token expires in {token_expiration} seconds")
        return access_token

    def get_destination_code(self, city_name: str) -> str:
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
        print(f"Status code {response.status_code}. Airport IATA: "
              f"{response.text}")
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        else:
            return code
