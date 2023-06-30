#!/usr/bin/python3
"""7-error_code.py module"""
import requests
import sys


if __name__ == "__main__":
    length = len(sys.argv)
    if length > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    params = {"q": letter}
    url = "http://0.0.0.0:5000/search_user"

    # Send POST request
    response = requests.post(url, data=params)

    # Check the response
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
