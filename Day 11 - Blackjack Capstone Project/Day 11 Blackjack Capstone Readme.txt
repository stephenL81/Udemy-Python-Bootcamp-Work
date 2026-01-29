Day 11 - Blackjack Capstone Project Readme

Description:
This is a simple command-line implementation of the classic Blackjack card game. The player competes against the dealer, aiming to get a hand value as close to 21 as possible without exceeding it. The dealer must draw cards until reaching at least 17.

How to Play:
Run the script: python main.py
The player is dealt two random cards, and so is the dealer.
The dealer’s first card is revealed, while the second remains hidden.
The player chooses to either draw another card ('y') or stick with their current hand ('n').
If the player’s total exceeds 21, they bust and lose the game.
Once the player is done, the dealer draws cards until reaching at least 17.
If the dealer’s total exceeds 21, they bust and the player wins.
Otherwise, the player’s and dealer’s scores are compared to determine the winner.

How It Works (Code Overview):
deal_card() → Returns a random card from a predefined deck.
first_deal() → Deals two initial cards to both the player and the dealer.
show_cards() → Displays the player’s hand and the dealer’s first card.
adjust_for_aces() → Converts Aces from 11 to 1 if the total score exceeds 21.
The game loop runs until the player either busts or chooses to stick.
Once the player is done, the dealer automatically draws cards as per game rules.
The final scores determine the winner.

Key Features:
Uses a simple list-based deck for quick card dealing.
Handles Aces dynamically to avoid immediate busts.
Implements game logic for both player and dealer turns.
Displays real-time game status and results in the terminal.

