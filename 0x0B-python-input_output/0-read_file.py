#!/usr/bin/python3
""" This Module runs a function that reads a file and
    Prints its contents to standard output
"""
def read_file(filename=""):
    """ The parmeter filename is initialized to an empty
	string and represents the files name

	A with statement has to be used.
    """
    with open('filename', encoding="UTF8") as my_file:
        for line in my_file:
            print(line, end="")
