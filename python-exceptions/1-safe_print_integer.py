#!/usr/bin/python3


def safe_print_integer(value):
    #  Try to print an integer and return 'True' if operation is successful
    try:
        print("{:d}".format(value))
        return True

    #  If 'value' is not an integer return 'False'
    except:
        return False
