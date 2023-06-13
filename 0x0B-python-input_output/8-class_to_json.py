#!/usr/bin/python3
"""
   This Module runs a Script that that returns the 
   dictionary description with simple data structure
   (list, dictionary, string, integer and boolean
   for JSON serialization of an object
"""
def class_to_json(obj):

    return obj.__dict__
