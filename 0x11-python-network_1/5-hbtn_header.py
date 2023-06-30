#!/usr/bin/python3
"""4-hbtn_status.py module"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    header = response.headers
    request_id = header.get('X-Request-Id')
    print("{}".format(request_id))
