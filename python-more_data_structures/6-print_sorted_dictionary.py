#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    #  sorts keys of a dictionary by alphabetic order
    sorted_keys = sorted(a_dictionary.keys())
    #  iterate across the new dictionary by key's values
    for key in sorted_keys:
        print("{:s}: {}".format(key, a_dictionary[key]))
