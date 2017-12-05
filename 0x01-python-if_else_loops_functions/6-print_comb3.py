#!/usr/bin/python3
i = 0
while i != 9:
	for x in range(i, 10):
		if (i * 10) + x == 89:
			print("{:d}".format((i * 10) + x))
		elif x != i:
			print("{0:02}, ".format((i * 10) + x), end="")
	i += 1
