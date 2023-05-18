#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_set = set(my_list)
    sum_elements = 0

    for element in my_set:
        sum_elements += element
    return sum_elements
