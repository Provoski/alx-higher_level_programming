#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    list_lenght = 0
    item = 0
    for i in my_list:
        list_lenght += 1
    for item in range(x):
        if isinstance(my_list[item], int):
            print(my_list[item], end="")
            count += 1
    print()
    return count
