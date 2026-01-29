Weather Rain Alert SMS

Description

This project checks the weather forecast using the OpenWeather API and sends an SMS notification using Twilio if rain is predicted within the next 12 hours. It is designed as a simple automation project to demonstrate API usage, environment variables, and third-party service integration in Python.



Key Features

Checks upcoming weather forecast data
Detects rain based on weather condition codes
Sends an automated SMS notification to a mobile phone
Uses environment variables to keep credentials secure
Designed to run locally or via GitHub Actions



Technologies Used

Python
Requests
Twilio API
OpenWeather API
Environment Variables



How it Works (Code Overview)

load_dotenv() → loads environment variables from a local .env file

requests.get() → retrieves weather forecast data from the OpenWeather API

response.json() → converts API response into Python data

loop through forecast → checks weather condition IDs for rain

Client() → creates a Twilio client using secure credentials

messages.create() → sends SMS alert if rain is detected



Setup

Clone the repository

Create a .env file in the project root with the following variables:

TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN
FROM_NUMBER
TO_NUMBER
OWM_API_KEY

Install dependencies:

pip install requests twilio python-dotenv

Run the script:

python main.py



Notes

The .env file is excluded from version control to prevent leaking private credentials.
For automated runs in GitHub Actions, credentials should be stored as repository secrets instead.
