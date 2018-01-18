#!/usr/bin/python3
def write_file(filename="", text=""):
    with open("my_first_file.txt", "w") as file:
        file.write(text)
