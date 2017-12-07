#!/usr/bin/python3
argv = __import__("sys").argv
count = 0
for x in argv[1:]:
    count += int(x)
print("{}".format(count))
