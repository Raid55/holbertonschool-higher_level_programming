#!/usr/bin/python3
""" makes request and handles error """

from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    try:
        req = Request(argv[1])
        with urlopen(req) as page:
            print(page.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.code)
