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
        self.__size = size

    def area(self):
        """
        A method that calculate and returns the area of a square.

        Return:
             Return the area of the square.
        """
        return self.__size * self.__size
    
    @property
    def size(self):
        """
        Size getter method.
        
        Return:
            Size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        A method that sets the private instance of the class and validate size.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
