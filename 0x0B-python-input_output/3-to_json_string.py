#!/usr/bin/python3
""" This Module runs a script that returns the
	JavaScript Object Notation of an object
"""
import json
#The Module is required to perform serialization

def to_json_string(my_obj):
    """
	Parameter Explanation:
		my_obj - The object to get the json format
	The returns the JSON representation of an object 
	(string):
    """

    json_string = json.dumps(my_obj)
    return json_string
