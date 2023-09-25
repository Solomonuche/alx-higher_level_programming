#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{}".format(value))
    except Exception:
        print("{}".format(value))
        return False
    return True
