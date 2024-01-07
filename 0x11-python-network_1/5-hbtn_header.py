#!/usr/bin/python3
"""
Response header value
"""

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    header = response.headers

    print(header['X-Request-Id'])
