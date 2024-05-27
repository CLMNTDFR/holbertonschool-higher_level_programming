#!/usr/bin/python3

"""reads a file"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults
        to an empty string.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
