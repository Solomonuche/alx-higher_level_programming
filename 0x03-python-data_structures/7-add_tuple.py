#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[:2] if len(tuple_a) >= 2 else (0, 0)
    b = tuple_b[:2] if len(tuple_b) >= 2 else (0, 0)
    if len(tuple_a) == 1:
        a = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        b = (tuple_b[0], 0)
    new_tuple = (a[0] + b[0], a[1] + b[1])
    return new_tuple
