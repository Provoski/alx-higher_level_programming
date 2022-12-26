#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a/b
        return (result)
    except:
        return (None)
    finally:
        if result > 0:
            print("Inside result: {:.1f}".format(result))
        else:
            print("Inside result: None")
