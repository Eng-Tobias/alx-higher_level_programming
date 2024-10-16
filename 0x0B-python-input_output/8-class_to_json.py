# 8-class_to_json.py
#!/usr/bin/python3
def class_to_json(obj):
    """Returns the dictionary description of an object for JSON serialization."""
    result = {}
    for attribute, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[attribute] = value
    return result
