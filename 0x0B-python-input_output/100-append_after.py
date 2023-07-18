#!/usr/bin/python3
""" This Script inserts a line of text to a file, after 
    each line containing a specific string
"""

def append_after(filename="", search_string="", new_string=""):

    """
	Parameters:
		- filename - The file's name
		- search_string - The string to search
		- new_string - String to append

    """
    with open(filename, "r+", encoding="utf-8") as my_file:
        lines = my_file.readlines()
        my_file.seek(0)

        for line in lines:
            my_file.write(line)
            if search_string in line:
                my_file.write(new_string)
        my_file.truncate()
