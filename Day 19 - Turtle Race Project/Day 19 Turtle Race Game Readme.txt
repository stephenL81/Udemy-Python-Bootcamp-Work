Day 19 - Turtle Race Game Readme

Description:
This is a Turtle Race Game where the player bets on which turtle will win the race. Six turtles are placed on the screen, and the player guesses which one will cross the finish line first. Each turtle moves randomly forward with the goal of reaching the finish line. The game will announce whether the player’s guess was correct or not after the race is over.

How to Run:
Run the script:python main.py
The game will ask you to make a bet: Choose the color of the turtle you think will win the race.
The turtles will race, and the screen will update as they move.
After the race ends, the game will announce whether your bet was correct or not.
Click on the screen to exit when done.

How It Works (Code Overview):
turtle.Terminator → Handles the case where the turtle graphics window is closed manually, preventing the program from crashing.
for turtle_index in range(0, 6): → Creates 6 turtles, each with a unique color, and places them at different vertical positions.
user_bet → Prompts the user to input their bet on the winning turtle color.
is_race_on → A flag that controls the race loop, which keeps running as long as no turtle has crossed the finish line.
rand_distance → Randomly moves each turtle forward by a random distance.
screen.exitonclick() → Waits for a click on the screen to close the turtle window after the race is finished.

Key Features:
Allows the player to bet on which turtle will win.
Uses random movement to simulate a race.
Displays the winner and whether the player's bet was correct.
Handles window closure with error handling for a smooth user experience.


