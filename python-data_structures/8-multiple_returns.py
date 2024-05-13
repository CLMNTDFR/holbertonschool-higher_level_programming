#!/usr/bin/python3

def multiple_returns(sentence):
    #  if sentence is not empty:
    if sentence:
        length = len(sentence)
        first = sentence[0]

    #  if sentence is empty
    else:
        lenght = 0
        first = None

    return (length, first)
