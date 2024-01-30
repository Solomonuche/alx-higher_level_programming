#!/usr/bin/python3
"""
Urllib library error handling
"""

from urllib.request import Request, urlopen
import urllib.error
from sys import argv

if __name__ == "__main__":
    try:
        req = Request(argv[1])
        with urlopen(req) as response:
            res = response.read()

            print(res.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
