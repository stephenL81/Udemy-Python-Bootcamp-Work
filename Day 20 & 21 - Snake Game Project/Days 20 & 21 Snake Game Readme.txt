Days 20 & 21 - Snake Game Project Readme

Description:
This is a Snake game where the player controls a snake that moves around the screen to collect food. Each time the snake eats the food, it grows longer and the score increases. The game ends if the snake collides with the wall or its own tail. The game is displayed using Turtle graphics, and the score is shown at the top of the screen.

How to Run:
Run the script:python main.py
Use the arrow keys to control the snake’s movement:

Up: Move the snake up.
Down: Move the snake down.
Left: Move the snake left.
Right: Move the snake right.
The snake will grow each time it eats food, and the score will increase.
The game ends when the snake collides with the wall or its own tail.
Click on the screen to exit when done.
How It Works (Code Overview):
Food class (food.py) → Creates the food object and randomly places it on the screen.
Snake class (snake.py) → Manages the snake's creation, movement, and growth:

Creates the initial snake segments.
Moves the snake by updating each segment’s position.
Controls the direction of the snake using the arrow keys.
Extends the snake when it eats food.
Scoreboard class (scoreboard.py) → Displays and updates the score:
Initializes the score at the top of the screen.
Increases the score when the snake eats food.
Displays "GAME OVER" when the game ends.
Main script (main.py) → Orchestrates the game by creating instances of the Snake, Food, and Scoreboard classes, running the game loop, and handling user input.
Key Features:
Uses Turtle graphics for real-time drawing of the game.
Keeps track of the score and updates it as the snake eats food.
Detects collisions with the wall and tail to end the game.
Handles keyboard input to control the snake's movement.
