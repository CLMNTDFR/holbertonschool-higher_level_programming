#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    num_args = len(argv) - 1
    total = 0

    for i in range(1, num_args + 1):
        total += int(argv[i])

    print("{:d}".format(total))
