#!/usr/bin/python3

def max_integer(my_list=[]):

    if not my_list:
        return None
    max_int = my_list[0]
    for nums in my_list:
        if nums > max_int:
            max_int = nums
    return max_int
