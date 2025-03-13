Day 32 - Birthday Email Automation App ReadMe

Overview

This Python script automates the process of sending personalized birthday emails. It reads a CSV file containing birthday details, selects the appropriate recipient based on the current date, and sends a randomly chosen birthday message from a set of pre-written templates.

Features
Reads birthday details from a CSV file.
Checks if today matches any birthdays in the file.
Selects a random birthday message tempate.
Replaces placeholders in the template with the recipient's name.
Sends an automated birthday email using SMTP.

How it Works (Code Overview)
Reads Data: The script loads birthday details from birthdays.csv.
Checks Dates: It compares today's date with the birthdays in the file.
Selects Template: If a match is found, it picks a random letter template from letter_templates/.
Personalizes Message: The placeholder [NAME] is replaced with the recipient's actual name.
Sends Email: Uses smtplib to send the email via an SMTP server.

Requirements
Python 3.x
Required libraries: smtplib, pandas, datetime, random
A valid email account (e.g., Gmail) with an app-specific password

Setup & Execution
Enter Email Credentials:
Replace my_email with your sender email address.
Replace my_password with your email app password.
Prepare the Birthday List:
Populate birthdays.csv with names, emails, and birth dates.
Run the Script:
python main.py

Notes
Ensure your email provider allows SMTP access.
Use an app-specific password for security.
The script will only send an email if a birthday matches today’s date.
The letter_templates/ folder should contain letter templates with the [NAME] placeholder.
