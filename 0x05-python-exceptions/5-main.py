#!/usr/bin/python3
raise_exception_msg = __import__('5-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("This is a NameError message")
except NameError as e:
    print("Exception raised: {}".format(e))
