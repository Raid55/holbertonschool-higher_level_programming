#!/usr/bin/python3
"""
this module adds int safely
and
yea
"""
def add_integer(a, b):
    """
        Adds numbers together making sure they arrent anything but int or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
