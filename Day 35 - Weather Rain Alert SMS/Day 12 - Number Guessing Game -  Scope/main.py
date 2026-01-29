from art import logo
import random

print(logo)

lives = 0
number = random.randint(1,100)
carry_on = True

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'easy':
    lives = 10
else:
    lives = 5


while lives > 0 and carry_on == True:
    print(f"You have {lives} attempts remaining to guess the number")

    user_guess = int(input("Make a guess: "))

    if user_guess > number:
        print("Too High")
        lives -= 1
    elif user_guess < number:
        print("Too low")
        lives -= 1
    else:
        carry_on = False

if lives == 0:
    print(f"You've run out of guesses!\nThe number was {number}\n You lose!.")
else:
    print(f"You got it! The answer was {number}")