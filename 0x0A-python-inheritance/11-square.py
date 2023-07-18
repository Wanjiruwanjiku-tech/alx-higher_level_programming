#!/usr/bin/python3

""" This Module runs a script that inherits from class
    Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle



class Square(Rectangle):

    # The Derived Class

    def __init__(self, size):
        """ Initialization """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Returns a Square Description """

        return "[Square] {}/{}".format(self.__size, self.__size)
