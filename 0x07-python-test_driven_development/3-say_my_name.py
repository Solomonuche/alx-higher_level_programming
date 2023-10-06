#!/usr/bin/python3
"""
Say my name
"""


def say_my_name(first_name=None, last_name="", *args):
    """
    a function that prints My name is <first name> <last name>
    """

    """ Validate that not more 2 arguments is passed into the functio"""
    if len(args) != 0:
        raise TypeError("say_my_name() expects 1 or 2 positional "
                        "arguments, but ... were given")

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
