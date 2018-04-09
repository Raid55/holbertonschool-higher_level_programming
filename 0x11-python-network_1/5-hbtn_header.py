#!/usr/bin/python3
""" uses requests lib to make req and get header """

import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
