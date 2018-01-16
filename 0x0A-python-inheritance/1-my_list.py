#!/usr/bin/python3
"""
    mylist class
"""
class MyList(list):
    """a class based on list
    """
    def print_sorted(self):
        print(sorted(self))
