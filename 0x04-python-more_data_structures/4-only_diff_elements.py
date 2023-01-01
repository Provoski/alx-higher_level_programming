#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    uniq_set_1 = set_1 - set_2
    new_set_1 = list(uniq_set_1)
    uniq_set_2 = set_2 - set_1
    new_set_2 = list(uniq_set_2)
    for i in new_set_1:
        new_set_2.append(i)
    return new_set_2
