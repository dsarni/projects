# Daniel Sarni
# dsarni@ucsc.edu
# Programming Assigment 5
# This program takes a users input and prints out all prime numbers leading up to the users input.



def makeSieve(n):
    S = [False]*2 + [True]*(n-1)
    for k in range(2,n+1):
        if S[k]:
            m = 2*k
            while m <= n:
                S[m] = False
                m += k
    return S

def getPrimes(n):
    S = makeSieve(n)
    p = []
    for i in range(2,len(S)):
        if S[i] == True:
            p.append(i)
    return p

def inOrder(n, p):
    n1 = 0
    for r in p:
        if (n1 == 10):
            print()
            n1 = 0
        print(r,end = " ")
        n1 += 1
    print()
    print()

if __name__=='__main__':
    n = int(input("\nEnter a positive integer: "))
    while n <= 0:
        n = int(input("Please enter a positive integer: "))
    if n > 1:
        p = getPrimes(n)
        print("\nThere are",len(p),"prime numbers less than or equal to", str(n)+ ":\n")
        inOrder(n, p)
    if n == 1:
        p = getPrimes(n)
        print("\nThere are",len(p),"prime numbers less than or equal to", str(n)+ ":\n")
        print()

