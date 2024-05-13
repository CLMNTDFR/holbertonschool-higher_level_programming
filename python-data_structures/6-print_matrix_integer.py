#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix or matrix == [[]]:
        print("")

    else:
        for row in matrix:
            for element in row:
                print("{:d}".format(element), end=" ")
            print()
