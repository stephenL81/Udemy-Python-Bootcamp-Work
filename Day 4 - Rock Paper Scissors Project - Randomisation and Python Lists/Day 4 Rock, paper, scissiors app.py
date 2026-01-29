import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock,paper,scissors]

user_choice = int(input("What would you like to choose? Type 0 for Rock, 1 for Paper, 2 for Scissors and press enter\n>>>"))
random_number = random.randint(0,2)

if user_choice < 0 or user_choice >=3:
    print("You did not pick a number between 0 and 2. YOU LOSE!!!!")
else:
    print(f"\nYour Choice\n{options[user_choice]}")
    print(f"\nComputers Choice\n{options[random_number]}")

    if user_choice == random_number:
        print("Its a draw")
    elif user_choice == 0:
        if random_number == 1:
            print("You lose!")
        else:
            print("You win!")
    elif user_choice == 1:
        if random_number == 0:
            print("You win!")
        else:
            print("You lose!")
    elif user_choice == 2:
        if random_number == 0:
            print("You lose!")
        else:
            print("You win!")
