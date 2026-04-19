from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

email_address = os.getenv('MY_EMAIL')
email_password = os.getenv('MY_PASSWORD')

url = "https://appbrewery.github.io/instant_pot/"

target = 100

header = {"user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36","Accept-Language":"en-GB"}

response = requests.get(url=url,headers=header)
soup = BeautifulSoup(response.text, "html.parser")
price_dollars = soup.find(name="span", class_="a-price-whole").text.strip()
price_cents = soup.find(name="span", class_="a-price-fraction").text.strip()
price = f"{price_dollars}{price_cents}"
float_price = float(price)

if float_price < float(target):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_address,password=email_password)
        connection.sendmail(
            from_addr=email_address,
            to_addrs="stephenlancaster23@gmail.com",
            msg=f"Subject:Price Alert!!\n\nThat thing that you want is now ${float_price}"
        )
        print("email sent")