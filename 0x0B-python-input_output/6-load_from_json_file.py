#!/usr/bin/python3
import json
"""6-load_from_json_file.py module"""


def load_from_json_file(filename):
    """creates objrct from a jason file"""

    with open(filename, 'r+', encoding='utf-8') as json_file:
        obj = json.load(json_file)
    return (obj)
