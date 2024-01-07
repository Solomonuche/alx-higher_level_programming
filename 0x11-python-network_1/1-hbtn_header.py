#!/usr/bin/python3
""" Response header value"""

from urllib.request import Request, urlopen
from sys import argv

req = Request(argv[1])
if __name__ == "__main__":
    with urlopen(req) as response:
        res = response.headers

        print(res['X-Request-Id'])
