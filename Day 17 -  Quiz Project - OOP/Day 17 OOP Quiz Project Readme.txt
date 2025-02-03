Day 17 - OOP Quiz Project

Description:
This is a True/False quiz game that asks the player a series of questions and keeps track of their score. The game pulls random trivia questions from a dataset and presents them one by one. The player enters "True" or "False" for each question, and at the end, the total score is displayed.

How to Play:
Run the script:python main.py
The game will display a True/False question.
Type "True" or "False" and press Enter.
If correct, you gain a point; if incorrect, the correct answer is shown.
The game continues until all questions are answered.
At the end, your final score is displayed.

How It Works (Code Overview):
data.py → Stores the quiz questions and answers in a dictionary.
question_model.py → Defines the Question class, which stores question text and answer.
quiz_brain.py → Manages the quiz logic:
Keeps track of the current question number.
Asks the user for input.
Checks if the answer is correct and updates the score.
main.py → The entry point of the program:
Loads the questions into a list.
Runs the quiz loop until all questions are answered.

Key Features:
Uses Object-Oriented Programming (OOP) for better structure.
Can be easily expanded with more questions or different question types.
Keeps track of score and displays a final result.
