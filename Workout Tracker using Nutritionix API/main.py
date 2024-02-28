import requests
from datetime import datetime

GENDER = "MALE"
WEIGHT = "68"
HEIGHT = "172"
AGE = "19"

sheety_endpoint = "https://api.sheety.co/cfece88ac87f148b8b2468929054f77d/myWorkouts/workouts"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Enter exercises you did today: ")

headers = {
    "x-app-id": "20894428",
    "x-app-key": "af520783be92759bcc7acc68bdbbf050"

}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=headers)

    print(sheet_response.text)



