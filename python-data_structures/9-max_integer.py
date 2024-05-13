#!/usr/bin/python3

def max_integer(my_list=[]):
    
    if len(my_list) == 0:
        return None
    
    else:
        my_list.sort()
        my_list.reverse()
        current_max = my_list[0]
        return current_max
