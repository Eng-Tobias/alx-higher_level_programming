#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple((1, 2), (3, 4)))
print(add_tuple((1, 2, 3), (4, 5, 6)))
print(add_tuple((1,), (3,)))
