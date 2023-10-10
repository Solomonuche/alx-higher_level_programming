#!/usr/python3
"""
Read file module
"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF8) and prints it to stdout
    """

    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
        print(data, end='')
