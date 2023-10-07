#!/usr/bin/python3
"""
Text indentation module
"""


def text_indentation(text):
    """
    Text indentation - a function that prints a text with
    2 new lines after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()

    _list = []
    for i in text:
        if i in ('.', '?', ':'):
            _list.extend([i, '\n' * 2])
        else:
            _list.append(i)
    print(''.join(_list))
