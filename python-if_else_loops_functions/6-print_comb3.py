#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 10):
        if (i == j) or (i > j):
            continue
        else:
            print("{}{}".format(i, j), end="")
            if i + j != 17:
                print(", ", end="")
print("")
