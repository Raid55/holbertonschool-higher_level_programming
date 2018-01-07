#!/usr/bin/python3
"""
    printing squars for days
    to bad its not chocolate squares
"""
def print_square(size):
    """
        prints a square based on size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
