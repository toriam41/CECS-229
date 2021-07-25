"""
@author Tori McDonald
@version 10/21/2020
@ file sieve.py

This program finds all primes less than 10,000
"""

# Find all prime numbers 1 - 100
primesToHundred = [2]

startInt = 2
counter = startInt + 1

while (counter <= 100):
    if (counter % startInt != 0):
        primesToHundred.append(counter)

    counter += 1

#print(primesToHundred)

index = 1
i = index + 1
startInt = primesToHundred[index]

while (startInt != primesToHundred[-1]):
    while (i < len(primesToHundred)):
        counter = primesToHundred[i]

        if (counter % startInt == 0):
            del primesToHundred[i]

        i += 1

    index += 1
    startInt = primesToHundred[index]

#print(primesToHundred)

primesToTenThousand = []

for i in primesToHundred:
    primesToTenThousand.append(i)

#print(primesToTenThousand)

c = 101
index = 0

while (c <= 10000):
    while (index < len(primesToHundred)):
        startInt = primesToHundred[index]
        mod = c % startInt

        if (mod == 0):
            break
        else:
            index +=1

    if (index == len(primesToHundred)):
        primesToTenThousand.append(c)

    c += 1
    index = 0

print(primesToTenThousand)
