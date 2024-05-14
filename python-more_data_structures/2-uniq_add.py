#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    #  delet double elements with set
    return sum(uniq_list)  # sum is a native function in python
