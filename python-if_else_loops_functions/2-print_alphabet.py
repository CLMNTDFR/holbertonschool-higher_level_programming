#!/usr/bin/python3
str = ""  # initialize empty variable for string
for letter in range(97, 123):
    str += chr(letter)  # chr convert number to ASCII character
print("{}".format(str), end="")  # end="" used to skip auto new-line
