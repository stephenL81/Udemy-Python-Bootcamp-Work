Day 19 - Etch a Sketch Project Readme

Description:
This is a Turtle graphics program that allows users to control a turtle on the screen using keyboard inputs. The program listens for specific key presses and moves the turtle forward, backward, or changes its direction accordingly. The turtle can also be reset to the center of the screen by pressing the 'c' key. This project is a good example of using higher-order functions and key bindings in Turtle graphics.

How to Run:
Run the script:python main.py

Once the script runs, use the following keys to control the turtle:

Up: Move the turtle forward.
Down: Move the turtle backward.
Left: Turn the turtle left.
Right: Turn the turtle right.
'c': Reset and center the turtle.
Click on the screen to exit when done.

How It Works (Code Overview):
move_forward() → Moves the turtle forward by 10 units.
move_backward() → Moves the turtle backward by 10 units.
turn_left() → Rotates the turtle left by 10 degrees.
turn_right() → Rotates the turtle right by 10 degrees.
center_and_reset() → Resets the turtle to the center of the screen.
screen.onkey() → Binds a specific key press to a function that moves or resets the turtle.
screen.listen() → Makes the screen listen for key events.

Key Features:
Uses keyboard input to control the turtle's movement.
Implements higher-order functions by passing functions as arguments to the onkey() method.
Allows for real-time interaction with the program via keyboard events.
