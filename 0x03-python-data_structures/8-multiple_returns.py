#!/usr/bin/python3
# File name:
#       8-multiple_returns.py
# Description:
#       Returns the lenfth of a string 
#       and its first character
# Author:
#       eu-dk3-t

def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        result = (0, None)
        return result
    else:
        final = (length, sentence[0:1])
        return final
