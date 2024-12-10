from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import find_cheapest_flight
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

# data_manager.destination_data = sheet_data
# data_manager.update_destination_codes()

# ==================== Retrieve customer emails =====================
customer_data = data_manager.get_customer_data()
customer_email = [row["whatIsYourEmail?"] for row in customer_data]

# ==================== Search for Cheapest Flights ========================
tomorrow = (datetime.now() + timedelta(days=1))
six_months_from_today = (datetime.now() + timedelta(days=180))
for destination in sheet_data:
    city = destination["city"]
    code = destination["iataCode"]
    print(f"Getting flights for {city}")
    flights = flight_search.find_flights(
        origin_city_code="MAN",
        destination_city_code=code,
        from_time=tomorrow,
        to_time=six_months_from_today
    )

    cheapest_flight = find_cheapest_flight(flights)
    print(f"{city}: £{cheapest_flight.price}")
    time.sleep(2)

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination["city"]}. Looking for "
              f"indirect flights...")
        stopover_flights = flight_search.find_flights(
            origin_city_code="MAN",
            destination_city_code=code,
            from_time=tomorrow,
            to_time=six_months_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: £{cheapest_flight.price}")

# ================== Send notification =================================
    if cheapest_flight.price != "N/A":
        if destination["lowestPrice"] > cheapest_flight.price:
            formatted_msg = (
                f"Low price alert! Only {cheapest_flight.price} to fly from "
                f"{cheapest_flight.origin_airport} to "
                f"{cheapest_flight.destination_airport}, "
                f"on {cheapest_flight.out_date} to "
                f"{cheapest_flight.return_date}"
            )
            destination["lowestPrice"] = cheapest_flight.price
            notification_manager = NotificationManager()
            notification_manager.send_message(formatted_msg)

# data_manager.destination_data = sheet_data
# data_manager.update_prices()
