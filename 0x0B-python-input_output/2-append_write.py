#!/usr/bin/python3
"""
	This Module runs a function that appends a piece
	of text in a file.
"""
def append_write(filename="", text=""):
    """
	Parameter Explanation:
		- filename=""- This is the files name
		the parameter is initialized to an empty
		string.
		- text="" - This is the piece of txt to
		append. It is also initialized to an empty
		string

	The Function returns the number of characters added
    """
    num_of_chars = 0 #To keep track
    with open(filename, "a", encoding="utf-8") as my_file:
        num_of_chars = my_file.write(text)
        return num_of_chars   
