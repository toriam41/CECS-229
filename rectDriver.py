"""
@author Tori McDonald
@version 10/3/2020
@ file rectDriver.py

This program tests objects of the Rectangle class
"""
from rectangle import Rectangle


def main():
    rect1 = Rectangle(40, 4)
    rect2 = Rectangle(35.9, 3.5)
    rect3 = Rectangle()

    print("Rectangle 1")
    print("-----------")
    print("Length: ", rect1.length)
    print("Width: ", rect1.width)
    print("Area: ", rect1.getArea())
    print("Perimeter: " + str(rect1.getPerimeter()))
    print("\n")

    print("Rectangle 2")
    print("-----------")
    print("Length: ", rect2.length)
    print("Width: ", rect2.width)
    print("Area: ", rect2.getArea())
    print("Perimeter: ", rect2.getPerimeter())
    print("\n")

main()
