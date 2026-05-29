from random import randint


print("--- Welcome to the Number Guessing Game! ---\n")
main()
#rename funcs?

def main():
    lowerBound = int(input("Please enter a lower bound: "))
    upperBound = int(input("Please enter an upper bound: "))

    num = randint(lowerBound, upperBound)
    guess_num = 0
    guess = False

    print("You'll have 5 chances to guess the correct number!\n")
    print("Ready...\nSet...\nGo!\n")

    while ((guess == False) & (guess_num < 5)):
        guess_num += 1
        user_guess = input(f"Guess {guess_num}: ")

        if (user_guess == num):
            print("Congratulations, you've won!")
    
    user_response = input("Would you like to play again (y/n)?")

    if (user_response == "y"):
        main()
    else:
        print("Thanks for playing!")
    