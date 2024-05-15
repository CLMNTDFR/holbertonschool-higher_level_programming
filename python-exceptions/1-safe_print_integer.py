#!/usr/bin/python3


def safe_print_integer(value):
    """
    Attempts to print the provided value as an integer.

    Args:
        value (any): The value to be printed as an integer.

    Returns:
        bool: True if the value was successfully printed as an integer, otherwise False.
    """
    try:
        # Try to format and print the value as an integer
        print("{:d}".format(value))
        # If successful, return True
        return True
    except ValueError:
        # Handle the case where the value cannot be formatted as an integer
        return False
    except TypeError:
        # Handle the case where the type of the value is not suitable for integer formatting
        return False
