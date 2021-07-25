"""
@author Tori McDonald
@version 10/21/2020
@ file primefactor.py

This program finds the prime factorization of an integer
"""

import math

def factor(number):
    factors = []
    sqrt = int(math.sqrt(number))
    d = 2

    while (d <= sqrt):
        if (number % d != 0):
                d += 1
        else:
            factors.append(d)
            number = number / d

    if (d > sqrt):
        factors.append(number)

    return factors


def main():
    num = int(input("Please enter a number to find the prime factors of: "))

    factorization = factor(num)

    print("The prime factorization of ", num, "is: ")
    print(factorization)

main()
