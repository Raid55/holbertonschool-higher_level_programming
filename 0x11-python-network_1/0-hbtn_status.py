#!/usr/bin/python3
""" requests /status page """

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as page:
        read = page.read()
        print("Body response:")
        print("\t- type:", type(read))
        print("\t- content:", read)
        print("\t- utf8 content:", read.decode('utf-8'))

