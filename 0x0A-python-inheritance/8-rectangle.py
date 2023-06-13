#!/usr/bin/python3
""" 
    This Module runs a subclass of the BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
#Import the class BaseGeometry from the Module

class Rectangle(BaseGeometry):

    """ This derived class inherits from BaseGeometry """
    #Constractor
    def __init__(self, width, height):
        """ - This Method initializes the class with 
	    the arguments width and height
	    - They both have to be private with no getter
	    or setter.
	    - both values must be validated  by
	    integer_validator
        """
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
