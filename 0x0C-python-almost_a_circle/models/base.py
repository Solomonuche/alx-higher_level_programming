#!/usr/bin/python3
"""
Base class
"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None, *args):
        """ Class constructor"""

        if len(args) != 0:
            raise TypeError("Base.__init__() takes from 1 to 2 positional "
                            "arguments but ... were given")

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ A static method that returns the JSON string representation
        of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ A class method that writes the JSON string representation
        of list_objs to a file"""

        filename = f'{type(list_objs[0]).__name__}.json'
        with open(filename, 'w', encoding='utf-8') as file:
            if list_objs is None:
                file.write("[]")
            else:
                mylist = []
                for i in range(len(list_objs)):
                    mylist.append(list_objs[i].to_dictionary())

                jstring = Base.to_json_string(mylist)
                file.write(jstring)

    def from_json_string(json_string):
        """ A static method that returns the list of the JSON
        string representation """

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """  A class method that returns an instance with all
        attributes already set"""

        dummy_rectangle = cls(1, 1)
        dummy_rectangle.update(**dictionary)
        return dummy_rectangle
