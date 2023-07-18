#!/usr/bin/python3
"""This Module defines a class that inherits from
another class
"""

class MyList(list):
    """ The class is a subclass of the builtin class
	list
    """
    def print_sorted(self):
        """The Function prints a sorted list"""
        print(sorted(self))
