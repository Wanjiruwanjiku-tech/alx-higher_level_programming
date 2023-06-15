#!/usr/bin/python3

"""
	This Module runs a Script that adds a new 
	attribute to an objec
"""


def add_attribute(obj, attr, value):

    """
		Obj - The object where the attribute will
			be added

		attr - The attribute to add to the object

		value - The value of the new attribute
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
