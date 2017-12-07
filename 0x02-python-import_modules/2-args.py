#!/usr/bin/python3
from sys import argv
print("{} arguments{}".format(len(argv) - 1, ":" if len(argv) > 1 else "."))
i = 0
for x in argv:
    if i == 0:
        i += 1
        continue
    print("{}: {}".format(i, x))
    i += 1
