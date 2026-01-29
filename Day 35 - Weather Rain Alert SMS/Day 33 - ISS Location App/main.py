import requests
from datetime import datetime
import smtplib
import time

my_email = "stephenpythontest2025@gmail.com"
password = "pwdx hvav fgwo uybk"

MY_LAT = 53.313171 # Your latitude
MY_LONG = -2.979611 # Your longitude

def in_range():#
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT + 5 > iss_latitude > MY_LAT -5:
        if MY_LONG + 5 > iss_longitude > MY_LONG - 5:
            return True

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()

    if time_now.hour <= sunrise or time_now.hour >= sunset:
        return True

while True:
    time.sleep(60)
    if is_dark() and in_range():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="Look Up!\n\nThe ISS is above you in the sky."
            )


