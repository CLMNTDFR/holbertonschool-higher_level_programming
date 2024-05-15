#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            #  Try to divides elements
            result = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError:
            #  Check if one element is zero
            result = 0
            print("division by 0")

        except IndexError:
            #  Check if list_length is out of range
            result = 0
            print("out of range")

        except (TypeError, ValueError):
            #  Check if element is been an integer or a float type
            result = 0
            print("wrong type")

        finally:
            #  Add the final result to the empty list 'new_list'
            new_list.append(result)

        return new_list
