#!/usr/bin/python3
"""
Requests exception handling
"""

import requests
from requests.exceptions import HTTPError
from sys import argv

if __name__ == "__main__":
    try:
        r = requests.get(argv[1])

        # raise an exception if any else pass
        r.raise_for_status()
        print(r.text)
    except HTTPError as e:
        print(f'Error code: {e.response.status_code}')
