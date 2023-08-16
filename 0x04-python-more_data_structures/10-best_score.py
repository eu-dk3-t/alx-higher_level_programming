#!/usr/bin/python3
# File name:
#       10-best_score.py
# Description:
#       Gets the highest value in
#       a dict
# Author:
#       eu-dk3-t


def best_score(a_dictionary):
    current_high = 0
    true_high = None
    if type(a_dictionary) is dict:
        for (key, value) in a_dictionary.items():
            if value > current_high:
                current_high = value
                true_high = key
    return true_high
