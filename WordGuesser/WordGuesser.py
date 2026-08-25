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
print("\nYou will have 10 attempts to guess each character in the word. Good luck!\n")

attempts = 10
guessed_chars = ""
score = 0

while (attempts != 0):
    score = 0

    for char in target_word:
        if char in guessed_chars:
            print(char, end=" ")
            score += 1
        else:
            print("_", end=" ")

    if (score == len(target_word)):
        print("\n\nYou Win!")
        print(f"\nThe word was: {"".join(target_word)}")
        break

    # if (attempts == 0):
    #     print("\n\nYou loose! Better luck next time...")
    #     print(f"\nThe word was: {"".join(target_word)}")
    #     break

    users_guess = input("\n\nGuess a character: ")

    if (len(users_guess) != 1):
        print("\nPlease enter a valid character!\n")
        continue

    if (users_guess in guessed_chars):
        print("\nYou already guessed that character!\n")
        continue

    guessed_chars += users_guess

    if (users_guess not in target_word):
        attempts -= 1
        
        print("\nWrong!")
        print(f"\nYou have {attempts} more attempts!\n")


print("\n\nYou loose! Better luck next time...")
print(f"\nThe word was: {"".join(target_word)}")
        