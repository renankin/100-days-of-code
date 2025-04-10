import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# https://www.webfx.com/web-development/glossary/http-status-codes/
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
#
# print(iss_position)

MY_LAT = 28.538336
MY_LONG = -81.379234

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json",
                        params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# print(json.dumps(data, indent=4))
print(sunrise)

time_now = datetime.now()

print(time_now.hour)
