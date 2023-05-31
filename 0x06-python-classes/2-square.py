#!/usr/bin/python3
"""Runs a Class called Square"""

class Square:
    """The class definition represents a square
    In this task we add validation in the class
    """

    def __init__(self, size=0):
        """size has been set to 0
        Exceptions:
            if size is not an int a TypeError exception
            is raise
            if size is less than 0 a ValueError exception
            is raised
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
