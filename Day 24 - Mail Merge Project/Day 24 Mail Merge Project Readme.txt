Day 24 - Mail Merge Project Readme

Description:
This script generates personalized letters for a list of names using a predefined letter template. Each letter is customized by replacing the placeholder [name] in the template with an individual name from the list. The personalized letters are then saved as separate .txt files in the specified output folder.

How to Run:
Run the script:python main.py
The script reads the list of names from Input/Names/invited_names.txt.
The letter template is read from Input/Letters/starting_letter.txt, where the placeholder [name] will be replaced with each name.
For each name, a new letter is created in the Output/ReadyToSend/ directory, with the filename format Letter_for_<name>.txt.
The letters are written with personalized content, and the [name] placeholder is replaced by the respective name.

How It Works (Code Overview):

Main script (main.py) → Orchestrates the letter generation:

Reads the list of names from the invited_names.txt file.
Reads the letter template from starting_letter.txt.
For each name, a new text file is created in the Output/ReadyToSend/ folder.
The placeholder [name] in the template is replaced with each name, and the letter is saved.
Input/Names/invited_names.txt → Contains the list of names:

One name per line, used to generate personalized letters.
Input/Letters/starting_letter.txt → Template for the letter:

The template includes a placeholder [name], which will be replaced with actual names from invited_names.txt.
Output/ReadyToSend/ → Directory for saving generated letters:
Each generated letter is saved as Letter_for_<name>.txt.

Key Features:
Reads a list of names and generates personalized letters for each name.
Customizes the letter by replacing the [name] placeholder with the respective name from the list.
Saves each personalized letter as a separate .txt file in the Output/ReadyToSend/ directory.
Simple, file-based input/output structure, with no dependencies other than Python.
