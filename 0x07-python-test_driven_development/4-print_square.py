#!/usr/bin/python3
"""
Print square Module
"""


def print_square(size=None, *args):
    """
    Print square - a function that prints a square with the character #
    """

    """ Validate argument length"""
    if len(args) != 0:
        raise TypeError("print_square() expects 1 required positional "
                        "argument but ... were given")

    if size is None:
        raise TypeError("print_square() expects 1 required positional "
                        "argument")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print("#" * size)
