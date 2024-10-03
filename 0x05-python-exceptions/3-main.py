#!/usr/bin/python3
safe_print_list_integers = __import__('3-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 'Hello', 3, 4]
nb_printed = safe_print_list_integers(my_list, 5)
print("nb_printed: {}".format(nb_printed))
