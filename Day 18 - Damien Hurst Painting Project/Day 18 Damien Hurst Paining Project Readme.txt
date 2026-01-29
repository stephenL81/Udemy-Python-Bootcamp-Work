Day 18 - Damien Hurst Paining Project Readme

Description:
This is a Turtle graphics program that uses a list of RGB color values (extracted from an image) to create a colorful grid on the screen. The program simulates drawing with the turtle module and uses random colors from the list to draw a grid of dots. The colors are represented as RGB tuples, which are then converted into floats to display on the screen.

How to Run:
Run the script:python main.py
The program will open a window and draw a grid of colored dots using Turtle.
Click on the window to exit when done.

How It Works (Code Overview):
color_list → A list of RGB tuples that represent colors extracted from an image.
float_colour_list → A list comprehension that converts each RGB tuple from integers to floats for the turtle module.
Turtle Object Setup → Creates a turtle object (tim), which is responsible for drawing the grid.
change_direction() → Changes the turtle's direction to alternate between moving left to right and right to left.
move_down_row() → Moves the turtle to the next row after completing a row of dots.
draw_row() → Draws a single row of colored dots, choosing a random color from the float list.
draw_painting() → Combines the functions to draw the full grid of dots, alternating directions after each row.

Key Features:
Uses Turtle graphics for visual drawing of a grid.
Generates random colors from a list and applies them to the dots.
Implements functions to break down the drawing process: change direction, move down a row, and draw a row.
