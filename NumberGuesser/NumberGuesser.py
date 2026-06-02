# For random number generation between set range
from random import randint

print("--- Welcome to the Number Guessing Game! ---\n")
continue_game = "y"

while (continue_game == "y"):
    try:
        lowerBound = int(input("Please enter a lower bound: "))
        upperBound = int(input("Please enter an upper bound: "))
        num = randint(lowerBound, upperBound)
    except ValueError:
        print("\n***That is not a valid number!***\n")
        continue

    guess_num = 0

    print("\nYou'll have 5 chances to guess the correct number!\n")
    print("Ready...\nSet...\nGo!\n")

    while (guess_num <= 5):
        guess_num += 1

        try:
            user_guess = int(input(f"Guess {guess_num}: "))
        except ValueError:
            print("\n***That is not a valid number!***\n")
            continue

        if (user_guess == num):
            print(f"Congratulations, you've won! It only took you {guess_num} try's!")
            break
        
        elif (guess_num >= 5 and user_guess != num):
            print(f"Sorry, you ran out of chances! The number was {num}! Better luck next time...")
            break
        
        elif (user_guess > num):
            print("Too high! Try a lower number!")
        
        elif (user_guess < num):
            print("Too low! Try a higher number!")
        
    user_response = input("\nWould you like to play again (y/n)? ")

    if (user_response == "y"):
        continue
    else:
        print("Thanks for playing!")
        continue_game = "n"
        break