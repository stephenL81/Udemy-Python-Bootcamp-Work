Day 12 - Number Guessing Game Readme

Description:
This is a simple number guessing game where the player must guess a randomly selected number between 1 and 100. The player can choose between two difficulty levels, which determine the number of attempts they have to guess the correct number.

How to Play:
Run the script: python main.py
The game will generate a random number between 1 and 100.
Choose a difficulty level: 'easy' gives 10 attempts, 'hard' gives 5 attempts.
Enter a number as your guess.
The game will tell you if your guess is too high, too low, or correct.
If you run out of attempts before guessing correctly, you lose.
If you guess correctly, you win!

How It Works (Code Overview):
random.randint() → Generates a random number between 1 and 100.
if input("Choose a difficulty...") → Sets the number of attempts based on difficulty.
while loop → Runs the game until the player guesses correctly or runs out of attempts.
if-elif statements → Checks if the guess is too high, too low, or correct.

Key Features:
A simple text-based game with interactive input.
Difficulty levels to adjust the challenge.
Randomized number selection for replayability.
Feedback on each guess to guide the player.
