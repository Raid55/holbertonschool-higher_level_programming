#!/usr/bin/python3
def uniq_add(my_list=[]):
    num = list(set(my_list))[0]
    for i in list(set(my_list))[1:]:
        num += i
    return num
