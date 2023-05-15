#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == '':
        char = None
    else:
        char = sentence[0]
    length = len(sentence)
    my_tuple = (length, char)
    return my_tuple
