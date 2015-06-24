#!/usr/bin/env python3

from math import sqrt
from numpy import mean, sqrt, square, subtract
import json
from pprint import pprint

def netflix_read(r):
    """
    Read a line from input file
    """
    return r.readline()[ : -1]    # Do not read the newline character

def netflix_print(s, w):
    """
    Write a line to output
    """
    w.write(str(s)+"\n")

def netflix_rate(r, w):
    """
    """
    while (True):
        line = netflix_read(r)

        if (line == ""):
            return
        
        if (line[-1] != ":"):
            netflix_print(netflix_predict(line), w)
        else:
            netflix_print(line, w)

def netflix_predict(c):
    return 1

def rmse(a, p):
    """
    O(1) in space
    O(n) in time
    """
    return sqrt(mean(square(subtract(a, p)))

    #z = zip(a, p)
    #v = sum([(x - y) ** 2 for x, y in z])
    #return sqrt(v / len(a))
