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
        super().__init__(size, size)

    def area(self):
        """ Area method"""

        return self.__size * self.__size

    def __str__(self):
        """Rectangle class string representation"""

        return f"[Square] {self.__size}/{self.__size}"
