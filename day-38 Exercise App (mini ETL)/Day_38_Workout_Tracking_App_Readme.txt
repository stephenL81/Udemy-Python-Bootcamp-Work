Day 37 - Workout Tracking App Readme

Description:
This is a workout tracking app that uses API calls to automatically log exercise data to a Google Sheet. The app follows an ETL (Extract, Transform, Load) pattern - it extracts exercise data from an API, transforms it into a structured format, and loads it into a Google Sheet. The user inputs a natural language description of their exercise (e.g. "ran for 5 mins"), and the app uses a nutrition/exercise API to calculate the duration and calories burned. It then posts this data along with the current date and time to a Google Sheet via the Sheety API.

How to Run:
1. Install required dependencies:
   pip install requests python-dotenv

2. Set up your .env file:
   Create a file named .env in the same directory as main.py with the following variables:
   APP_ID=your_nutritionix_app_id
   API_KEY=your_nutritionix_api_key
   SHEETY_ENDPOINT=your_sheety_endpoint_url
   SHEETY_AUTHORISATION=your_sheety_bearer_token

   IMPORTANT: Never commit your .env file to GitHub. Make sure .env is in your .gitignore file.

3. Sign up for free accounts:
   - 100 Days of Python Exercise API (course specific): https://app.100daysofpython.dev
   - Sheety (for Google Sheets API): https://sheety.co

4. Set up your Google Sheet:
   - Create a Google Sheet with the following column headers: Date, Time, Exercise, Duration, Calories
   - Share the sheet so "Anyone with the link" can edit
   - Connect the sheet to Sheety and copy the endpoint URL to your .env file
   - Set up Bearer token authentication in Sheety and add the token to your .env file

5. Run the script:
   python main.py

6. When prompted, enter your exercise in natural language:
   e.g. "ran for 5 mins" or "cycled for 30 minutes"

How It Works (Code Overview):
main.py → The main program that handles exercise tracking and data logging:
- Takes natural language exercise input from the user
- Makes a POST request to the exercise API with the user's input and personal stats (gender, weight, height, age)
- Extracts the exercise name, duration, and calories burned from the API response
- Makes a POST request to Sheety to log the data to Google Sheets along with the current date and time

API integrations:
- Exercise API: Processes natural language exercise descriptions and returns calculated exercise data including duration and calories burned
- Sheety API: Acts as a bridge between the app and Google Sheets, allowing data to be written directly to a spreadsheet via API calls

Environment variables (dotenv) → Securely stores API keys and credentials:
- Keeps sensitive information out of the source code
- Loaded from a .env file that should never be committed to version control

Key Features:
- Natural language input: Understands exercise descriptions written in plain English
- Automatic calculations: Calculates duration and calories burned based on personal stats
- Google Sheets integration: Automatically logs workout data to a Google Sheet
- Timestamping: Automatically records the date and time of each workout
- Secure credentials: Uses environment variables to protect API keys and tokens
- Bearer token authentication: Sheety API is protected with Bearer token authentication