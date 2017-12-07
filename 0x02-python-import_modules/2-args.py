#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    print("{} arguments{}".format(len(argv)-1, ":" if len(argv) > 1 else "."))
    i = 1
    for x in argv[1:]:
        print("{}: {}".format(i, x))
        i += 1
