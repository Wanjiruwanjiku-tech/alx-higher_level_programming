#!/usr/bin/python3
""" This Module runs a Derived Class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry
#Import the Superclass

class Rectangle(BaseGeometry): #The Derived Class

    def __init__(self, width, height):
        """ Initialization of the class """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Returns area of rectangle """
        area = self.__width * self.__height
        return area

    def __str__(self):
        """ Returns the print() and str() rep """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)

        return string
