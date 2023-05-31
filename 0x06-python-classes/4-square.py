#!/usr/bin/python3
"""Runs a class Square"""

class Square:
    """For this task we need to add the
    getter and setter attributes
    """
    def __init__(self, size=0):
        """Create a private size instance"""
        self.__size = size #double underscores

    def area(self):
        """The method returns the area"""
        return self.__size ** 2

    @property
    def size(self):
        """The instance retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size to the value 'value'
        if value is not an int a TypeError exception is
        raised and a ValueError if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size musy be >= 0")
        else:
            self.__size = value
