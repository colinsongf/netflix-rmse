#!/usr/bin/env python3

from numpy import mean, sqrt, square, subtract
import json

movie = ""

# Types of Netflix data
VIEWER = 0
MOVIE = 1
SOLUTIONS = 2

# Paths to average rating cachess
cache_viewer_avg = "http://www.cs.utexas.edu/~ebanner/netflix-tests/ezo55-Average_Viewer_Rating_Cache.json"
cache_movie_avg = "http://www.cs.utexas.edu/~ebanner/netflix-tests/BRG564-Average_Movie_Rating_Cache.json"
probe_solutions = "http://www.cs.utexas.edu/~ebanner/netflix-tests/pam2599-probe_solutions.json"

# ----------------
# get_netflix_data
# ----------------

def get_netflix_data(datatype):
    """
    Get json data depending on datatype
    VIEWER, MOVIE, SOLUTIONS
    """
    cache = ""
    if (datatype == MOVIE):
	    cache = cache_movie_avg
    elif (datatype == VIEWER):
        cache = cache_viewer_avg
    else:
        cache = probe_solutions
    
    f = open(cache, "r")
    data = json.loads(f.read())
    return data

# ------------
# netflix_read
# ------------
 
def netflix_read(movie_data, r):
    """
    Read a line from input
    Extract movie details as a tuple: (movie, avg rating, period)
    """ 
    if (":" in r):
        movie = r.split(":")[0]
        assert(movie > 0 and movie <= 17770)
        assert(str(movie) in movie_data)
        movie_info = (movie, movie_data[str(movie)]["average"], movie_data[str(movie)]["period"])
        return ("", movie_info)

    return (r.strip(), "")

# -------------
# netflix_print
# -------------

def netflix_print(s, w):
    """
    Write a line to output
    """
    w.write(str(s)+"\n")

# ------------
# netflix_rate
# ------------

def netflix_rate():
    """
    """
    return 1

# -------------
# netflix_solve
# -------------

def netflix_solve(r, w):
    """
    """
    netflix_data = [get_netflix_data(VIEWER), get_netflix_data(MOVIE), get_netflix_data(SOLUTIONS)]
    rating_actual = []
    rating_est = []
    movie_info = ()

    for line in r:
        s = netflix_read(netflix_data[MOVIE], line)

        if (s[0] != ""):
            est_rating = netflix_rate(netflix_data[VIEWER], s[0], movie_info)    # Get rating for movie
            actual_rating = netflix_data[SOLUTIONS][str(s[0])][str(movie_info[0])]            
            
            rating_est.append(est_rating)
            rating_actual.append(actual_rating)
            
            netflix_print(str(round(rating, 1)), w)
            
        else:
            movie_info = s[1]
            netflix_print(str(movie_info[0]) + ":", w)
      
        # Get rmse result and truncate
        temp = rmse(rating_est, rating_actual)
        parts = str(temp).split(".")
        after_decimal = parts[1]
        after_decimal = after_decimal[0 : 2]
        result = parts[0] + "." + after_decimal

        netflix_print("rmse: " + result) 
# ----
# rmse 
# ----
         
def rmse(a, p):
    """
    O(1) in space
    O(n) in time
    """
    return sqrt(mean(square(subtract(a, p)))

