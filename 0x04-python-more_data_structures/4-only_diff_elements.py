#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

    present_in_one = set_1 ^ set_2
    return present_in_one
