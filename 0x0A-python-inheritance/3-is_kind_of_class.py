#!/usr/bin/python3
""" This Module runs a function that returns True
	if the object is an instance of, or if the object 
	is an instance of a class that inherited from, 
	the specified class ; otherwise False
"""
def is_kind_of_class(obj, a_class):
    """ Arguments:
		obj - The the object to check
		a_class - The specified class
    """
    is_it = isinstance(obj, a_class)
    return is_it
