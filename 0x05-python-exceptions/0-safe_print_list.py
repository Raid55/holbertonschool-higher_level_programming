#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0;
    for i in range(0, x):
        num = i
        try:
            print("{}".format(my_list[i]), end="")
        except:
            break;
    print()
    return num