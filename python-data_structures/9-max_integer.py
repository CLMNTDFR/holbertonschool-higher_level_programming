#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    current_max = my_list[0]
    for num in my_list[1:]:
        if num > current_max:
            current_max = num

    return current_max
