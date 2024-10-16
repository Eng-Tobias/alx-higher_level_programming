#!/usr/bin/python3
"""
Module that defines the function `load_from_json_file`
"""


import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object represented by the JSON data.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
