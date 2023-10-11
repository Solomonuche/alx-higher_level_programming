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

    def to_json(self):
        """
        method that retrieves a dictionary
        """

        return Student.__dict__
