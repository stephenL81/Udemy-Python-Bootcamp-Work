Day - 5 Password Generator Project

Description:
This Python script generates a random password based on the user's input. The user is prompted to specify the number of letters, symbols, and numbers they want in their password. The script then combines these inputs, shuffles the characters, and generates a secure random password.

How to Use:
Run the script:python main.py

User Input:
Enter the number of letters for your password.
Enter the number of symbols you want.
Enter the number of numbers to be included.

Password Generation:
The program generates a password by randomly selecting characters from predefined lists of letters, symbols, and numbers.

Shuffling:
The password characters are shuffled to ensure randomness.

Password Display:
The final generated password is printed to the screen.

How It Works (Code Overview):

Input Collection:
The user is prompted to input how many letters, symbols, and numbers they would like in their password.
Password Construction:

Random characters are picked from predefined lists of letters, symbols, and numbers, using the random.choice() function.
Shuffling:

The random.shuffle() function is used to randomly rearrange the order of the selected characters.
Password Output:

The script then combines the shuffled characters into a single string and prints the password.

Key Features:
Customizable password length based on the user's choice of letters, numbers, and symbols.
Randomized selection and shuffling of characters to ensure security.
User-friendly interface for easy password generation.
