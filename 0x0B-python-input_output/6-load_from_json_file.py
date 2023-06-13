#!/usr/bin/python3
""" The Module runs a script that creates an Object from a JSON file
"""
# Import the Required Module
import json

def load_from_json_file(filename):
    """
	Parameter Explanation:
		- filename - The File to create the
		object from
    """
    with open(filename, 'r') as my_file:
        my_data = json.loads(my_file)
        return my_data
    
