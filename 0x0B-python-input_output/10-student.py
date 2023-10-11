#!/usr/bin/python3
"""
Student to JSON Class representation
"""


class Student:
    """ a class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initiliazer function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        method that retrieves a dictionary
        """

        json_dict = dict()

        if attrs is None:
            return self.__dict__
        elif isinstance(attrs, list):
            for item in attrs:
                if type(item) is str and item in self.__dict__:
                    json_dict[item] = self.__dict__[item]

        return json_dict
