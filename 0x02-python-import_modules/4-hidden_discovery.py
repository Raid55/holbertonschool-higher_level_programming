#!/usr/bin/python3
import hidden_4 as hid
if __name__ == "__main__":
    for x in dir(hid):
        if x[0:2] != "__":
            print("{}".format(x))
