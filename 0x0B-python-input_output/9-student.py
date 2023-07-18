#!/usr/bin/python3
""" This Script runs a class """

class Student:
    """
	The class defines a student by:-
		- first_name
		- lastname
		- age
    """
    def __init__(self, first_name, last_name, age):
        #The Constractor

        """ Parameter Explanation:
		- first_name - The students first name
		- last_name - The students last name
		- age - Their age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ The Public Method retrieves a dictionary 
            representation of a Student instance
        """
        return {'first_name' : self.first_name, 'last_name' : self.last_name, 'age' : self.age}
