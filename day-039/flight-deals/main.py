from flight_search import FlightSearch
from data_manager import DataManager
from pprint import pprint
import time


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)
flight_search = FlightSearch()

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)

pprint(sheet_data)

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()
