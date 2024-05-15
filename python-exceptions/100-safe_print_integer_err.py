#!/usr/bin/python3


def safe_print_integer_err(value):
    import sys

    try:
        # Try to format and print the value as an integer
        print("{:d}".format(value))
        # If successful, return True
        return True

    except ValueError as e:
        # Handle the case where the value cannot be formatted as an integer
        sys.stderr.write("Exception: {}\n".format(e))
        return False

    except TypeError as e:
        # Handle the case where the type of the value is not suitable for
        #  integer formatting
        sys.stderr.write("Exception: {}\n".format(e))
        return False
