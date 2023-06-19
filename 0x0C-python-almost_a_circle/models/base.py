#!/usr/bin/python3
""" This Module runs a script that defines a class """

import json

class Base:

    """ Class Definition of class Bas

        private class attribute __nb_objects = 0
        class constructor: def __init__(self, id=None)
    """
    __nb_objects = 0 #Private Class attr

    def __init__(self, id=None):
        """
            The class Constructor:
            The Method assigns the public instance atrr id

            The id parameter is an integer
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ The Method returns a json str repr """
        if list_dictionaries is None or bool(list_dictionaries) is False:
            return "[]"
        else:
            json_str = json.dumps(list_dictionaries)
        return json_str

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the json string """
        filename = "{}.json".format(cls.__name__)
        list_dictionaries = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                list_dictionaries.append(dictionary)
            json_str = Base.to_json_string(list_dictionaries)

        with open(filename, 'w',) as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(json_str)
