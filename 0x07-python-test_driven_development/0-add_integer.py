#1/usr/bin/python3
"""
Add integer function definition
"""


def add_integer(a, b=98, *args):
    """ Addition module, return a + b"""
    if len(args) >= 1:
        raise TypeError("add_integer() takes 1 or 2 positional argument, but ... were given")

    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if a == None:
        raise TypeError("add_integer() missing 1 required positional argument: 'a'")
    if isinstance(a, bool):
        raise TypeError("a must be an integer")
    if isinstance(b, bool):
        raise TypeError("b must be an integer")

    return a + b
