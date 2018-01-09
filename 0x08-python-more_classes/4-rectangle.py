#!/usr/bin/python3
"""
    rectangle
"""
class Rectangle():
    """ rect class
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def __str__(self):
        rendstr = ""

        for i in range(0, self.height):
            for j in range(0, self.width):
                rendstr += '#'
            if i is not self.height - 1:
                rendstr += '\n'
        return rendstr

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__,
                self.width, self.height)
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise typeerror("width must be an integer")
        if value < 0:
            raise valueerror("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise typeerror("height must be an integer")
        if value < 0:
            raise valueerror("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

