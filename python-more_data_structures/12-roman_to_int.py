#!/usr/bin/python3


def roman_to_int(roman_string):
    #  isinstance is a native python's function that check if an object
    #  is, in this case, a string. That return 'True' or 'False'
    if not isinstance(roman_string, str):
        return 0

    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    length = len(roman_string)

    #  iterate across the string through penultimate character:
    for i in range(length - 1):
        current_value = roman_values[roman_string[i]]
        next_value = roman_values[roman_string[i + 1]]

        if current_value < next_value:
            result -= current_value

        elif current_value > next_value:
            result += current_value

        #  adding the value of the last character:
        result += roman_values[roman_string[-1]]

        return result
