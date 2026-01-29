Day 24 - Updated Snake Project With Scoreboard readme

Description:
This is a classic Snake Game where the player controls a snake that grows longer as it eats food. The player needs to avoid colliding with the walls or the snake's own body. The game keeps track of the score and saves the highest score to a file for persistence. When the game resets, the score is cleared, but the highest score remains saved.

How to Run:
Run the script:python main.py
Control the snake:Use the Up, Down, Left, and Right arrow keys to move the snake.
The snake moves, and every time it eats food, it grows longer.
The goal is to avoid colliding with the walls and the snake's body.
When the snake collides with either, the game resets, and the score is updated if it's higher than the previous high score.
The high score is saved to data.txt so it persists across game sessions.
How It Works (Code Overview):
snake.py (Snake Class) → Models the snake and its movements:

The snake starts with three segments and grows as it eats food.
The snake moves continuously, and the direction is controlled by arrow keys.
Collisions with walls or the snake's body reset the game.
food.py (Food Class) → Models the food that the snake eats:

The food randomly appears at different positions on the screen.
When the snake eats the food, it grows, and the score increases.
scoreboard.py (Scoreboard Class) → Tracks and displays the score and high score:

The scoreboard shows the current score and the highest score.
When the game resets, the score is reset to zero, and the high score is updated if the new score is higher.
The high score is saved to a file (data.txt) for persistence.
data.py → Handles reading and writing of the high score:

Reads the high score from data.txt at the start of the game.
Writes the new high score to data.txt when a new high score is achieved.
main.py (Main Game Loop) → Orchestrates the game:Initializes the snake, food, scoreboard, and handles user input.
Runs the game loop where the snake moves, eats food, and checks for collisions.
Updates the scoreboard and handles resetting the game when needed.

Key Features:
Tracks the current score and high score.
High score persistence: The high score is saved to a file and remains between game sessions.
Game reset: The game resets when the snake collides with the wall or itself, and the score is updated if necessary.
Responsive controls: The player can control the snake's movement using the arrow keys.

