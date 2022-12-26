#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    lenght = 0
    try:
        for i in my_list:
            lenght += 1
        if (x-1) < lenght:
            for item in my_list[0:x]:
                print(item, end="")
                count += 1
                if count == x:
                    print()
        elif lenght == 0:
            for items in my_list:
                print(items)
        else:
            for items in my_list:
                print(items, end="")
                count += 1
                if count == lenght:
                    print()
    except:
        print("am Error occurred")
    return count
