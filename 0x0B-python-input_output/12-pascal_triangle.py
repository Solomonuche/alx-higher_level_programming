#!/usr/bin/python3
"""
Pascal's Triangle Module
"""


def pascal_triangle(n):
    """
    a function def pascal_triangle(n): that returns a list of lists of
    integers representing the Pascal’s triangle of n
    """

    my_list = list()

    if n <= 0:
        return my_list

    for i in range(n):
        my_list.append([1] * (i + 1))

    for i in range(2, n):
        for k in range(1, i):
            my_list[i][k] = my_list[i - 1][k - 1] + my_list[i - 1][k]

    return my_list
