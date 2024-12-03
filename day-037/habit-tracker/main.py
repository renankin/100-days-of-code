import requests
from datetime import datetime

USERNAME = "renankin"
TOKEN = "aue84orjhf239ljjh"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "aue84orjhf239ljjh",
    "username": "renankin",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config,
#                          headers=headers)
# print(response.text)

today = datetime.now().strftime("%Y%m%d")

pixel_entry = {
    "date": today,
    "quantity": input("How many km did you cycle today? "),
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

response = requests.post(url=pixel_creation_endpoint, json=pixel_entry,
                         headers=headers)
print(response.text)

update_endpoint = (
    f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
)
new_pixel_data = {
    "quantity": "20"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data,
#                         headers=headers)
# print(response.text)

delete_endpoint = (
    f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
)

# response = requests.delete(
#     url=delete_endpoint, headers=headers)
# print(response.text)
