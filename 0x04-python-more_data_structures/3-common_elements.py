#!/usr/bin/python3
def common_elements(set_1, set_2):
    return [x for x in set_1 if True for i in set_2 if x == i]
