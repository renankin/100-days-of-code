import os
import requests

APP_KEY = os.environ.get("APP_KEY")
APP_ID = os.environ.get("APP_ID")
WEIGHT_KG = 78
HEIGHT_CM = 177
AGE = 34
GENDER = "male"

headers = {
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

response = requests.post(url=nat_lang_endpoint, json=exercise_params,
                         headers=headers)
print(response.json())
