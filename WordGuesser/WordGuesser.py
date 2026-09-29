""" Author: Kamryn Smith
    Date Completed: 9/28/26

    Program Description: A word-guessing game where the program selects a random word from
    a word list, and the user has 10 attempts to guess the correct characters within the target word
    before the attempts run out.
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

    # For each character in the target word
    for char in target_word:
        # Map each correct user guess to the correct spots in target word
        if char in guessed_chars:
            # Print the correctly guessed character in output
            print(char, end=" ")
            # Increment score
            score += 1
        # Else if the user's guess is not in the target word
        else:
            # Output a blank underscore for that target letter
            print("_", end=" ")

    # If the user guesses each character in target word
    if (score == len(target_word)):
        # Output winning message and target word
        print("\n\nYou Win!")
        print(f"\nThe word was: {"".join(target_word)}")
        break

    # Get user's guess
    users_guess = input("\n\nGuess a character: ").lower()

    # If user's guess is not a valid character
    if (len(users_guess) != 1):
        print("\nPlease enter a valid character!\n")
        continue

    # If user's guess has already been guessed
    if (users_guess in guessed_chars):
        print("\nYou already guessed that character!\n")
        continue

    # Add user's input into the guessed characters list
    guessed_chars += users_guess

    # If the user's guess is not in the target word
    if (users_guess not in target_word):
        # Decrement attempts counter
        attempts -= 1

        # Output incorrect guess message
        print("\nWrong!")
        print(f"\nYou have {attempts} more attempts!\n")

        # If the user runs out of guessing attempts
        if (attempts == 0):
            # Output loosing message and correct full word
            print("\n\nYou loose! Better luck next time...")
            print(f"\nThe word was: {"".join(target_word)}")
        