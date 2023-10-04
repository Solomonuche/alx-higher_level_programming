#!/usr/bin/python3
"""
LockedClass representation
"""


class LockedClass:
    """
    Class definition
    """

    def __setattr__(self, name, value):
        """ Set atrribute """

        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError(f"'{type(self).__name__}' object"
                                 f" has no attribute '{name}'")
