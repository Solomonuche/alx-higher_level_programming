#!/usr/bin/python3
"""
POST an email
"""

import requests
from sys import argv

if __name__ == "__main__":
    data = {'email': argv[2]}
    response = requests.post(argv[1], data=data)
    print(response.text)
