from random import randint

def checkInput(lowerBound, upperBound):
    if ((type(lowerBound) & type(upperBound)) != int):
        print("Please enter valid integers!")
        return False
    
    else:
        return True
    

def getRange(targetNum):
    rangeValid = False

    while (rangeValid == False):
        print("Enter a lower bound for the range: ")
        lowerBound = input()

        print("Enter an upper bound for the range: ")
        upperBound = input()
            
        rangeValid = checkInput(lowerBound, upperBound)
    
    targetNum = randint(lowerBound, upperBound)

    return targetNum


def main():
    guessed = False
    numGuesses = 1
    print("--- Welcome to the number guessing game! ---")
    targetNum = getRange(targetNum)

    print("You'll have 5 chances to guess the correct number!")
    print("\n Ready...")
    print("Set...")
    print("Go!\n\n")
    
    while (guessed == False & numGuesses <= 5):
        print(f"Guess {numGuesses}: ")
        usersGuess = input()

        if (usersGuess == targetNum):
            print("Correct!")
            guessed = True
        
        elif (usersGuess < targetNum):
            print("Too low!")
            numGuesses -= 1
            continue

        else:
            print("Too high!")
            numGuesses -= 1
            continue
    
    print 

