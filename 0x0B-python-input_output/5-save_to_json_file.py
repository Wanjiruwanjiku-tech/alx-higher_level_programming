#!/usr/bin/python3
""" This Module runs a Script that writes an Object to a 
    text file, using a JSON representation
"""
# Import the Necessary Module
import json

def save_to_json_file(my_obj, filename):
    """
	Parameter Explanation:
		- my_obj - The object to serialize
		- filename - The file to write to

	The with statement has to be used to ensure
	effective closure of the file
    """

    with open(filename, "w") as my_file:
        json_str = json.dumps(my_obj)
        my_file.write(json_str)
