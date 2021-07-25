"""
@author Tori McDonald
@version 10/21/2020
@ file rsa.py

This program generates a valid key for the RSA cryptosystem
"""

import random
import math

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

def keyGenerator():
    # randomly select the first prime number p
    p = random.randint(10, 100)
    sqrt = int(math.sqrt(p))
    i = 2

    while i <= sqrt:
        rem = p % i

        if (rem != 0):
            i += 1
        else:
            p = random.randint(100, 500)
            sqrt = int(math.sqrt(p))
            i = 2

    # randomly select the second prime number q
    q = random.randint(10, 100)
    sqrt = int(math.sqrt(q))
    i = 2

    while i <= sqrt:
        rem = q % i

        if (rem != 0):
            i += 1
        else:
            q = random.randint(100, 500)
            sqrt = int(math.sqrt(q))
            i = 2

    # multiply p and q to get n
    n = p * q

    # find e relatively prime to (p - 1)(q - 1)
    rp = (p - 1) * (q - 1)
    e = 10

    while (gcd(e, rp) != 1):
        e += 1

    print("A valid RSA public encryption key(n, e) is (", n, ", ", e, ")!")

keyGenerator()
