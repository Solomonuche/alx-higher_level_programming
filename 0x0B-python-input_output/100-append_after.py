#!/usr/bin/python3
"""
Search and update module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    a function that searches for a string and replace it with new sring
    """
    lines = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if search_string in line:
                lines.append(line)
                lines.append(new_string)
            else:
                lines.append(line)

    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)
