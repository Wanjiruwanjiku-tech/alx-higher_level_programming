#!/usr/bin/python3
"""Module that runs the class rectangle"""

class Rectangle:
    """The class definition reps a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

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
        self.height = heigh
        type(self).number_of_instances += 1

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
        """ Sets Height to Value """
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
        """ Returns string representation """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.width] * self.height)

    def __repr__(self):
        """ Returns str rep of a rectangle that can 
		create a new instance 
        """
        return "Rectangke({}, {})".format(self.width, self.height)

    def __del__(self):
        """ prints a message when an instance is
		deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
