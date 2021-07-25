"""
@author Tori McDonald
@version 10/3/2020
@file euclidalgorithm.py

This program calculates the greatest common divisor of two numbers
"""
def gcd(a, b):
    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a

    while (y != 0):
        r = x % y
        x = y
        y = r

    return x

def main():
    print("Enter two numbers to find the greatest common divisor (gcd)")
    a = input("First Number: ")
    b = input("Second Number: ")

    result = gcd(a, b)

    print("The gcd of ", a, " and ", b, " is ", result)
    print("Goodbye world")
    return 0

main()
