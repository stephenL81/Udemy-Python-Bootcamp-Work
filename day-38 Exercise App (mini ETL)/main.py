import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_AUTHORISATION=os.getenv("SHEETY_AUTHORISATION")
SHEETY_ENDPOINT=os.getenv("SHEETY_ENDPOINT")
APP_ID=os.getenv("APP_ID")
API_KEY=os.getenv("API_KEY")

date = dt.date.today().strftime("%Y-%m-%d")
time = dt.datetime.now().strftime("%H:%M:%S")

GENDER = "male"
WEIGHT_KG = 82
HEIGHT_CM = 177
AGE = 44

#----------------POST REQUEST----------------------------------
base_url = "https://app.100daysofpython.dev"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_input = input("What exerecise did you do?: ")

post_url =f"{base_url}/v1/nutrition/natural/exercise/"

exercise_params = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
response = requests.post(url=post_url,headers=headers,json=exercise_params)
response.raise_for_status()
result = response.json()

exercise = result["exercises"][0]["name"]
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]


#-------------------------------------SHEETY POST-------------------------------------------------------
sheety_params ={
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SHEETY_AUTHORISATION}",
}

sheety_response = requests.post(SHEETY_ENDPOINT,json=sheety_params,headers=sheety_headers)
sheety_response.raise_for_status()
