#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Attempt to divide the elements
            division_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0  # Default value for division by zero
        except TypeError:
            print("wrong type")
            division_result = 0  # Default value for wrong type
        except IndexError:
            print("out of range")
            division_result = 0  # Default value for out of range
        finally:
            # Append the result (whether it was successful or a default value)
            result.append(division_result)
    return result
