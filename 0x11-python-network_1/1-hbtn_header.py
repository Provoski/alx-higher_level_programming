#!/usr/bin/python3
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.headers
    request_id = headers.get('X-Request-Id')

print(request_id)
