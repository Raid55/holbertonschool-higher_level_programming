#!/usr/bin/python3
def append_write(filename="", text=""):
    finNum = 0    
    with open(filename, "a+") as file:
        for l in text:
            finNum += 1
            file.write(l)
    return finNum
