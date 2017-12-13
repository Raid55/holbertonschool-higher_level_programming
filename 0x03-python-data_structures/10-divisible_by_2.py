#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bol_list = []
    for x in my_list:
        if x % 2 == 0:
            bol_list.append(True)
        else:
            bol_list.append(False)
    return bol_list
