#!/usr/bin/python3
"""Runs a class called Square"""

class Square:
    """For this task we add a new public instance
    Method called area to the class
    """

    def __init__(self, size=0):
        """"If size is not an int a TypeError exception
        is raised.
        if size is less that 0 a ValueError exception
        is raised
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """The method takes no parameters (except self)
        """
        return self.__size ** 2
