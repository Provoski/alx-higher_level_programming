#!/usr/bin/python3
"""7-error_code.py module"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    status = response.status_code
    if status >= 400:
        print("Error code:{}".format(status))
    else:
        body = response.text
        print("{}".format(body))
