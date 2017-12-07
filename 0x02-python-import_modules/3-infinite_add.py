#!/usr/bin/python3
from sys import argv
count = 0
for x in argv[1:]:
    count += int(x)
print("{}".format(count))
