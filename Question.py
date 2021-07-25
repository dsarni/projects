# Daniel Sarni
# dsarni@ucsc.edu
# Programming Assignment 6
# This program guesses a number that the user is thinking based on the users input.
def numberGuesser():
    global low
    global high
    global LGE
    if low == high:
        if guesses > 1:
            print("\nYour number is "+str(low)+". "+"I found it in "+str(guesses)+" guesses.")
            print()
            print()
        if guesses == 1:
            print("\nYour number is "+str(low)+". "+"I found it in 1 guess.")
            print()
            print()
    if low < high:
        rangeOf = str(input("Type 'L', 'G' or 'E': ")).upper()
        while rangeOf not in LGE:
            print()
            rangeOf = str(input("Please type 'L', 'G' or 'E': ")).upper()
            if rangeOf == ['L', 'G', 'E']:
                break
        if rangeOf == "L":
            lResponse()
        if rangeOf == "E":
            eResponse()
        if rangeOf == "G":
            gResponse()

def lResponse():
    global guesses
    global low
    global midpoint
    global high
    guesses = guesses + 1
    high = midpoint - 1
    midpoint = (high + low ) // 2
    if high == midpoint and low != midpoint:
        low = high + 1
        print("\nYour answers have not been consistent.")
        print()
        print()
    if low < high:
        print("\nIs your number Less than, Greater than, or Equal to "+str(midpoint)+"?")
    numberGuesser()

def gResponse():
    global guesses
    global low
    global midpoint
    global high
    guesses = guesses + 1
    low = midpoint + 1
    midpoint = (high + low) // 2
    if low < high:
        print("\nIs your number Less than, Greater than, or Equal to "+str(midpoint)+"?")
    numberGuesser()

def eResponse():
    global guesses
    print()
    guesses = guesses + 1
    if guesses == 1:
        print("I found your number in 1 guess.\n")
        print()
    if guesses > 1:
        print("I found your number in "+str(guesses)+" guesses.\n")
        print()
print()
print()
print("Enter two numbers, low then high.")
low = int(input("low = "))
high = int(input("high = "))

while low > high:
    print()
    print("Please enter the smaller followed by the larger number.")
    low = int(input("low = "))
    high = int(input("high = "))
print()
print("Think of a number in the range", str(low),"to",str(high)+".")
if low == high:
    print("\nYour number is "+str(low)+". I found it in 0 guesses.\n")
    print()
if low < high:
    midpoint = (high + low) // 2
    print("\nIs your number Less than, Greater than, or Equal to "+str(midpoint)+"?")
    LGE = ["L", "G", "E",]
    guesses = 0
    numberGuesser()

