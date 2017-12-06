#!/usr/bin/python3
letter = "a"
for i in range(0, 26):
    tmp = chr(ord(letter) + i)
    if tmp != "q" and tmp != "e":
        print("{}".format(tmp), end="")
