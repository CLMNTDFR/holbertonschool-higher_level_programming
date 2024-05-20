#!/usr/bin/python3
"""
Module composed by a function that prints 2 new lines after ".?:" characters
"""


def text_indentation(text):
    """Function that prints 2 new lines after ".?:" characters

    Args:
        text: input string

    Returns:
        No return

    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initial empty string to accumulate the result
    result = ""

    # Iterate through each character in the input text
    for char in text:
        # Add the character to the result
        result += char
        # If the character is one of the specified punctuation marks, add two new lines
        if char in ".?:":
            result += "\n\n"

    # Print the result, with leading/trailing spaces removed from each line
    print("\n".join([line.strip() for line in result.split("\n")]))
