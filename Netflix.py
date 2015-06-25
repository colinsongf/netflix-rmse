#!/usr/bin/env python3

from numpy import mean, sqrt, square, subtract
import json

movie = ""

# Types of Netflix data
VIEWER = 0
MOVIE = 1
DECADE = 2
SOLUTIONS = 3

# Paths to average rating cachess
cache_viewer_avg = "/u/ebanner/netflix-tests/ezo55-Average_Viewer_Rating_Cache.json"
cache_movie_avg = "/u/ebanner/netflix-tests/BRG564-Average_Movie_Rating_Cache.json"
cache_movie_decades = "/u/ebanner/netflix-tests/pra359-Movie_Decades_Cache.json"
cache_customer_decade = "/u/ebanner/netflix-tests/drc2582-customer_decade_dict.json"
probe_solutions = "/u/ebanner/netflix-tests/pam2599-probe_solutions.json"

# ----------------
# get_netflix_data
# ----------------

def get_netflix_data(datatype):
    """
    Get json data depending on datatype
    VIEWER, MOVIE, DECADE, SOLUTIONS
    """
    cache = ""
    if (datatype == MOVIE):
	    cache = cache_movie_avg
    elif (datatype == VIEWER):
        cache = cache_viewer_avg
    elif (datatype == DECADE):
        cache = cache_movie_decades
    else:
        cache = probe_solutions
    
    f = open(cache, "r")
    data = json.loads(f.read())
    return data

# ------------
# netflix_read
# ------------
 
def netflix_read(movie_data, decade_data, r):
    """
    Read a line from input
    Extract movie details as a tuple: (movie, avg rating, period)
    """ 
    if (":" in r):
        movie = r.split(":")[0]
        assert(str(movie) in movie_data)
        assert(str(movie) in decade_data)

        movie_avg = movie_data[str(movie)]
        movie_period = decade_data[str(movie)]
        movie_info = (movie, movie_avg, movie_period)
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

def netflix_rate(viewer_data, movie, movie_info):
    """
    Calculate estimated rating for a viewer
    Input movie_info: (movie_id, average rating, period)
    """
    viewer_rating_avg = viewer_data[movie]
    movie_rating_avg = movie_info[1]
    period = movie_info[2]

    # Start with a rating that is the average of
    # all user ratings and the movie's average rating
    rating = (viewer_rating_avg + movie_rating_avg) / 2
   
    # Create a multiplier to modify rating with 
    multiplier = 0

    movie_rating_avg = int(movie_rating_avg)

    # Experiment with correlation between rating and decade
    if (period == 2000 and movie_rating_avg > 3.0):
        multiplier = 0.07
    elif (period == 1990 and movie_rating_avg > 3.0):
        multiplier = 0.05
    elif (period == 1980 and movie_rating_avg > 3.0):
        multiplier = .02
    elif (period == 1970 and movie_rating_avg > 3.0):
        multiplier = .02
    elif (period == 1960 and movie_rating_avg > 3.0):
        multiplier = .02
    elif (period == 1950 and movie_rating_avg > 3.0):
        multiplier = .03
    elif (period == 1940 and movie_rating_avg > 3.0):
        multiplier = 0.03
    elif (period == 1930 and movie_rating_avg > 3.0):
        multiplier = 0.06
    # People love that old stuff
    elif (period == 1920 and movie_rating_avg > 3.0):
        multiplier = 0.15
    
    if (viewer_rating_avg > 4):
        multiplier += 1.09
    elif (viewer_rating_avg > 3.70):
        multiplier += 1.05
    elif (viewer_rating_avg > 3.10):
        multiplier += 1.0
    else:
        multiplier += 0.98
   
    return (rating * multiplier)

# -------------
# netflix_solve
# -------------

def netflix_solve(r, w):
    """
    """
    netflix_data = [get_netflix_data(VIEWER), get_netflix_data(MOVIE), get_netflix_data(DECADE), get_netflix_data(SOLUTIONS)]
    rating_actual = []
    rating_est = []
    movie_info = ()

    for line in r:
        s = netflix_read(netflix_data[MOVIE], netflix_data[DECADE], line)

        if (s[0] != ""):
            # If viewer, get rating prediction and actual rating and add to lists
            est_rating = netflix_rate(netflix_data[VIEWER], s[0], movie_info)
            actual_rating = netflix_data[SOLUTIONS][movie_info[0]][s[0]]
            
            rating_est.append(est_rating)
            rating_actual.append(actual_rating)

            netflix_print(str(round(est_rating, 1)), w)
            
        else:
            # If movie, get movie information
            movie_info = s[1]
            netflix_print(str(movie_info[0]) + ":", w)
      
    # Get rmse result and truncate
    temp = rmse(rating_est, rating_actual)
    parts = str(temp).split(".")
    after_decimal = parts[1]
    after_decimal = after_decimal[0 : 2]
    result = parts[0] + "." + after_decimal

    netflix_print("rmse: " + result, w)

# ----
# rmse 
# ----
         
def rmse(a, p):
    """
    O(1) in space
    O(n) in time
    """
    return(sqrt(mean(square(subtract(a, p)))))
