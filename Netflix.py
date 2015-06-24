#!/usr/bin/env python3

def netflix_read(r):
    """
    Read a line from input file
    """
    return r.readline()

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
    """
    """
    return 1
