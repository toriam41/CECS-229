"""
@author Tori McDonald
@version 10/3/2020
@ file rectangle.py

This program creates the class for Rectangle objects
"""

class Rectangle():
    def __init__(self, length = None, width = None):
        if (length == None and width == None):
            self.length = 1
            self.width = 1
        else:
            self.length = length
            self.width = width

    def getArea(self):
        return self.length * self.width

    def getPerimeter(self):
        return 2 * (self.length + self.width)
