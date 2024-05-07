#!/usr/bin/python3
def uppercase(str):
    for i in str:  # iterate index until end of string
        if (ord(i) <= 122) and (ord(i) >= 97):  # check if is lowercase ASCII
            i = chr(ord(i) - 32)  # convert to uppercase
        print("{:s}".format(i), end="")  # print and skip new line
    print("")  # print new line
