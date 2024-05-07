#!/usr/bin/python3
def uppercase(str):
    for c in str:  # iterate index until end of string
        if (ord(c) >= 97) and (ord(c) <= 122):  # check if is lowercase ASCII
            c = chr(ord(c) - 32)  # convert to uppercase
        print("{:s}.format(c)", end="")  # print and skip new line
    print("")  # print new line
