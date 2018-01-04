#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Just a Square class
"""
class Square:
    """ a square class
    """
    def __init__(self, size=0):
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

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

    def my_print(self):
        """ prints hashtag squar """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for x in range(0, self.__size):
                    print("#", end="")
                print()
    pass
