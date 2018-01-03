#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    finArr = []
    for i in range(0, list_length):
        try:
            divSum = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            divSum = 0.00
        except IndexError:
            print("out of range")
            divSum = 0.00
        except TypeError:
            print("wrong type")
            divSum = 0.00
        finally:
            finArr.append(divSum)
    return finArr


