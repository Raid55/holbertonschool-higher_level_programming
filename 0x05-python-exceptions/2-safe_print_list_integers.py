#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except IndexError as err:
            print("{:d}".format(my_list[i]), end="")
            break
        except:
            continue
        num += 1
    print()
    return num
