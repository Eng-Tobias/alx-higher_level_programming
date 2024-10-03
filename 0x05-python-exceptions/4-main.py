#!/usr/bin/python3
raise_exception = __import__('4-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as e:
    print("Exception raised: {}".format(e))
