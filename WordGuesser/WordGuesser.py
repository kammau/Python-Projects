""" Author: Kamryn Smith
    Date Completed: 
    Time Worked On (Including idea development and refinement): 45 min

    Program Description: 
"""

import random

# 10 random words that I generated from the internet LOL
words = ["Pencil", "Ocean", "Guitar", "Cloud", "Window", "Apple", "Tiger", "House", "River", "Book"]
target_word = list(random.choice(words).lower())
guessed_letters = ["_" for char in target_word]
attempts = 0

player_name = input("What is your name player? ")
print(f"Welcome {player_name}! You will have 10 trys to guess the word good luck!\n")

while ((attempts < 10) or (guessed_letters == target_word)):
    print(target_word)
    for letter in guessed_letters:
        print(letter, end=" ")


    user_input = input("\n\nGuess a letter: ").lower()

    if (user_input in target_word):
        i = 0
        for letter in target_word:
            if user_input == target_word[i]:
                guessed_letters[i] = user_input

            i += 1

    else:
        print ("\n Wrong! \n")

    attempts += 1

    print(guessed_letters)

if (guessed_letters == target_word):
    print("Congratulations!")
else:
    print("Better luck next time!")