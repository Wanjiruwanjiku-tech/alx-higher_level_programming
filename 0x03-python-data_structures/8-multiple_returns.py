#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == '\0':
        return None
    length = len(sentence)
    char = sentence[0]
    my_tuple = (length, char)
    return my_tuple
