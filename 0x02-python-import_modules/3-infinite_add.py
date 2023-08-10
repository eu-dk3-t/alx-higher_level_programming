#!/usr/bin/python3
# File name:
#       3-infinite_add.py
# Description:
#       Prints the addition
#       of all args
# Author:
#       eu-dk3-t

if __name__ == "__main__":
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
