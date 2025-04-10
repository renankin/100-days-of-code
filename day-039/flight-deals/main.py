from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
import time
from datetime import datetime, timedelta

# ==================== Set up the Flight Search ====================
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

# =========== Update the Airport Codes in Google Sheet ====================
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# ==================== Search for Cheapest Flights ========================
tomorrow = (datetime.now() + timedelta(days=1))
six_months_from_today = (datetime.now() + timedelta(days=180))
for destination in sheet_data:
    city = destination["city"]
    code = destination["iataCode"]
    print(f"Getting flights for {city}")
    data = flight_search.find_flights(
        origin_city_code="MAN",
        destination_city_code=code,
        from_time=tomorrow,
        to_time=six_months_from_today,
    )
    flight_data = FlightData(data)
    flight_data.find_cheapest_flight()
    print(f"{city}: £{flight_data.price}")
    time.sleep(2)

# ================== Send notification =================================
    if flight_data.price != "N/A":
        if destination["lowestPrice"] > flight_data.price:
            formatted_msg = (
                f"Low price alert! Only {flight_data.price} to fly from "
                f"{flight_data.origin_airport} to "
                f"{flight_data.destination_airport}, "
                f"on {flight_data.out_date} to {flight_data.return_date}"
            )
            destination["lowestPrice"] = flight_data.price
            notification_manager = NotificationManager()
            notification_manager.send_message(formatted_msg)

data_manager.destination_data = sheet_data
data_manager.update_prices()
