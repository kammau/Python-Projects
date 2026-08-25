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


while (attempts > 0):
    score = 0

    if (score == len(target_word)):
        print("\nYou Win!")
        print(f"\n The word was: {"".join(target_word)}")
    for char in target_word:
        if char in guessed_chars:
            print(char, end=" ")
            score += 1
        else:
            print("_", end=" ")

    users_guess = input("\nGuess a character: ")

    if (len(users_guess) != 1):
        print("\nPlease enter a valid character!\n")
        continue

    if (users_guess in guessed_chars):
        print("\nYou already guessed that character!\n")

    guessed_chars += users_guess

    if (users_guess not in target_word):
        print("\nWrong!")
        print(f"\nYou have {attempts} more attempts!")

        if (attempts == 0):
            print("\nYou loose! Better luck next time...")
            print(f"\nThe word was: {"".join(target_word)}")

        