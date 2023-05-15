#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    if not my_list:
        return []
    result = []
    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
