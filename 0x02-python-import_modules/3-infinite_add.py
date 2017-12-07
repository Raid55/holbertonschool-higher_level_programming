#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = 0
    for x in argv[1:]:
        count += int(x)
    print("{}".format(count))
