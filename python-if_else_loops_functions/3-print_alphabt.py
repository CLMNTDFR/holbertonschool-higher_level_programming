#!/usr/bin/python3
result = ""  # initialize empty variable for string
unavailable_letter = {"e", "q"}  # array

for ascii in range(97, 123):  # 97 = 'a' and 122 = 'z'
    letter = chr(ascii)  # chr convert number to ASCII character
    if letter not in unavailable_letter:
        result += letter  # add letter to final string

print("{}".format(result), end="")  # end="" used to skip auto new-line
