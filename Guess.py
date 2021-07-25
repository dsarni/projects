# Daniel Sarni
# dsarni@ucsc.edu
# Programming Assignment 4
# This program picks a random integer from 1-10 and gives the user 3 guesses to pick the right integer.

import random
winningNumber = random.randint(1,10)
def checker(): 
    if guess > winningNumber:
        print("Your guess is too high.")
        print()
    elif guess < winningNumber:
        print("Your guess is too low.")
        print()
    else:
        print("You win!\n")

def losecheck():
    if guess3 == winningNumber:
        print("You win!\n")		
    elif guess3 > winningNumber:
        print("Your guess is too high.\n")
        print("You lose. The number was",str(winningNumber)+".\n")
    else:
        print("Your guess is too low.\n")
        print("You lose. The number was",str(winningNumber)+".\n")

print()
print("I'm thinking of an integer in the range 1 to 10. You have three guesses.\n")
guess = int(input("Enter your first guess: "))
checker()
if guess != winningNumber:
    guess = int(input("Enter your second guess: "))
    checker()
    if guess != winningNumber:
        guess3 = int(input("Enter your third guess: "))
        losecheck()

