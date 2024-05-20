#!/usr/bin/python3
"""

This module print a text with 2 new lines after each
of these characters: ".", "?" and ":"

"""


def text_indentation(text):
    """Function that print a text with 2 new lines after each
        of these characters: ".", "?" and ":"

    Args:
        text: the text to print

    Returns:
        No returns

    Raises:
        TypeError: if text is not a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_char = {".", "?", ":"}
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in special_char:
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    print(result, end="")
