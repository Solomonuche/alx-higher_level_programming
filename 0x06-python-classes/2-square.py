#!/usr/bin/python3
"""Create and initilize and instance of a class."""


class Square:
    """
    This class defines a class.
    """
    def __init__(self, size=0):
        """
        The __init__ method initializes the instance attribute of the class.

        Args:
            size: private instance attribute.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
