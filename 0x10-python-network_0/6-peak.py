#!/usr/bin/python3
""" finding the peak with python """


def find_peak(list_of_integers):
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    for i in range(0, len(list_of_integers)):
        if i == 0 and list_of_integers[i] > list_of_integers[i + 1]:
            return list_of_integers[i]
        elif (i == len(list_of_integers) - 1 and
                list_of_integers[i] > list_of_integers[i - 1]):
            return list_of_integers[i]
        if (list_of_integers[i] > list_of_integers[i + 1] and
                list_of_integers[i] > list_of_integers[i - 1]):
            return list_of_integers[i]
