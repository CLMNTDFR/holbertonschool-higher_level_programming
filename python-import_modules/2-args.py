#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    num_args = len(argv) - 1

    if (num_args) == 0:
        print("{:d} arguments.".format(num_args))

    elif (num_args) == 1:
        print("{:d} argument:".format(num_args))
        print("1: {:s}".format(argv[1]))

    elif (num_args) > 1:
        print("{:d} arguments:".format(num_args))
        for i in range(1, num_args + 1):
            print("{:d}: {:s}".format(i, argv[i]))
