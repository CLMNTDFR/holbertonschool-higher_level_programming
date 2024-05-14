#!/usr/bin/python3

def best_score(a_dictionary):

    if not a_dictionary:
        return None

    max_key = None
    max_item = -int('inf')
    #  initialize value with negative infinite integer

    for key, item in a_dictionary.items():
        if item > max_item:
            max_item = item
            max_key = key

    return max_key
