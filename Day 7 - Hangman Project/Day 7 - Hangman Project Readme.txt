Description:
The Hangman Game is a word-guessing game where the player has to guess the correct word by suggesting letters. If the player makes too many incorrect guesses, the game ends. The game tracks incorrect guesses and displays the current state of the word with underscores for unguessed letters. The player has six chances to guess the correct word.

How to Play:
Run the script:python main.py

Game Starts:
The player is prompted to guess letters of a word.
For every wrong guess, a part of the hangman is drawn.

Incorrect Guesses:
If the player guesses a letter incorrectly, the number of lives decreases and the hangman drawing progresses.

Correct Guesses:
If the guessed letter is in the word, the word display is updated to show the guessed letters.

Game Over:
The game ends when the player guesses all letters correctly or loses all their lives.

Win or Loss:
If the player guesses all letters before running out of lives, they win! Otherwise, the game ends in a loss.

How It Works (Code Overview):

hangman_art.py
Stores the stages of the hangman and the game's logo as ASCII art.

hangman_words.py
Contains a list of random words for the player to guess.

main.py
Contains the main game logic:
The player is asked for input and the game proceeds.
If the player's guess is correct, the word is updated.
Incorrect guesses decrease the number of lives and display the hangman stages.
If the player guesses the word or loses all lives, the game ends.

Key Features:
Displays an ASCII art hangman that progresses with incorrect guesses.
Tracks the player's remaining lives and updates the game state.
Checks if the player has guessed the word correctly or made too many incorrect guesses.
Uses a random word list for varied gameplay.
