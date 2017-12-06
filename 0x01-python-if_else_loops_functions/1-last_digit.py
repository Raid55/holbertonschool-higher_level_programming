#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNum = ""
if number < 0 and (number % 10) != 0:
    lastNum = str(number)[0]
lastNum = lastNum + str(number)[-1:]
loadedStr = "Last digit of {:d} is {}".format(number, lastNum)
if int(lastNum) > 5:
    print("{} and is greater than 5".format(loadedStr))
elif int(lastNum) == 0:
    print("{} and is 0".format(loadedStr))
else:
    print("{} and is less than 6 and not 0".format(loadedStr))
