import art
#Could also do from art import logo. The on line 7 - print(logo)
print(art.logo)

carry_on = True
highest = 0
winner = ""
bids ={}
while carry_on:

    name = input("What is your name? >>>")
    bid = int(input("What's your bid? >>>"))

    bids[name] = bid

    if input("Do you wish to add another bid, please type yes or no >>>") == "no":
        carry_on = False
    else:
        print("\n" * 20)

for key in bids:
    if bids[key] > highest:
        highest = bids[key]
        winner = key

print(f"The winner is {winner} with a bid of {highest}!")