#!/usr/bin/python3
def append_write(filename="", text=""):
    finNum = 0    
    with open(filename, "a+") as f:
        for l in text:
            finNum += 1
            f.write(l)
    return finNum
