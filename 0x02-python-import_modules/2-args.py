#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv)
    plural = "s" if argc != 2 else ""
    print("{} argument{}{}".format(argc - 1, plural, ":" if argc > 1 else "."))
    i = 1
    for x in argv[1:]:
        print("{}: {}".format(i, x))
        i += 1
