#!/usr/bin/python3
""" This Module runs a Script that Deserializes
    a JSON representation of an object
"""
import json
# This Module is required to perform desirialization

def from_json_string(my_str):
    """ The Function converts a json represented object
	back to its original state, that is, back to
	its former data structure.

	Parameter Explanation:
		my_str - The string to deserialize
    """

    my_data = json.loads(my_str)
    return my_data
