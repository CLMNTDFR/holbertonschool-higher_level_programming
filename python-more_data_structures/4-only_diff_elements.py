#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff_items = set_1.symmetric_difference(set_2)
    #  .symmetric_difference is a native function in python that returns
    #  only the differents elements between two lists
    return diff_items
