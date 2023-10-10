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

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            self.name = name
            self.value = value
