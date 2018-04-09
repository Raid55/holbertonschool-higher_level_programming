#!/usr/bin/python3
""" pings github """

import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    r = request.get('https://api.github.com/users/' + argv[1],
                    auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))
