#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(i for i in my_list)
    result = 0
    for i in my_set:
        result += i
    return result
