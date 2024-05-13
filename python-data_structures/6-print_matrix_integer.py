#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    #  loop iteration in row
    for i in range(len(matrix)):
        #  loop iteration in column
        for j in range(len(matrix[i])):
            if j != 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][j]), end='')
        print()
