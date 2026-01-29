import random
import hangman_words
import hangman_art

lives = 6
words = hangman_words.word_list
word = str(random.choice(words))
display = ""
incorrect_attempts = []

for char in range(len(word)):  #initially sets display to the length of the word
    display += "_"

print(hangman_art.logo)
while (not display == word) and (lives > 0):
    print(hangman_art.stages[lives])
    print(f"your word is {display}")
    if len(incorrect_attempts) > 0:
        print(f"Incorrect letters {incorrect_attempts}")
    guess = input("Make a guess\n>>>")
    word_with_guesses =""
    correct = False
    for char in range(0,len(word)):
        if guess == word[char]:
            word_with_guesses+= guess
            correct = True
        elif display[char] == "_":
            word_with_guesses+= "_"
        else:
            word_with_guesses += display[char]

    display = word_with_guesses

    if correct == False:
        incorrect_attempts += guess
        lives-=1
        print(hangman_art.logo)
        print(f"\nWrong, you have {lives} lives left")
    else:
        print(hangman_art.logo)
        print(f"\nCorrect, you have {lives} lives left")

if display == word:
    print(f"\nCONGRATULATIONS the word was {word}, YOU WIN!!!!!!")
else:
    print(hangman_art.stages[0])
    print(f"\nThe word was {word}\nYOU LOSE!!!!!")
