#!/usr/bin/python3

def safe_print_dict(a_dictionary, n=0):
    count = 0
    for index, (key, value) in enumerate(a_dictionary.items()):
        if index < n:
            try:
                print("{}: {}".format(key, value))
                count += 1
            except Exception:
                continue
    return count
