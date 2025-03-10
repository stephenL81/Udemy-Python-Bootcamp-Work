Day 31 - Flashcard Learning App

Overview
This is a flashcard-based learning application built using Tkinter. The app helps users learn French words by displaying a French word on a card, and after a short delay, flipping the card to reveal the English translation. Users can mark words as known, removing them from the learning list, or move to the next card to keep practicing.

Features
Displays a random French word and flips the card after 3 seconds to reveal the English translation.
Allows users to remove known words from the dataset to focus on new words.
Saves progress by storing remaining words in a CSV file.
Uses a visually appealing UI with images and dynamic updates.

How it Works (Code Overview)
next_card() -> Displays a new French word, resets the flip timer, and starts a 3-second countdown before flipping the card.
flip_card() -> Changes the card to display the English translation of the current word.
remove_word() -> Removes the current word from the learning list and updates the CSV file.
Canvas() -> Displays the card background, French word, and English translation.
Button() -> Two buttons allow users to mark words as known or skip to the next word.
try-except block -> Checks for an existing saved words file; if missing, it loads the full dataset.
window.after() -> Used to schedule the automatic flip of the card after 3 seconds.

Usage
Run the script to start the flashcard application.
The app will display a random French word on the card.
After 3 seconds, the card will flip to show the English translation.
Click the ❌ button to skip to the next word.
Click the ✅ button to mark the word as learned and remove it from the dataset.

Requirements
Python 3.x
Tkinter (included in standard Python library)
Pandas (install using pip install pandas)

Setup & Execution
Ensure Python is installed.
Install dependencies: pip install pandas
Place the french_words.csv file inside a data/ directory.
Save the script as main.py.
Run the script using:
python main.py

Notes
The app stores progress by saving the remaining words to words_to_learn.csv.
If words_to_learn.csv exists, it loads that file instead of the full dataset.
The card background changes dynamically between the front and back images.
