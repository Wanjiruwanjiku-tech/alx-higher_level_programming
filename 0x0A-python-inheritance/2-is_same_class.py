#!/usr/bin/python3
""" This Module runs a function that checks if an object
	is indeed an instance of a specified class
"""
def is_same_class(obj, a_class):
    """ The function returns:
		True if true
		False if false
	Arguments:
		obj - The object to check
		a_class - Specified class.
    """
    return type(obj) == a_class
