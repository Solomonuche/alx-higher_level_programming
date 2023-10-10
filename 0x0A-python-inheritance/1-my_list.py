#!/usr/bin/python3
"""
My list module
"""


class MyList(list):
    """
    My list class representation.
    """

    def print_sorted(self):
        """
        Public instance method: that prints the list,
        but sorted (ascending sort)
        """

        print(sorted(self))
