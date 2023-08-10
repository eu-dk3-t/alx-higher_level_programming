#!/usr/bin/python3
# File name:
#       4-hidden_discovery.py
# Description:
#       Prints names defined
#       by the hidden_4 module
# Author:
#       eu-dk3-t
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
