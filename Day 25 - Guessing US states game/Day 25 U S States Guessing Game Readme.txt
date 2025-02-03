Day 25 - U.S States Guessing Game Readme

Description:
This is a U.S. States quiz game where the player is asked to name the U.S. states on a map. As the player types the name of the state, the program checks if the answer is correct and places the state's name on the map. When the player types "Exit", the names of the states that were not guessed correctly are saved to a CSV file for later review. The game continues until all 50 states have been guessed correctly.

How to Run:
Run the script:python main.py
Start the game: The game will display a blank U.S. map.
Guess a state: Type the name of a U.S. state.
If correct, the state's name will be written on the map at the correct location.
If you want to quit, type "Exit", and the names of the states you haven't guessed yet will be saved in a states_to_learn.csv file.
Once all 50 states are guessed correctly, the game will congratulate you and end.

How It Works (Code Overview):
main.py → The entry point for the game:
Displays the blank U.S. states map and handles user input for guessing state names.
Checks if the guessed state is correct using the correct_guess function.
Displays the name of the state on the map at the correct coordinates.
Tracks the player's score and ends the game once all states are guessed correctly.
correct_guess function → Checks if the guessed state is correct and not already guessed:
The function returns True if the guessed state is valid and hasn't been guessed yet.
If the user types "Exit", it saves the remaining unguessed states to a CSV file.
pandas → Handles reading the U.S. states data from a CSV file:

The CSV file 50_states.csv contains the names and coordinates of all the U.S. states.
The coordinates are used to display the state's name at the correct location on the map.
turtle → Displays the U.S. map and writes the names of correctly guessed states:
The turtle module is used to draw and display the map and text on the screen.

Key Features:
Interactive: The player types the state names to guess their location on the map.
Tracks progress: Displays the score and number of correct guesses.
Persistence: Saves the states that the player hasn't guessed yet in a CSV file for later review.
Game completion: The game ends once all 50 states are guessed correctly, and a congratulatory message is displayed.
