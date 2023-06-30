#!/usr/bin/python3
"""10-my_github.py module"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passw = sys.argv[2]
    url = "https://api.github.com/user"
    headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': f'Token {passw}'
            }
    response = requests.get(url, headers=headers, auth=(user, passw))
    data = response.json()
    print("{}".format(data['id']))
