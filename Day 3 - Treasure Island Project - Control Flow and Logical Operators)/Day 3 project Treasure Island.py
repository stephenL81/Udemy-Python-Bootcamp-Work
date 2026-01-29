print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("\nYou're at a cross road. Where do you want to go?\nType \"left\" or \"right\" >>>")
if direction.lower() != "left":
    print("\nYou fall into a hole. Game Over.")
else:
    swim = input("\nYou've come to a lake. There is an island in the middle of the lake.\nType \"wait\" to wait for a boat. Type \"swim\" to swim across >>>")
    if swim.lower() != "wait":
        print("\nYou are attacked by trout. Game Over.")
    else:
        door = input("\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.\nWhich colour do you choose? >>>")
        if door.lower() == "red":
            print("\nBurned by Fire. Game Over.")
        elif door.lower() == "yellow":
            print("\nYou Win!")
        elif door.lower() == "blue":
            print("\nEaten by beasts. Game Over.")
        else:
            print("\nGame Over.")
