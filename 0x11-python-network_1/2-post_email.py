#!/usr/bin/python3
""" posts email to params """

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    data = urlencode({'email': argv[2]}).encode('utf-8')
    req = Request(argv[1], data)

    with urlopen(req) as page:
        print(page.read().decode('utf-8'))
