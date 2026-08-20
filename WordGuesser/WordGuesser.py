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

player_name = input("What is your name player? ")
print(f"Welcome {player_name}! You will have 10 trys to guess the word good luck!\n")

i = 0

print(target_word)
for letter in guessed_letters:
    print(letter, end=" ")


user_input = input("\n\nGuess a letter: ").lower()

if (user_input in target_word):
    print("Yes")

else:
    print ("\n Wrong! \n")