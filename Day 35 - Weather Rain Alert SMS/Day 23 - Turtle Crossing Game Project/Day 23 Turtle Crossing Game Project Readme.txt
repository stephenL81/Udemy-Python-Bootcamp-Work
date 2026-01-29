Day 23 - Turtle Crossing Game Readme

Description:
This is a Turtle Crossing game where the player controls a turtle that must cross a busy road without getting hit by the moving cars. The game gets progressively harder as the turtle successfully crosses the road, with cars speeding up as the player levels up. The game continues until the player collides with a car, at which point the game ends and displays the final message.

How to Run:
Run the script:python main.py
Control the turtle:Use the Up arrow key to move the turtle forward.
The goal is to cross the road while avoiding the moving cars.
The speed of the cars increases every time the player successfully crosses the road.
The game ends when the turtle collides with a car.
Click on the screen to exit when done.

How It Works (Code Overview):
Player class (player.py) → Defines the player turtle and its movement:
The player starts at the bottom of the screen and can move up using the Up arrow key.
If the player reaches the finish line, they return to the start, and the level increases.
If the player collides with a car, the game ends.
CarManager class (car_manager.py) → Manages the creation and movement of cars:
Creates new cars at random intervals and moves them across the screen from right to left.
Increases the speed of the cars each time the player successfully crosses the finish line.
Scoreboard class (scoreboard.py) → Tracks and displays the score and level:

Displays the current level at the top of the screen.
Increases the level each time the player reaches the finish line.
Displays "GAME OVER" when the player collides with a car.
Main script (main.py) → Orchestrates the game flow:

Initializes the game by creating instances of the Player, CarManager, and Scoreboard classes.
Runs the game loop where the player moves, cars are created and moved, and collisions are detected.

Key Features:
Uses Turtle graphics for the game's visual display.
Keeps track of the level and increases the difficulty by speeding up the cars.
Detects collisions between the player and the cars, ending the game when they collide.
Implements real-time keyboard input to control the player's movement.
