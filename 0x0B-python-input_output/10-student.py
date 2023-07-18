#!/usr/bin/python3
""" The script defines a class """

class Student:
    """ Defines a Stufent """
    def __init__(self, first_name, last_name, age):
        """Initialization"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """ Retrieves a dictionary representation of a 
	Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: val for key, val in self.__dict__.items() if key in attrs}
