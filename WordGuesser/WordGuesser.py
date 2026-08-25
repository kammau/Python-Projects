""" Author: Kamryn Smith
    Date Completed: 

    Program Description: 
"""

# Module to give the program a method to select a random word from words list
import random

# 10 random words that I generated from the internet LOL
words = ["pencil", "ocean", "guitar", "cloud", "window", "apple", "tiger", "house", "river", "book"]

# Stores a randomly chosen word from words list using random's .choice method
target_word = random.choice(words)

# Welcoming message + getting user's name
print("--- Word Guessing Game ---")
name = input("\nWhat is your name player? ")
print(f"Welcome {name}, to the Word Guessing Game!")
print("\nYou will have 10 attempts to guess each character in the word. Good luck!\n")

# Store's wrong attempts left before user looses
attempts = 10
# Store's each character/letter the user guesses
guessed_chars = ""
# Store's the number of characters/letters the user has guessed correctly
score = 0

# --- Main Game Loop ---
# While the user hasn't run out of attempts
while (attempts != 0):
    # Reset score to 0 
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

    users_guess = input("\n\nGuess a character: ").lower()

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

        if (attempts == 0):
            print("\n\nYou loose! Better luck next time...")
            print(f"\nThe word was: {"".join(target_word)}")
        