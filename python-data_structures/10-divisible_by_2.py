#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    checked_list = []

    for i in range(len(my_list)):
        if (my_list[i] % 2 == 0):
            checked_list.append(True)

        else:
            checked_list.append(False)

    return checked_list
