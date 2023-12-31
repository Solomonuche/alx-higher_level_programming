#!/usr/bin/python3
"""
Geometry module
"""


class BaseGeometry:
    """
    Geometry class representation.
    """

    def area(self):
        """Area method"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator method"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
