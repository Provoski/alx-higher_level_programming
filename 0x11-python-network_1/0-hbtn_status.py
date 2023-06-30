#!/usr/bin/python3
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read()

body_type = type(body)
content = body.decode('utf-8')

print("Body response:")
print("\t- type: {}".format(body_type))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(content))
