#!/usr/bin/python3
""" getting from star wars api """

import requests
from sys import argv


if __name__ == "__main__":
    payload = {'search': argv[1]}
    r = requests.get('https://swapi.co/api/people', params=payload)
    try:
        json = r.json()
        # print(json)
        print("Number of results: {}".format(json['count']))
        for n in json['results']:
            print(n['name'])
    except:
        print('Not a valid JSON')
