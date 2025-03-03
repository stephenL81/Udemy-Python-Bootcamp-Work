Day 27 - Mile to Km & Km to Mile Converter

Overview

This is a simple Tkinter-based GUI application that allows users to convert distances between miles and kilometers. The application provides an intuitive interface where users can input a value, choose the conversion direction using radio buttons, and get the result with a button click.


Features

Converts miles to kilometers and vice versa.

Allows user input via an entry field.

Displays results dynamically.

Uses radio buttons to switch between conversion modes.

Simple and responsive layout with labels and buttons.


How it Works (Code Overview)

calculate() -> Converts miles to kilometers and updates the result label.

calculate2() -> Converts kilometers to miles and updates the result label.

radio_used() -> Changes the conversion mode based on the selected radio button.

Entry() -> Accepts user input for the conversion value.

Label() -> Displays static text and results.

Button() -> Triggers the selected conversion function.

Radiobutton() -> Allows the user to switch between conversion modes.

window.mainloop() -> Keeps the GUI running and responsive.


Usage

Enter a numerical value in the input box.

Select a conversion mode (Miles to Km or Km to Miles) using the radio buttons.

Click the "Calculate" button to see the converted value.


Requirements

Python 3.x

Tkinter (included in standard Python library)


Setup & Execution

Ensure you have Python installed.

Save the script as main.py.

Run the script using:

python main.py

Interact with the GUI to perform conversions.


Notes

The application updates labels dynamically when switching between conversion modes.

The radio buttons modify labels and adjust the calculation function accordingly.
