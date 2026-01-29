Day 16 - Object Oriented Programming Coffee Machine Project Readme

This is an Object-Oriented Programming (OOP) version of the coffee machine project. It allows users to order coffee, check resources, process payments, and deduct ingredients using modular classes.

How This Version is Different from the Previous One:
Uses OOP principles to separate concerns into different classes.
Instead of global variables and functions, each component is handled by a dedicated class.
More scalable and reusable compared to the procedural version.

How to Use:
Run the script:python main.py
Type your choice: espresso, latte, or cappuccino to order a drink.
Type 'report' to check available resources and money earned.
Type 'off' to power down the machine.
If ordering coffee, insert coins when prompted.
The program will return change (if applicable) and serve the drink!

Code Structure (OOP Breakdown)
MenuItem class → Models individual coffee menu items (name, ingredients, cost).
Menu class → Stores available drinks and retrieves menu options.
CoffeeMaker class → Handles resource management (checking inventory, making coffee).
MoneyMachine class → Handles payment processing (accepting coins, calculating change).
main.py → Brings all classes together and runs the program.

Key Features:
Encapsulation: Each responsibility (menu, machine, money) is handled in its own class.
Modular Design: Classes can be reused or extended easily.
Better Code Maintainability: Easier to debug and expand compared to the procedural version.
