#!/usr/bin/python3
import json
"""5-save_to_json_file.py module"""


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON representation"""

    json_file = json.dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as my_file:
        my_file.write(json_file)
