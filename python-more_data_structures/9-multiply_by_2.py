#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dico = a_dictionary.copy()

    for key in new_dico:
        new_dico[key] = new_dico[key * 2]

    return new_dico
