#!/usr/bin/python3
def write_file(filename="", text=""):
    with open("my_first_file.txt", "w") as f:
        return f.write(text)
