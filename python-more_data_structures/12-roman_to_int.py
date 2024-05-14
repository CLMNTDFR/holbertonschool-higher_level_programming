#!/usr/bin/python3


def to_subtract(subtract_tmp):
    """
    Calculates the final value to be added to the result by subtracting
    all smaller values from the largest value in the list.
    """
    to_sub = 0
    max_list = max(subtract_tmp)

    # Sum all values less than the maximum to subtract from the max
    for n in subtract_tmp:
        if max_list > n:
            to_sub += n

    return max_list - to_sub


def roman_to_int(roman_string):
    """
    Converts a Roman numeral string to an integer.
    If the input string is not valid (not a string or None), returns 0.
    """
    # Validate the input
    if not roman_string or not isinstance(roman_string, str):
        return 0

    # Mapping of Roman numerals to their integer values
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    available_keys = list(roman_values.keys())

    result = 0
    last_rom = 0
    subtract_tmp = [0]

    # Process each character in the Roman numeral string
    for char in roman_string:
        for r_num in available_keys:
            if r_num == char:
                # Check the value against the last seen Roman numeral value
                if roman_values[char] <= last_rom:
                    # If current is less or equal, calculate interim result and reset list
                    result += to_subtract(subtract_tmp)
                    subtract_tmp = [roman_values[char]]
                else:
                    # Otherwise, append the value for potential subtraction
                    subtract_tmp.append(roman_values[char])

                last_rom = roman_values[char]

    # Add the result of the last sequence of values
    result += to_subtract(subtract_tmp)

    return result
