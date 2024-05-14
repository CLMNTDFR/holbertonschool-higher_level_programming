#!/usr/bin/python3


def weight_average(my_list=[]):
    # Check if the list is empty or the input is not a list
    if not my_list or not isinstance(my_list, list):
        return 0  # Return 0 immediately if the input is invalid

    score_sum = 0
    weight_sum = 0

    for score, weight in my_list:
        score_sum += score * weight  # Add weighted score to the total
        weight_sum += weight  # Add weight to the total weight sum

    return score_sum / weight_sum  # Return the calculated average
