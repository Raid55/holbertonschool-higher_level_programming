#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename) as file:
        if nb_lines <= 0:
            print(file.read(), end="")
        else:
            for i in range(0, nb_lines):
                print(file.readline(), end="")
