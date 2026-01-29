import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

from_number=os.getenv("FROM_NUMBER")
to_number=os.getenv("TO_NUMBER")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
if not account_sid or not auth_token:
    raise RuntimeError("Twilio credentials not loaded")

OWM_Endpoint ="https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "appid": os.getenv("OWM_API_KEY"),
    "lat": 53.313171,
    "lon": -2.979611,
    "cnt": 4,
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_conditions = weather_data["list"]

client = Client(account_sid, auth_token)
rain_expected = False

for item in weather_conditions:
    for weather in item["weather"]:
        if weather['id'] < 700:
            rain_expected = True
            break

if rain_expected:

    message = client.messages.create(
        body="It's going to rain today. Remember to take an ☂️",
        from_=from_number,
        to=to_number
    )

