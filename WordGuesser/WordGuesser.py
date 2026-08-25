""" Author: Kamryn Smith
    Date Completed: 

    Program Description: 
"""

import random

# 10 random words that I generated from the internet LOL
words = ["Pencil", "Ocean", "Guitar", "Cloud", "Window", "Apple", "Tiger", "House", "River", "Book"]
target_word = list(random.choice(words).lower())

print("--- Word Guessing Game ---")
name = input("\nWhat is your name player? ")
print(f"Welcome {name}, to the Word Guessing Game!")
print("\nYou will have 10 attempts to guess each character in the word. Good luck!")

attempts = 10
guessed_chars = ""

print(target_word)
for char in target_word:
    if char in guessed_chars:
        print(char, end=" ")
    else:
        print("_", end=" ")

# while (attempts > 0):
#     for char in target_word:
#         if char in guessed_chars:
#             print(char, end=" ")
#         else:
#             print("_", end=" ")



        