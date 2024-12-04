import os
import requests
from datetime import datetime


SHEET_TOKEN = os.environ.get("SHEET_TOKEN")
APP_KEY = os.environ.get("APP_KEY")
APP_ID = os.environ.get("APP_ID")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
WEIGHT_KG = 78
HEIGHT_CM = 177
AGE = 34
GENDER = "male"

app_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

nat_lang_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did today? ")

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(
    url=nat_lang_endpoint, json=exercise_params, headers=app_headers
)
result = response.json()


bearer_headers = {
    "Authorization": f"Bearer {SHEET_TOKEN}"
}

sheet_endpoint = SHEET_ENDPOINT

today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(
        url=sheet_endpoint, json=sheet_inputs, headers=bearer_headers
    )
    print(sheet_response.text)
