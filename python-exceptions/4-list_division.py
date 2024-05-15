#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            #  Try to divides elements
            result = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError:
            #  Check if one element is zero
            print("division by 0")
            result = 0

        except IndexError:
            #  Check if list_length is out of range
            print("out of range")
            result = 0

        except (TypeError, ValueError):
            #  Check if element is been an integer or a float type
            print("wrong type")
            result = 0

        finally:
            #  Add the final result to the empty list 'new_list'
            new_list.append(result)

        return new_list
