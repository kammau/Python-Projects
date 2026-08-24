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
wrong_attempts = 10

player_name = input("What is your name player? ")
print(f"Welcome {player_name}! You will have 10 trys to guess the word good luck!\n")

while (wrong_attempts > 0):

    if (guessed_letters == target_word):
        break

    for letter in guessed_letters:
        print(letter, end=" ")

    user_input = input("\n\nGuess a letter: ").lower()

    if (user_input in target_word):
        i = 0
        for letter in target_word:
            if user_input == target_word[i]:
                guessed_letters[i] = user_input

            i += 1

    elif (user_input in guessed_letters):
        print ("You already guessed that letter!")

    else:
        print ("\nWrong! \n")
        wrong_attempts -= 1
        print(f"Attempts Remaining: {wrong_attempts}")

    #print(guessed_letters)

if (guessed_letters == target_word):
    print("\nCongratulations!")
else:
    print("\nBetter luck next time!")

print(f"\nThe word was: {"".join(target_word)}")