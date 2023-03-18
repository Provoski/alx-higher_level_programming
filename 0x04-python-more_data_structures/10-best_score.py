#!/usr/bin/python3
def best_score(a_dictionary):
    max_key = 0
    if a_dictionary is None:
        return None
    if len(a_dictionary) == 0:
        return None
    for k, v in a_dictionary.items():
        if v > max_key:
            max_key = v
            key = k
    return key
