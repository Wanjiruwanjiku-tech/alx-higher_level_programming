#!/usr/bin/python3
""" This Module defines a Square subclass derived
    fron the rectangle subclass
"""

#Import the class

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle): #The Drived class

    """ The class defines a square """
    def __init__(self, size):
        """Initialize a New square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Strinb rep for square """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """ Returns the area """
        area = self.__size ** 2
        return area
