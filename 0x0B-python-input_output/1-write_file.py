#!/usr/bin/python3
""" This Module runs a function that writes a string to a 
    text file (UTF8) and returns the number of characters
   written
"""

def write_file(filename="", text=""):
    """ Parameters:
		filename - The file's name

		text - The text to write to the file
	Both parameters are empty strings

	The function should:
		- Create a file if it does not exist
		- Overwrite the contents of the file if
		it exists
	A with statement has to be used
	The function returns the number of characters
	writen to the file.
    """
    number_of_chars = 0 #To keep count

    with open(filename, 'w', encoding="utf-8") as file:
        number_of_chars = file.write(text)
        return number_of_chars
