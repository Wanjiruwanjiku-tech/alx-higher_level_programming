#!/usr/bin/python3
""" This Module returns True if the object is an instance 
	of a class that inherited (directly or indirectly)
	from the specified class ; otherwise False
"""
def inherits_from(obj, a_class):
    """ Arguments:
		obj - The object in question
		a_class - The specfied class in question
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
