#!/usr/bin/python3

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False


def uppercase(str):
    for letter in str:
        if islower(letter):
            letter = chr(ord(letter) - 32)
        print("{}".format(letter), end="")
    print("")
