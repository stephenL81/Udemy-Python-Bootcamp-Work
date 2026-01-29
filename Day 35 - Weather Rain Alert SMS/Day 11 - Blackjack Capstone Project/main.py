from art import logo
import random

print(logo)

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
dealer_score = 0
users_cards = []
dealers_cards = []

def deal_card(): #returns a random card
    return random.choice(cards)
#ok up to here , move carry_on and not sure about dealer_carry_on

def first_deal(): #deals 2 random cards for the player and dealer
    users_cards.append(deal_card())
    users_cards.append(deal_card())
    dealers_cards.append(deal_card())
    dealers_cards.append(deal_card())

def show_cards(): #show users cards and current score
    print(f"\nYour cards: {users_cards}, current score: {sum(users_cards)}")
    print(f"Dealers first card: {dealers_cards[0]}")

def adjust_for_aces(hand): #Convert aces to 1's if score goes over 21
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1

first_deal()
user_score = int(sum(users_cards))
dealer_score = int(sum(dealers_cards))

carry_on = True

#players turn
while carry_on:
    show_cards()
    if input("Type 'y' to get another card. Type 'n' to stick >>>") == "y":
        users_cards.append(deal_card())
        adjust_for_aces(users_cards)
        user_score = sum(users_cards)
        if user_score > 21:
                print(f"\nYour cards:{users_cards}, Final Score: {user_score}")
                print("Bust! You Lose")
                carry_on = False

    else:
        carry_on = False

#Dealers Turn
if user_score <= 21:
    print(f"\nDealers cards: {dealers_cards}, Dealers Score: {dealer_score}")


    while dealer_score < 17:
        print("Dealer draws a card...")
        dealers_cards.append(deal_card())
        adjust_for_aces(dealers_cards)
        dealer_score = int(sum(dealers_cards))
        print(f"Dealer's Cards: {dealers_cards}, Dealers Score: {dealer_score}")

    #Determine winner
    if dealer_score > 21:
        print("Dealer is bust! You win!")
    elif user_score > dealer_score:
        print("You win!")
    elif user_score < dealer_score:
        print("Dealer wins!")
    else:
        print("Its a draw!!")












        #SHOULD I USE RECURSION???????
