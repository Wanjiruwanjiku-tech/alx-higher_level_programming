#!/usr/bin/python3

""" THIS MODULE RUNS A FUNCTION THAT RETURNS
	A LIST OF ATTRIBUTES AND METHODS
"""
def lookup(obj):
    my_list = []
    my_list = dir(obj)
    return my_list
