#!/usr/bin/python3


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.

    The function reads the content of the file and prints it to the standard output.
    It uses the with statement to ensure the file is properly closed after reading.
    """
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        print(content)
