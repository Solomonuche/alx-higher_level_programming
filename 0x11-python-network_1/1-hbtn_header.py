#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in
the header of the response
"""

from urllib.request import Request, urlopen
from sys import argv

if __name__ == "__main__":
    req = Request(argv[1])
    with urlopen(req) as response:
        res = response.headers

        print(res['X-Request-Id'])