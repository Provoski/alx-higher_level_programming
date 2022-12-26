#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    flag = True
    try:
        result = a/b
        return (result)
    except ZeroDivisionError as e:
        flag = False
    finally:
        if flag:
            print("Inside result: {:.1f}".format(result))
        else:
            print("Inside result: None")
    return (None)
