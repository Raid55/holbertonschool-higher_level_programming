#!/usr/bin/python3
""" fetches header for request """

import urllib.request
from sys import argv


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as page:
        print(dict(page.info()).get('X-Request-Id'))
