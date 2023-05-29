#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    try:
        count = 0 #counter to keep track
        for i in range(x):
            print(my_list[i], end=" ")
            count += 1

    except IndexError:
        pass #ignore any index errors

    finally:
        print()
        return count
