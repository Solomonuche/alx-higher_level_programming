#!/usr/bin/python3
"""
Rectangle class module
"""
from models.base import Base


class Rectangle(Base):
    """ Rectaangle class representation"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def setterValidator(self, name, value):
        """Public instance setter validator"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif name in ("width", "height") and value <= 0:
            raise ValueError(f"{name} must be > 0")
        elif name in ("x", "y") and value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """Area of Rectangle method"""

        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #"""

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def update(self, *args, **kwargs):
        """A method that assigns an argument to each attribute"""

        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 1:
                    self.__width = args[1]
                if i == 2:
                    self.__height = args[2]
                if i == 3:
                    self.__x = args[3]
                if i == 4:
                    self.__y = args[4]
                if i == 0:
                    super().__init__(args[0])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                elif key == "id":
                    super().__init__(value)

    def to_dictionary(self):
        """ A method that returns the dictionary representation
        of a Rectangle"""

        return {
                'id': self.id,
                'width': self.__width,
                'height': self.__height,
                'x': self.__x,
                'y': self.__y,
                }

    def __str__(self):
        """official string representation"""

        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    @property
    def width(self):
        """Width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter"""
        self.setterValidator("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """ height setter"""
        self.setterValidator("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter"""

        return self.__x

    @x.setter
    def x(self, value):
        """ x setter"""

        self.setterValidator("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""

        return self.__y

    @y.setter
    def y(self, value):
        """ y setter"""

        self.setterValidator("y", value)
        self.__y = value
