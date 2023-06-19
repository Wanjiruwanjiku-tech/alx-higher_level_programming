#!/usr/bin/python3
""" This Module Runs a Script that Defines a Subclass of
The Base superclass.
"""

#import the superclass

from base import Base

class Rectangle(Base):

    """ The subclass Rectangle derived from Class Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ The Class Constructor initialzes the classes
        with private instance attributes
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        #Width getter and setter

        @property
        def width(self):
            """ Returns the width """
            return self.__width

        @width.setter
        def width(self, value):
            """ Sets width to value """
            if (type(value) is not int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        #Height getter and setter

        @property
        def height(self):
            """ Returns the height """
            return self.__height

        @height.setter
        def height(self, value):
            """ Sets height to value """
            if (type(value) is not int):
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        # x getter and setter methods

        @property
        def x(self):
            """ Returns x as a private instance attr """
            return self.__x

        @x.setter
        def x(self, value):
            """ Sets x to Value """
            if (type(value) is not int):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be positive")
            self.__x = value

        # Y getter and setter methods

        @property
        def y(self):
            """ Returns y as a private instance attr """
            return self.__y

        @y.setter
        def y(self, value):
            """ Sets y to value """
            if (type(value) is not int):
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be positive")
            self.__y = value


        # Area Method
        def area(self):
            """ Returns area of a rectangle """
            my_area = self.__width * self.__height
            return my_area

        # Display Method
        def display(self):
            """ Displays a rectangle """
            for y in range(self.y):
                print("")
            for row in range(self.__height):
                for x in range(self.x):
                    print(" ", end="")
                for column in range(self.__wigth):
                    print("#", end="")
                print()

        # Str Method
        def __str__(self):
            """ Returns a string representation """
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

        # Update Method
        def update(self, *args, **kwargs):
            """ Assigns an argument to each attr """
            if args:
                attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)

        # To dict Method
        def to_dictionary(self):
            """ Returns the dict representation """
            obj_dict = {'id' : self.id, 'widtb' : self.__width, 'height' : self.__height, 'x' : self.__x, 'y' : self.__y}
            return obj_dict
