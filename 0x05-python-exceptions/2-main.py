#!/usr/bin/python3
safe_print_dict = __import__('2-safe_print_dict').safe_print_dict

a_dict = { 'name': 'John', 'age': 25, 'city': 'New York' }
nb_printed = safe_print_dict(a_dict, 2)
print("nb_printed: {}".format(nb_printed))
