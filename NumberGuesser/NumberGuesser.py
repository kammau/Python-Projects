""" Author: Kamryn Smith
    Date Completed: Jun 7, 2026
    Time Worked On: Unknown

    Program Description: A simple number guessing game that prompts the user to enter a lower bound and 
        upper bound number, with which (using the random module), the program will randomly select a number 
        within that range (inclusive of both lower and upper bounds). The user will be given 5 chances to 
        guess said number, with hints being returned to the user during the guessing process based on 
        whether the user's guess was lower (returning "Too low! Try a higher number!") or higher (returning
        "Too high! Try a lower number!") than the generated number. If the user guesses the correct number
        within 5 guesses, they win the game; otherwise, they automatically lose. After each outcome, the game
        asks the user if they would like to play again. If the player chooses to play again, the process will
        restart, reprompting for new lower and upper bounds. If the player chooses not to play again, the program terminates.
"""

# For random number generation between set range
from random import randint

print("--- Welcome to the Number Guessing Game! ---\n")
continue_game = "y"

# While the user wants to continue game play
while (continue_game == "y"):
    # Input validation to ensure lower and upper bound input is an integer
    try:
        lowerBound = int(input("Please enter a lower bound: "))
        upperBound = int(input("Please enter an upper bound: "))
        num = randint(lowerBound, upperBound)
    # Handle invalid user input
    except ValueError:
        print("\n***That is not a valid number!***\n")
        continue
    
    # Holds the current guess the user is on
    guess_num = 1

    print("\nYou'll have 5 chances to guess the correct number!\n")
    print("Ready...\nSet...\nGo!\n")

    # While the user has not guessed the correct number and the number of guesses has not exceeded 5
    while (guess_num <= 5):

        # Input validation to ensure user's guess input is a valid integer
        try:
            user_guess = int(input(f"Guess {guess_num}: "))
        # Handle invalid user input
        except ValueError:
            print("\n***That is not a valid number!***\n")
            continue
        
        # User wins
        if (user_guess == num):
            print(f"Congratulations, you've won! It only took you {guess_num} try's!")
            break
        # User looses
        elif (guess_num >= 5 and user_guess != num):
            print(f"Sorry, you ran out of chances! The number was {num}! Better luck next time...")
            break
        # Too high
        elif (user_guess > num):
            print("Too high! Try a lower number!")
        # Too low
        elif (user_guess < num):
            print("Too low! Try a higher number!")
        
        # Increment the guess counter
        guess_num += 1

    # Replay game?    
    user_response = input("\nWould you like to play again (y/n)? ")

    if (user_response == "y"):
        # Restart while loop
        continue
    else:
        # Exit
        print("Thanks for playing!")
        continue_game = "n"
        break