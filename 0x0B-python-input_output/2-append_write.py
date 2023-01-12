#!/usr/bin/python3
"""2-append_write.py module"""


def append_write(filename="", text=""):
    """a function that append charactes to a text
    file and return the number of character
    added
    """

    text_len = 0
    with open(filename, 'a', encoding='utf-8') as my_file:
        text_len = my_file.write(text)
    return text_len
