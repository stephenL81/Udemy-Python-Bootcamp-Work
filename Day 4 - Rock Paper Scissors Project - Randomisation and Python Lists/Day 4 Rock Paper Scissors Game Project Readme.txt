Day 4 - Rock, Paper, Scissors Game Project Readme

Description:
This is a simple text-based version of the classic game Rock, Paper, Scissors. The player chooses one of the three options, and the computer randomly selects its own option. The game then compares the choices and displays the outcome, determining whether the player wins, loses, or ties.

How to Play:
Run the script:python main.py
User Choice: Type "0" for Rock, "1" for Paper, or "2" for Scissors, then press Enter.
Computer Choice: The computer randomly selects one of the three options.
Outcome: The game compares the user's and computer's choices and displays whether the player won, lost, or tied.

How It Works (Code Overview):
User Input:
The program asks the user to choose Rock, Paper, or Scissors by entering the corresponding number (0 for Rock, 1 for Paper, or 2 for Scissors).

Random Choice for Computer:
The computer selects a random choice from the available options using random.randint().

Game Logic:
The program compares the user's choice and the computer's choice using a series of if and elif statements to determine the outcome: win, lose, or draw.

Key Features:
Randomized computer choice.
Simple decision-making logic for determining the winner.

