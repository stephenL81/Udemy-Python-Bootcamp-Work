Day 15 - Coffee Machine Project Readme

Description:
This is a virtual coffee machine program that allows users to order different types of coffee (espresso, latte, cappuccino). 

The machine:
Checks if there are enough resources (water, milk, coffee).
Processes coin payments and calculates change.
Deducts resources when a drink is made.
Allows users to view a report of available resources.
Supports a refill option to reset resources.
Can be powered on/off with a command.

How to Use:
Run the script:python main.py
Type your choice:espresso, latte, or cappuccino to order a drink.
Type 'report' to check available resources.
Type 'refill' to restock resources.
Type 'off' to power down the machine.
If ordering coffee, insert coins when prompted.
The program will return the change (if applicable) and serve the drink!

Key Features:
Ingredient Check: Ensures enough water, milk, and coffee before making a drink.
Coin Processing: Accepts payments and calculates correct change.
Inventory Management: Tracks and updates available ingredients.
Power Control: Allows turning off the machine.

Code Overview:
ml_or_g() → Returns the correct unit (ml or g) for each ingredient.
report() → Displays current resource levels.
check_resources(drink) → Checks if there are enough ingredients to make the selected drink.
deduct_resource() → Deducts the used resources after making a drink.
process_coins() → Handles payment input and returns the total amount inserted.
transaction_successful(cash) → Compares inserted money to the drink price, returns change if necessary, and serves the drink.
Main Loop (while power == True):Continuously prompts for user input (off, report, refill, or coffee selection).Calls the appropriate functions based on the user’s input.
