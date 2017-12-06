#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    tmp = number % 10
    print(tmp, end="")
    return int(tmp)
