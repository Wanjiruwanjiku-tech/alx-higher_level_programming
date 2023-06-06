#!/usr/bin/python3
""" Module tha runs the class Rectangle """

class Rectangle:
    """The class represents a rctangle"""

    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """ The method initializes the class with 2
		parameters:
			width - reps the width
			height - reps the  height
		Exceptions:
			TypeError if value is not an int
			ValueError if value is < 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Retrieves the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width to valur """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrives the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """The method returns the area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimetet of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """ Returns a str representation of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Returns a str rep of a rectangle
		that can be used to create a new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Prints a rectangle when a class instance is
		deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
