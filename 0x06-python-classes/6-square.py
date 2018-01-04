#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Just a Square class
"""
class Square:
    """ a square class
    """
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if len(position) == 2 and \
                all(isinstance(item, int) for item in position) and \
            all(True if num >= 0 else False for num in position):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ calcs area """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position
    @position.setter
    def poition(self, value):
        if len(value) == 2 and \
                all(isinstance(item, int) for item in value) and \
                all(True if num >= 0 else False for num in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """ prints hashtag squar """
        if self.__size == 0:
            print()
        else:
            for yMarg in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for zMarg in range(0, self.__position[0]):
                    print(" ", end="")
                for x in range(0, self.__size):
                    print("#", end="")
                print()
    pass
