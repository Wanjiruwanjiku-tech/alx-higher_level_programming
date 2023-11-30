#!/usr/bin/python3
"""The Module runs a function that finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """
    The function finds the peak in a list of unsorted ints
    parameters:
        list_of_integers = The list of unsorted integers to get the peak from
    """
    # Check if the list is empty
    if not list_of_integers:
        return None
    
    # Initialize pointers for searching
    low, high = 0, len(list_of_integers) - 1

    # Perform a search until low and high values meet
    while low < high:
        #calculate the middle index average
        mid_index = (low + high) // 2
        # Compare the middle index with its right neighbour
        if list_of_integers[mid_index] > list_of_integers[mid_index + 1]:
            high = mid_index
        else:
            low = mid_index + 1
        
    return list_of_integers[low]