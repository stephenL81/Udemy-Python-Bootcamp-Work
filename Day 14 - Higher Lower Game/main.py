from art import logo
from art import vs # can do from art import logo,vs
from game_data import data
from random import randint

already_used = []
carry_on = True
score = 0

def find_winner():  #RETURNS LOWERCASE A OR B
    if data[person_a]["follower_count"] > data[person_b]["follower_count"]:
        return "a"
    else:
        return "b"

def pick_person(): # RETURNS A RANDOM NUMBER AND ALSO ADDS THAT NUMBER TO ALREADY USED LIST
    person = 0
    carry_on = True
    while carry_on:
        person = randint(0,len(data)-1)
        if not person in already_used:
            carry_on = False
            already_used.append(person)
    return person

print(logo)
print("")
person_a = pick_person()
person_b = pick_person()

while carry_on:
    print(f"Compare A: {data[person_a]['name']}, {data[person_a]['description']}, from {data[person_a]['country']}")
    print(vs)
    print(f"Against B: {data[person_b]['name']}, {data[person_b]['description']}, from {data[person_b]['country']}")
    user_choice = input("Who has the most followers? Type 'A' or 'B' :")
    if user_choice.lower() == find_winner():
        score += 1
        person_a = person_b
        person_b = pick_person()
        print("\n*******************************************************************************")
        print(f"\nYou're right, current score: {score}")

    else:
        print("Wrong , Game Over!")
        carry_on = False