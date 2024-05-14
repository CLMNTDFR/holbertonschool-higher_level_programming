#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    #  Create a copy to protect contains of original list
    keys_list = list(a_dictionary.keys())

    #  Iterate on the copy
    for key in keys_list:
        #  Check if the current value is the value to delete
        if a_dictionary[key] == value:
            del a_dictionary[key]

    return a_dictionary
