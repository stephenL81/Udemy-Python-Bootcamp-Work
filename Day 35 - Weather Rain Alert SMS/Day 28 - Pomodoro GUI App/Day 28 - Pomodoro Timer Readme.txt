Day 30 - Pomodoro Timer Readme

Overview
This is a simple Pomodoro Timer built using Tkinter. The Pomodoro technique helps improve productivity by breaking work into intervals, typically 25 minutes in length, separated by short breaks. This application provides an easy-to-use graphical interface for managing work and break sessions.

Features
Implements the Pomodoro technique with work, short break, and long break intervals.
Displays a countdown timer that updates dynamically.
Uses visual indicators such as color-coded labels to differentiate work and break sessions.
Tracks completed work sessions and displays checkmarks (✔) as progress indicators.
Provides start and reset buttons to control the timer.

How it Works (Code Overview)
start_timer() -> Initiates the timer, alternating between work and break intervals.
count_down(count) -> Handles the countdown logic and updates the timer display.
reset_timer() -> Stops the timer and resets all values to default.
Canvas() -> Displays the Pomodoro tomato image and countdown timer.
Label() -> Displays the timer status and progress checkmarks.
Button() -> Allows the user to start or reset the timer.
window.after(ms, function) -> Recursively calls count_down() every second to update the countdown.
window.mainloop() -> Keeps the GUI running and responsive.

Usage
Click the Start button to begin the Pomodoro session.
Work for the set duration (default 25 minutes, but set to 7 seconds for testing).
After completing a work session, take a short break (default 5 minutes).
Every fourth session, take a long break (default 20 minutes).
Click the Reset button at any time to stop and restart the timer.

Requirements
Python 3.x
Tkinter (included in standard Python library)
math module (included in standard Python library)

Setup & Execution
Ensure Python is installed.
Save the script as main.py.
Place tomato.png in the same directory as the script.
Run the script using:
python main.py
Use the GUI to start and reset the timer.

Notes
The work and break durations are currently set to shorter values for testing. Update the WORK_MIN, SHORT_BREAK_MIN, and LONG_BREAK_MIN constants to their intended values.
The app uses color-coded labels to indicate different phases:
Green for work sessions
Pink for short breaks
Red for long breaks
Checkmarks (✔) are displayed after each completed work session to track progress.
