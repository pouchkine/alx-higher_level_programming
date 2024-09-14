#!/usr/bin/python3

import urllib.request

request = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(request) as response:
    type_content = response.read()
    type_response = type(type_content)
    type_utf = str(type_content)[2:-1]
    print(f'    - type: {type_response}')
    print(f'    - content: {type_content}')
    print(f'    - utf8 content: {type_utf}')
