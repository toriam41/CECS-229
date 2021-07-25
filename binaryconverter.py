"""
@author Tori McDonald
@version 10/3/2020
@ file binaryconverter.py

This program converts a base 2 number to base 10
"""

def conversion(num):
    number = num
    places = 0
    sum = 0

    while (number != 0):
        number /= 10
        places += 1

    i = 0
    while (i < places):
        digit = num % 10
        num /= 10
        sum += digit * 2**i
        i += 1

    return sum

def main():
    binary = int(input("Please enter a binary number to convert to decimal: "))
    decimal = conversion(binary)
    print(binary, "is equal to", decimal, "in decimal (base 10)")

    return 0


main()
