class FlightData:

    def __init__(self, data):
        """
        Constructor for initializing a new flight data instance by parsing
        a flight data received from the Amadeus API. If no valid flight data
        is found it returns arguments with "N/A", otherwise its attribute
        will correspond to the first flight found.

        Parameters:
            data (dict): The JSON data containing flight information returned
            by the API.
        """
        self.data = data
        if self.is_data_valid():
            first_flight = self.data[0]
            self.price = float(first_flight["price"]["grandTotal"])
            self.origin_airport = first_flight["itineraries"][0][
                "segments"][0]["departure"]["iataCode"]
            self.destination_airport = first_flight["itineraries"][0][
                "segments"][0]["arrival"]["iataCode"]
            self.out_date = first_flight["itineraries"][0][
                "segments"][0]["departure"]["at"].split("T")[0]
            self.return_date = first_flight["itineraries"][1][
                "segments"][0]["departure"]["at"].split("T")[0]

    def is_data_valid(self):
        """
        Checks if the data from the Amadeus API contains valid flight
        entries and updates the class attributes with "N/A" if it does. If not
        returns True.
        """
        if self.data is None or not self.data:
            self.price = "N/A"
            self.origin_airport = "N/A"
            self.destination_airport = "N/A"
            self.out_date = "N/A"
            self.return_date = "N/A"
        else:
            return True

    def find_cheapest_flight(self):
        """
        Finds the cheapest flight within the available options from the
        Amadeus API flights if the data is valid and updates object attributes
        with the cheapest flight.
        """
        if self.is_data_valid():
            for flight in self.data:
                price = float(flight["price"]["grandTotal"])
                if price < self.price:
                    self.price = float(flight["price"]["grandTotal"])
                    self.origin_airport = flight["itineraries"][0][
                        "segments"][0]["departure"]["iataCode"]
                    self.destination_airport = flight["itineraries"][0][
                        "segments"][0]["arrival"]["iataCode"]
                    self.out_date = flight["itineraries"][0][
                        "segments"][0]["departure"]["at"].split("T")[0]
                    self.return_date = flight["itineraries"][1][
                        "segments"][0]["departure"]["at"].split("T")[0]
