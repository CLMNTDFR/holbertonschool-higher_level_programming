#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    nb_printed = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list), end="")
            nb_printed += 1

        except IndexError:
            break  # Exit the loop if loop is out of range

        except ValueError:
            continue

    print()  # Print a new line
    return nb_printed
