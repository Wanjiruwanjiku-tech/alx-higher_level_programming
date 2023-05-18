#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # my_list is the initial list
    # search is the element to replace
    # replace is the new element

    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list
