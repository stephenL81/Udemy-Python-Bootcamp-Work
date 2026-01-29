Day 30 - Password Manager - Updated with JSON, Error Handling, and Search Function

Overview
This updated Password Manager application allows users to securely store, generate, and search for website login credentials. The data is saved in a JSON file, offering a more structured format for storing passwords. The app includes error handling to ensure smooth operation, and users can now search for and copy passwords from the saved entries.

Features
Password Generation: Generate secure, random passwords with letters, numbers, and symbols.
Store Login Details: Save website login details (email/username and password) in a JSON file.
Search Functionality: Search for stored credentials by website name, and easily copy passwords to the clipboard.
Error Handling: Includes checks for missing data and handles cases where the data file doesn't exist yet.
Clipboard Integration: Automatically copies the generated password or the retrieved password to the clipboard.

How it Works (Code Overview)
generate_password() -> Generates a random, secure password and inserts it into the password entry field. Copies the password to the clipboard.
save() -> Saves the entered website, email/username, and password in a data.json file. If the file doesn't exist, it creates one.
find_password() -> Searches for a website's credentials in the data.json file. If found, prompts the user to copy the password to the clipboard.
Entry() -> Accepts user input for the website, email/username, and password.
Label() -> Displays text labels for each input field (Website, Email/Username, Password).
Button() -> Triggers actions like password generation, saving data, and searching for passwords.
messagebox.askokcancel() -> Prompts the user to confirm actions, such as saving new credentials or copying a password.
window.mainloop() -> Runs the GUI and keeps the application open and interactive.

Usage
Enter the website name in the "Website" field.
Enter your email/username for the website.
Either generate a secure password by clicking "Generate Password" or enter your own.
Click "Add" to save the credentials, or click "Search" to retrieve and copy the password for an existing website.

Requirements
Python 3.x
Tkinter (included with standard Python installation)
pyperclip (install with pip install pyperclip)
JSON (included in the standard Python library)

Setup & Execution
Ensure Python is installed on your machine.
Install the required pyperclip library using:
pip install pyperclip
Save the script as main.py.
Run the script:
python main.py
The graphical user interface will appear, allowing you to manage your passwords.

Notes
Passwords are saved in data.json. If the file doesn't exist, it will be created.
The password generator creates a password of 8-10 characters, with 2-4 numbers and symbols each.
Be aware that data.json contains passwords in plain text. Consider implementing encryption for enhanced security in future versions.
If the data file is missing or corrupted, the app will alert you with a message box.
You can search for saved credentials by entering a website name and clicking the "Search" button.
