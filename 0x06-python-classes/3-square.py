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
    pass
