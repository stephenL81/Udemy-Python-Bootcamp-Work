Day 36 - Stock Trading News Alert Readme

Description:
This is a stock trading news alert system that monitors Tesla (TSLA) stock price changes and sends SMS notifications when significant price movements occur. The program uses API calls to fetch stock data and news articles. It compares yesterday's closing price with the day before yesterday's closing price. If the stock price changes by 5% or more (either up or down), it fetches the latest Tesla-related news articles and sends SMS alerts via Twilio with headlines and article links.

How to Run:
1. Install required dependencies:
   pip install requests twilio python-dotenv

2. Set up your .env file:
   Create a file named .env in the same directory as main.py with the following variables:
   FROM_NUMBER=your_twilio_phone_number
   TO_NUMBER=your_personal_phone_number
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   STOCK_API_KEY=your_twelvedata_api_key
   NEWS_API_KEY=your_newsapi_key

   IMPORTANT: Never commit your .env file to GitHub. Add .env to your .gitignore file.

3. Sign up for free API accounts:
   - Twelve Data (for stock prices): https://twelvedata.com/
   - News API (for news articles): https://newsapi.org/
   - Twilio (for SMS): https://www.twilio.com/

4. Run the script:
   python main.py

How It Works (Code Overview):
main.py → The main program that coordinates stock monitoring and SMS alerts:
- Fetches the last 3 days of Tesla stock data from Twelve Data API
- Compares yesterday's closing price with the day before yesterday's closing price
- Calculates if there's a 5% or greater price change
- If price changed by 5%+, fetches the top 3 Tesla-related news articles from News API
- Sends SMS alerts via Twilio with the stock movement direction (🔺 for up, 🔻 for down), headline, and article URL

up_or_down() function → Determines if the stock went up or down:
- Compares yesterday's price to the day before yesterday's price
- Returns an up arrow emoji (🔺) if price increased, down arrow (🔻) if decreased

API integrations:
- Twelve Data API: Provides daily stock price data for Tesla (TSLA)
- News API: Fetches recent Tesla-related business news articles
- Twilio API: Sends SMS messages to your phone

Environment variables (dotenv) → Securely stores API keys and credentials:
- Keeps sensitive information out of the source code
- Loaded from a .env file that should never be committed to version control

Key Features:
- Automated monitoring: Checks Tesla stock price changes automatically
- Smart alerts: Only sends notifications when price changes by 5% or more
- News integration: Provides relevant news context for significant price movements
- SMS notifications: Delivers alerts directly to your phone via Twilio
- Secure credentials: Uses environment variables to protect API keys
- Error handling: Includes try/except blocks to handle message sending failures gracefully

Notes:
- Twilio trial accounts have character limits per SMS. Headlines are truncated to 40 characters to stay within limits.
- Free tier API limits: Twelve Data allows 800 calls/day, News API varies by plan, Twilio trial has daily SMS limits.
- The program currently monitors Tesla (TSLA) but can be modified to track any stock symbol.