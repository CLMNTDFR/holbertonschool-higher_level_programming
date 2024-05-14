#!/usr/bin/python3

def best_score(a_dictionary):

    if not a_dictionary:
        return None

    best_key = None
    best_item = -int('inf')
    #  initialize value with negative infinite integer

    for key, item in a_dictionary.items():
        if item > best_item:
            best_item = item
            best_key = key

    return best_key
