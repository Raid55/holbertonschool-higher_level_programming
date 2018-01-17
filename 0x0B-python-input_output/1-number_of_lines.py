#!/usr/bin/python3
def number_of_lines(filename=""):
    num_lines = 0
    with open(filename) as file:
        for line in file:
            num_lines += 1
    return num_lines
