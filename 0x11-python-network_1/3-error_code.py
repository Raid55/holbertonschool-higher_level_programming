#!/usr/bin/python3
""" makes request and handles error """

import urllib
from sys import argv

if __name__ == "__main__":
    try:
        req = urllib.request.Request(argv[1])
        with urllib.request.urlopen(req) as page:
            print(page.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code:", e.code)
