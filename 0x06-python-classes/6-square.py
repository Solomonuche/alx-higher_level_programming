#!/usr/bin/python3
"""Create and initilize and instance of a class."""


class Square:
    """
    This class defines a class.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        The __init__ method initializes the instance attribute of the class.

        Args:
            size: private instance attribute.
            position: tuple with 2 positive integers
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Position getter method.

        Return:
            position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        A method that sets the private instance of the class and
        validate position.
        """
        if isinstance(value, tuple) and len(value) == 2 and \
                isinstance(value[0], int) and isinstance(value[1], int) and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        A public instance method that prints in stdout
        the square with the character.
        """
        for _ in range(self.__position[1]):
            print()
        if self.__size > 0:
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
        else:
            print()
