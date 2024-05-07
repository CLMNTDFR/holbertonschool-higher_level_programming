#!/usr/bin/python3
result = ""  # initialize empty variable for string
for ascii in range(97, 123):  # 97 = 'a' and 122 = 'z'
    if chr(ascii) not in ['q', 'e']:  # chr convert number to ASCII character
        result += chr(ascii)  # add letter to final string

print("{}".format(result), end="")  # end="" used to skip auto new-line
