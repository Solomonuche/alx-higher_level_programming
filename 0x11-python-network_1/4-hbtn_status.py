#!/usr/bin/python3
"""
Fetching url with request module
"""

import requests

response = requests.get('https://alx-intranet.hbtn.io/status')
# response contains the body in bytes, convert to str by <.text>
body = response.text
print('Body response:')
print(f'\t- type: {type(body)}')
print(f'\t- content: {body}')
