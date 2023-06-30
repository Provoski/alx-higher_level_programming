#!/usr/bin/python3
"""4-hbtn_status.py module"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    response = requests.post(url, data=data)
    body = response.text
    print("{}".format(body))
