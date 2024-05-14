#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    #  keep the key and multiplies the item by two
    new_dico = {key: item * 2 for key, item in a_dictionary.items()}

    return new_dico
