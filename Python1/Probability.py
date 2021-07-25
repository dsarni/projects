# Daniel Sarni 
# dsarni@ucsc.edu
# Programming Assignment 7
# This program asks to user to input information of dice and the amount of trials they'd like to perform
# and outputs the statistics of the probability of what side the dice would land on

import random
def throwDice(m, k, R):
    diceList = []
    for i in range(m):
        diceList.append(R.randrange(1, k+1))
    return (tuple(diceList))

def main(SEED=237):
    m = int(input("\nEnter the number of dice: "))
    while m < 1:
        print("The number of dice must be at least 1")
        m = int(input("Please enter the number of dice: "))
    k = int(input("\nEnter the number of sides on each die: "))
    while k < 2:
        print("The number of sides on each die must be at least 2")
        k = int(input("Please enter the number of sides on each die: "))
    nTrials = int(input("\nEnter the number of trials to perform: "))
    while nTrials < 1:
        print("The number of trials must be at least 1")
        nTrials = int(input("Please enter the number of trials to perform: "))

    rng = random.Random(SEED)
    frequency = ((m * k) +1)*[0] 
    for i in range(nTrials):
        t = throwDice(m, k, rng)
        frequency[sum(t)] += 1;

    relativeFrequency = [0, 0]
    Experimental = [0, 0]
    for i in range(2, len(frequency)):
        r = frequency[i] / nTrials
        relativeFrequency.append(r)
        e = (relativeFrequency[i] * 100)
        experiment = round(e, 3)
        Experimental.append(experiment)
    print()
    formatAnswer = "{: >4}{: >11}{: >18.5f}{: >21.2f} %"
    print(" Sum     Frequency     Relative Frequency     Experimental Probability")
    print("----------------------------------------------------------------------")
    for i in range(m, len(frequency)):
       print(formatAnswer.format(i,frequency[i],relativeFrequency[i], Experimental[i]))
    print()
if __name__=='__main__':

    main()
