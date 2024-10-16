#!/usr/bin/python3
# Function to convert a class instance to a JSON-compatible dictionary.

def class_to_json(obj):
    """Returns the dictionary description of a simple data structure
    for JSON serialization."""
    return {key: value for key, value in obj.__dict__.items()
            if isinstance(value, (list, dict, str, int, bool))}
