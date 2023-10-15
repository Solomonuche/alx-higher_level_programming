#!/usr/bin/python3
"""
Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class representation"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Official string representation"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""

        self.setterValidator("width", value)
        self.__size = value
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """A method that assigns an argument to each attribute"""

        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 1:
                    self.__size = self.width = self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
                if i == 0:
                    self.id = args[0]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                elif key == "id":
                    self.id = value

    def to_dictionary(self):
        """ A method that returns the dictionary representation of a Rectangle"""

        return {
               'id': self.id,
               'size': self.__size,
               'x': self.x,
               'y': self.y,
               }
