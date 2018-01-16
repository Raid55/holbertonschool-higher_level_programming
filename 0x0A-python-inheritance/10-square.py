#!/usr/bin/python3
"""
square class
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """square class
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
