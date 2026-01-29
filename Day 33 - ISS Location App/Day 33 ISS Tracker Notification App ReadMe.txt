Day 33 -ISS Tracker & Notification System

Overview
This project tracks the position of the International Space Station (ISS) and checks whether it is currently visible in the sky. It also determines if it's nighttime at the user's location. If both conditions are met, the program sends an email notification, reminding the user to look up and spot the ISS.

Features
Fetches real-time ISS position data from the Open Notify API.
Determines if the ISS is within a set proximity to the user's location.
Checks the current sunrise and sunset times using the Sunrise-Sunset API.
Sends an email notification when the ISS is visible at night.
Runs continuously, checking every 60 seconds.

How it Works (Code Overview)
in_range() -> Checks if the ISS is within ±5 degrees of the user's latitude and longitude.
is_dark() -> Fetches local sunrise and sunset times to determine if it is currently nighttime.
while loop -> Runs continuously, checking ISS visibility every 60 seconds and sending an email alert if conditions are met.

Setup & Execution
Ensure you have the necessary Python libraries installed: pip install requests
Enter Your Location - Modify MY_LAT and MY_LONG with your actual latitude and longitude.
Configure Email Settings: Replace my_email with your actual email address.Generate an App Password (if using Gmail) and replace password with it. Modify the smtplib.SMTP settings if using a different email provider.
Run the Script: python main.py

Notes
The script runs continuously and checks for ISS visibility every 60 seconds.
Make sure to enable "Less secure apps" or use an app password if using Gmail.
Ensure you have an active internet connection for API requests.


