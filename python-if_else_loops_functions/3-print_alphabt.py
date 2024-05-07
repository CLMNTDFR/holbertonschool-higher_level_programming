#!/usr/bin/python3
for i in range(97, 123):  # 97 = 'a' and 122 = 'z'
    if (i != 101) and (i != 113):
        print("{:s}".format(chr(i)), end="")
        # chr convert number to ASCII character
        # end="" used to skip auto new-line
