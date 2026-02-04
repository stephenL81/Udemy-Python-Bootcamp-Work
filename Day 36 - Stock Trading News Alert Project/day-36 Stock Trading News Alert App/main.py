import requests
import datetime as dt
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

from_number=os.getenv("FROM_NUMBER")
to_number=os.getenv("TO_NUMBER")
twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
stock_api_key = os.getenv("STOCK_API_KEY")
news_api_key= os.getenv("NEWS_API_KEY")

date = dt.date.today()

def up_or_down():
    diff = yesterday_price - day_before_price
    if diff > 0:
        return "🔺+5%"
    else:
        return "🔻+5%"

stock_endpoint = "https://api.twelvedata.com/time_series?"
stock_parameters={
    "apikey":stock_api_key,
    "interval": "1day",
    "symbol": "TSLA",
    "outputsize": 3,
}

news_endpoint = "https://newsapi.org/v2/top-headlines?"
news_parameters = {
    "apiKey": news_api_key,
    "country": "us",
    "category": "business",
    "pagesSize": 3,
    "q": "Tesla",
    "searchin": "title",
    "from": date,
}

stock_response = requests.get(stock_endpoint,params=stock_parameters)
stock_response.raise_for_status()
data = list(stock_response.json()["values"])
yesterday_price=float(data[1]["close"])
day_before_price=float(data[2]["close"])
positive_diff=abs(yesterday_price - day_before_price)
five_percent = yesterday_price * 0.05
if positive_diff >= five_percent:

    news_response = requests.get(news_endpoint,params=news_parameters)
    news = news_response.json()
    articles = news["articles"]
    length = len(articles)

    client = Client(twilio_account_sid,twilio_auth_token)

    for item in articles:
        headline = item['title'][:40]

        try:
            message = client.messages.create(
            body=f"TSLA: {up_or_down()}\nHeadline: {headline}...\nArticle: {item['url']}\n",
            from_=from_number,
            to=to_number,
            )
            print(f"Sent successfully: {message.sid}")
        except Exception as e:
            print(f"failed to send message: {e}")