#!/usr/bin/python3
letter = "a"
for i in range(0, 26):
    print("{}".format(chr(ord(letter) + i)), end="")
