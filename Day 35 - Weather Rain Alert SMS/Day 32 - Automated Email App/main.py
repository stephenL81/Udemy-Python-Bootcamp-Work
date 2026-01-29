import smtplib
import pandas
import datetime as dt
from random import randint

my_email = "" #Enter senders email address here
my_password = "" #Enter the app password for the email address
data = pandas.read_csv("birthdays.csv")
today = dt.datetime.now()
birthday_today = ""

data_dict = data.to_dict(orient="records")
for item in data_dict:
    if item["day"]== today.day and item["month"] == today.month:
        birthday_today = (item["name"])
        birthday_email = (item["email"])

if birthday_today:
    with open(f"letter_templates/letter_{randint(1,3)}.txt") as letter_template:
        letter = letter_template.read()
        named_letter = letter.replace("[NAME]", birthday_today)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_email,
            msg=f"Subject: Happy Birthday!\n\n{named_letter}"
    )