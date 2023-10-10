#!/usr/bin/python3
"""
Load, add, save module

a script that adds all arguments to a Python list, and
then save them to a fil
"""
import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

mylist = list()

try:
    mylist = load_from_json_file("add_item.json")
except Exception:
    pass
if len(argv) == 0:
    save_to_json_file(mylist, "add_item.json")
else:
    for i in range(1, len(argv)):
        mylist.extend([argv[i]])
    save_to_json_file(mylist, "add_item.json")
    load_from_json_file("add_item.json")
