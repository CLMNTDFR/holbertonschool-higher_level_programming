#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_items = set_1.intersection(set_2)
    #  .intersection is a native function in python that checks common
    #  elements between two lists
    return common_items
