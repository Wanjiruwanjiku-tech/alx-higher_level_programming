#!/usr/bin/python3
""" The Script defines a class """

class Student:
    """
	The Class Represents a Student
    """
    def __init__(self, first_name, last_name, age):
        """ Class Initialization """
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

    def reload_from_json(self, json):
        """ The Public Method replaces all attributes 
            of the Student instance
        """
        for key, val in json.items():
            setattr(self, key, val)
