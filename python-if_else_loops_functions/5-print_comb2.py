#!/usr/bin/python3
for number in range(0, 100):
    if number < 99:
        # ":02d" used to display two character (ex: 00, 09, 33, ...)
        print(f"{number:02d}, ", end="")
    else:
        print(f"{number}")
