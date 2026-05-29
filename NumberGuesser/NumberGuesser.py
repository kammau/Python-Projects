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
    guess = False

    print("\nYou'll have 5 chances to guess the correct number!\n")
    #FIXME: Delete later
    print(f"Correct num: {num}")
    print("Ready...\nSet...\nGo!\n")

    while ((guess == False) & (guess_num < 5)):
        guess_num += 1
        user_guess = int(input(f"Guess {guess_num}: "))

        if (user_guess == num):
            print("Congratulations, you've won!")
            break
    
    user_response = input("\nWould you like to play again (y/n)? ")

    if (user_response == "y"):
        continue
    else:
        print("Thanks for playing!")
        continue_game = "n"
        break