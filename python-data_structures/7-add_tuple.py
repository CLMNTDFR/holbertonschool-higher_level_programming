#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        first_element_a = tuple_a[0]
        second_element_a = tuple_a[1]

    else:
        first_element_a = tuple_a[0] if len(tuple_a) > 0 else 0
        second_element_a = 0

    if len(tuple_b) >= 2:
        first_element_b = tuple_b[0]
        second_element_b = tuple_b[1]

    else:
        first_element_b = tuple_b[0] if len(tuple_b) > 0 else 0
        second_element_b = 0

    return (first_element_a + first_element_b, second_element_a + second_element_b)
