import requests
from datetime import datetime

APP_ID = "9867fe3a"
APP_KEY = "bb29337ece0a86dfc9f71e365d0ef983"

header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0",
}

AGE = 22
GENDER = "male"
WEIGHT = 65
HEIGHT = 100
query = input("What did you do? ")

exercise_endpoints = "https://trackapi.nutritionix.com/v2/natural/exercise"
body = {
    "exercise": {
        "query": query,
        "gender": GENDER,
        "weight_kg": WEIGHT,
        "height_cm": HEIGHT,
        "age": AGE,
    }
}

response = requests.post(url=exercise_endpoints, json=body, headers=header)
result = response.json()

today = datetime.now()
formatted_date = today.strftime("%d%m%Y")
formatted_time = today.strftime("%I:%M %p")

sheety_url = "https://api.sheety.co/cd25bffb434ffa9714c3610ed74dbb3b/workoutTracking/workouts"

for exercise in result["exercise"]:
    sheet_inputs = {
        "workout": {
            "date": formatted_date,
            "time": formatted_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories",]
        }
    }

    sheet_response = requests.post(sheety_url, json=sheet_inputs)
    print(sheet_response.text)
