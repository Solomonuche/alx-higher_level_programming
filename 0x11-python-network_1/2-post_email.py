#!/usr/bin/python3
"""
POST an email
"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    # build the value
    value = {'email': argv[2]}
    data = urlencode(value).encode('ascii')

    # Make request
    req = Request(argv[1], data)
    with urlopen(req) as response:
        res = response.read()

        print(res.decode('utf-8'))
