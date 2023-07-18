#!/usr/bin/python3
"""
   This Module defines a Class
"""
class BaseGeometry:
    """ The Class Definition """
    def area(self):
        """ The Public instance Method raises an Exception 
	    with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value): 
        """ The public instance Method validates
	    a value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
