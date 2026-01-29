Day 26 - Nato Alphabet Project Readme

Description:
This program allows the user to input a word, and it will convert each letter of the word into the corresponding NATO phonetic alphabet code (e.g., "A" becomes "Alpha", "B" becomes "Bravo"). The program uses a CSV file to map each letter to its phonetic code and then prints out the phonetic alphabet representation of the inputted word.

How to Run:
Run the script:python main.py
Start the program: The program will prompt you to enter a word.
Enter a word: Type any word, and it will be converted to the NATO phonetic alphabet.
View the result: The program will output a list of phonetic codes corresponding to each letter of the word.

How It Works (Code Overview):
nato_phonetic_alphabet.csv → Contains the NATO phonetic alphabet mapping:
The CSV file has two columns: "letter" (A, B, C, etc.) and "code" (Alpha, Bravo, Charlie, etc.).
This data is used to create a dictionary that maps each letter to its corresponding phonetic code.
pandas → Reads and processes the CSV file:
The pandas.read_csv function is used to read the data into a DataFrame.
iterrows() is used to loop through each row in the DataFrame to populate the dictionary with letter-code pairs.
User input → Accepts a word from the user:
The user is prompted to enter a word, and the program converts the word to uppercase to ensure case-insensitive comparison.
phonetic_dict → A dictionary that maps each letter to its corresponding phonetic code:
Each letter in the user-inputted word is used as a key to fetch the phonetic code from the dictionary.

Key Features:
Case-insensitive: The user can input the word in any case (upper or lower).
Real-time conversion: The program instantly converts the entered word to the NATO phonetic alphabet and displays the result.
Dynamic input handling: The program will work for any word input by the user.
