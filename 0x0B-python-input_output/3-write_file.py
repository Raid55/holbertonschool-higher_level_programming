#!/usr/bin/python3
def write_file(filename="", text=""):
    finNum = 0
    with open("my_first_file.txt", "w") as file:
        for l in text:
            finNum += 1
            file.write(l)
    return finNum
