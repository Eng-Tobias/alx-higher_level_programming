#!/usr/bin/python3
update_dictionary = __import__('11-multiply_by_2').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14}
print_sorted_dictionary(a_dictionary)

update_dictionary(a_dictionary, 'John', 89)
print("--")
print_sorted_dictionary(a_dictionary)

update_dictionary(a_dictionary, 'Sarah', 40)
print("--")
print_sorted_dictionary(a_dictionary)
