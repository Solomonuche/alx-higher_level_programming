#!/usr/bin/python3
"""
Representation of class named rectangle
"""


class Rectangle:
    """
    Rectangle class definition
    """

    def __init__(self, width=0, height=0):
        """
        Instance initialization
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter method of private width instance
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter method
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Height Property retriever
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Height property setter
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
