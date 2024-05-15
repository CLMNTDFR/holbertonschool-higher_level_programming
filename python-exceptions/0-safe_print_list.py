#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    nb_printed = 0

    for i in range(x):
        try:
            print(my_list[i], end="")
            nb_printed += 1  # Increments only if printing succeeds

        except IndexError:
            break  # Exit the loop if loop is out of range

    print()  # Print a new line
    return nb_printed
