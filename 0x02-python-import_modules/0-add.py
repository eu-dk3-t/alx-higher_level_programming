#!/usr/bin/python3
# File name:
#       0-add.py
# Description:
#       Imports the function add
#       from the file add_0.py
# Author:
#       eu-dk3-t

if __name__ == '__main__':
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
