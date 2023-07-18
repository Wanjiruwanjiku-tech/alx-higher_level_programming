#!/usr/bin/python3
""" Runs a class Square """

class Square:
    """In this task we add a public instance
       method called my_print that prints a
       square of size 'size'
    """

    def __init__(self, size=0):
        """"Create a public instance att called size"""
        self.__size = size

    def area(self):
        """Returns the area if the square"""
        return self.__size ** 2

    @property
    def size(self):
        """ Retrive the Size """
        return self.__size

    @size.setter
    def size(self, value):
        """sets size to the value value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ The method instance prints a square
            using the char '#' and an empty line
            if size == 0
        """
        if size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
