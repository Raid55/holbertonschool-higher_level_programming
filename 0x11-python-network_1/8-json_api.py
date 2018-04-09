#!/usr/bin/python3
""" posts to api with params """

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        payload = {'q': argv[1]}
    else:
        payload = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        json = r.json()
        if len(json) == 0:
            print('No result')
        else:
            print("[{}] {}".format(json['id'], json['name']))
    except:
        print('Not a valid JSON')
