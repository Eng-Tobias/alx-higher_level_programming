#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{} is divisible by 2: {}".format(my_list[i], list_result[i]))
    i += 1
