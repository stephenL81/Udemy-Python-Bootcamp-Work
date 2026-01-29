Day 22 - Pong Game Project Readme

Description:
This is a Pong game built using Python's Turtle graphics library. The player controls two paddles, one on the left and one on the right, using the keyboard. The objective is to prevent the ball from passing your paddle and try to score points by having the ball pass the opponent's paddle. The game tracks the score for both players and displays it at the top of the screen.

How to Run:
Run the script:python main.py
Control the paddles:
Right Paddle: Use the Up and Down arrow keys.
Left Paddle: Use the 'w' (up) and 's' (down) keys.
The ball will bounce off the top and bottom walls, and players must try to bounce it past the opponent's paddle to score a point.
The game continues until a player reaches a certain score.
Click on the screen to exit when done.
How It Works (Code Overview):
Paddle class (paddle.py) → Defines the paddle's appearance and movement:

Controls the paddle's position and allows it to move up or down.
The paddles are created at fixed positions on the left and right sides of the screen.
Ball class (ball.py) → Defines the ball's movement and interaction with paddles:

The ball moves continuously in a diagonal direction.
When it hits the top or bottom wall, it bounces off.
The ball bounces off the paddles when it comes into contact with them.
If the ball crosses the screen boundary (left or right), the score is updated and the ball resets to the center.
Scoreboard class (scoreboard.py) → Displays and updates the score:

Keeps track of the score for both the left and right players.
Updates the score whenever the ball crosses the left or right boundary.
Main script (main.py) → Orchestrates the game flow:

Initializes the game by creating paddle, ball, and scoreboard objects.
Sets up the screen and listens for user inputs (keyboard events).
Runs the game loop where the ball moves, checks for collisions, and updates the score.
Key Features:
Uses Turtle graphics for the game's graphics.
Allows for real-time keyboard input to control the paddles.
Keeps track of the score and updates it as the game progresses.
Implements collision detection between the ball and paddles, as well as wall bounces.


