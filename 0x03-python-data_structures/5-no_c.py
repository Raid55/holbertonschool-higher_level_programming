#!/usr/bin/python3
def no_c(my_string):
    new_str= ""
    for x in range(0, len(my_string)):
        if my_string[x] == 'c' or my_string[x] == 'C':
            continue;
        else:
            new_str += my_string[x]
    return new_str
