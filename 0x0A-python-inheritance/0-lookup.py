#!/usr/bin/python3
"""
A module that returns a list of attributes
"""


def lookup(obj):
        """
        A function that returns the list of available
        attributes and methods of an object
        """
                    
        return (dir(obj))
