#!/usr/bin/env python3

from math import sqrt
from numpy import mean, sqrt, square, subtract
import json
from pprint import pprint

movie = ""

# Paths to average rating cachess
cache_viewer_avg = "http://www.cs.utexas.edu/~ebanner/netflix-tests/ezo55-Average_Viewer_Rating_Cache.json"
cache_movie_avg = "http://www.cs.utexas.edu/~ebanner/netflix-tests/BRG564-Average_Movie_Rating_Cache.json"

def avg_rating_movie():
    """
    """
    data = json.loads(open(cache_movie_avg).read())
    movie_rating = data[movie]

def avg_rating_user(viewer_id):
    """
    """
    data = json.loads(open(cache_viewer_avg).read())
    return data[viewer_id]
    
def netflix_read(r):
    """
    Read a line from input file
    """
    if (":" in r):
        global movie
        movie = r.split(":")[0]
        avg_rating_movie()
        return ""
    return r.strip()

def netflix_print(s, w):
    """
    Write a line to output
    """
    w.write(str(s)+"\n")

def netflix_rate(s):
    """
    """
	return 0

def netflix_solve(r, w):
    """
    """
    for line in r:
        s = netflix_read(line)

        if (s != ""):
            rating = netflix_rate(s)
            netflix_print(str(rating), w)
        else:
            netflix_print(str(movie) + ":", w)
        
         
def rmse(a, p):
    """
    O(1) in space
    O(n) in time
    """
    return sqrt(mean(square(subtract(a, p)))

    #z = zip(a, p)
    #v = sum([(x - y) ** 2 for x, y in z])
    #return sqrt(v / len(a))
