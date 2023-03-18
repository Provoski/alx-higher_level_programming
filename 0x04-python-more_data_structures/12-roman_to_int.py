#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    roman_dict_special = {"V" : 4, "X" : 9}
    int_val = 0
    temp = ""
    roman_fig = ""
    special = iter(roman_string)
    for count in range(0, len(roman_string)):
        for count2 in range (1, len(roman_string), 2):
            if count2 in roman_dict_special:
                int_val += roman_dict_special[temp]
                count += 2
                break
        roman_fig = roman_string[count]
        int_val += roman_dict[roman_fig]
        count += 1
    return int_val
