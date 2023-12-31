#!/usr/bin/python3
"""
Square module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square subclass representation.
    """

    def __init__(self, size):
        """constructor mrthod"""

        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """ Area method"""

        return self.__size * self.__size
