#!/usr/bin/python3
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""7-add_item.py module. adds arguments to a list and save
it as json file
"""


filename = "add_item.json"
num_arg = len(sys.argv)
arg_list = []
for i in range(1, num_arg):
    arg_list.append(sys.argv[i])
save_to_json_file(arg_list, filename) 
load_from_json_file(filename)
