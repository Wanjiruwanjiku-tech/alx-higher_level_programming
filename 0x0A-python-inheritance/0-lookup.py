#!/usr/bin/python3

""" THIS MODULE RUNS A FUNCTION THAT RETURNS
	A LIST OF ATTRIBUTES AND METHODS
"""
def lookup(obj):
""" Returns a list of available attributes """
    return dir(obj)
