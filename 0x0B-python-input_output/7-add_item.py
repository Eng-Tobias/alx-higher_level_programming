#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file.
"""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = 'add_item.json'

# Load existing items from the file if it exists, otherwise create an empty
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add command line arguments (excluding the script name) to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
