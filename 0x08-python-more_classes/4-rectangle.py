#!/usr/bin/python3
""" Module that runs the class rectangle """

class Rectangle:
    def __init__(self, width=0, height=0):
        """ The method initializes the class
            Parameters:
                        width - reps the width
                        height - reps the height
            Exceptions:
                TypeError if values are not integers
                ValueError if values are < 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ The method retrives the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ The method sets width to the value, value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """The method retrives the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height to value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns the area of a rectangle
                width * height
        """
        return self.__height * self.__width

    def perimeter(self):
        """ Returns the perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """ Returns a printable representation of a
		rectangle using the # character.
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
        if i != self.__height -1:
            rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        """ The method returns the string rep of the
		rectangle
        """
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle
