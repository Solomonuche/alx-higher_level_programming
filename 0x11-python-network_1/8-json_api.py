#!/usr/bin/python3
"""
Requests exception handling
"""

import requests
from sys import argv

if __name__ == "__main__":

    q = argv[1] if len(argv) > 1 else ""

    # Make request
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        json_data = r.json()
        if json_data:
            user_id = json_data.get('id')
            user_name = json_data.get('name')

            print(f'[{user_id}] {user_name}')
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
