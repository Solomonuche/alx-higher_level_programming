#!/usr/bin/python3
"""
Representation of class named rectangle
"""


class Rectangle:
    """
    Rectangle class definition
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Instance initialization
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Return the area of a rectangle
        """

        return self.height * self.width

    def perimeter(self):
        """
        Return the perimeter of a rectangle.
        """

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """
        String representation of rectangle class
        """

        if self.width == 0 or self.height == 0:
            return ""

        result = ""
        for i in range(self.height):
            for j in range(self.width):
                result += str(self.print_symbol)
            result += "\n"

        return result[:-1]

    def __repr__(self):
        """
        String representation of rectangle class
        """

        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Class deconstructor
        """

        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")
