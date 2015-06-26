#!/usr/bin/env python3

from Netflix import *
from unittest import main, TestCase
from io import StringIO
import json
import math

class TestNetflix (TestCase):

    # ----
    # read
    # ----

    def test_read1 (self):
        movie_data = json.loads('{"123": 456}')
        decade_data = json.loads('{"123": 2000}')
        r = "123:\n1\n2\n3"
        
        info = netflix_read(movie_data, decade_data, r)
        movie_info = info[1]
        assert(len(movie_info) == 3)
        self.assertEqual(movie_info[0], "123")
        self.assertEqual(movie_info[1], 456)
        self.assertEqual(movie_info[2], 2000)
    
    def test_read2 (self):
        movie_data = json.loads('{"123456": 789}')
        decade_data = json.loads('{"123456": 1900}')
        r = "123456:\n789\n12345\n4242"

        info = netflix_read(movie_data, decade_data, r)
        movie_info = info[1]
        assert(len(movie_info) == 3)
        self.assertEqual(movie_info[0], "123456")
        self.assertEqual(movie_info[1], 789)
        self.assertEqual(movie_info[2], 1900)         

    def test_read3 (self):
        movie_data = json.loads('{"1": 2}')
        decade_data = json.loads('{"1": 1920}')
        r = "1:\n2\n3"

        info = netflix_read(movie_data, decade_data, r)
        movie_info = info[1]
        assert(len(movie_info) == 3)
        self.assertEqual(movie_info[0], "1")
        self.assertEqual(movie_info[1], 2)
        self.assertEqual(movie_info[2], 1920)

    # -----
    # write
    # -----

    def test_write1(self):
        w = StringIO()
        netflix_print(str(12345), w)
        self.assertEqual(w.getvalue(), "12345\n")

    def test_write2(self):
        w = StringIO()
        netflix_print("12345:\n" + str(6789), w)
        self.assertEqual(w.getvalue(), "12345:\n6789\n")

    def test_write3(self):
        w = StringIO()
        netflix_print("", w)
        self.assertEqual(w.getvalue(), "\n")


    # ----
    # rmse
    # ----

    def test_rmse1 (self):
        a = [1, 2, 3, 4, 5]
        b = [0, 0, 0, 0, 0]
        res = rmse(a, b)
        self.assertEqual(res, math.sqrt(55/5))

    def test_rmse2 (self):
        a = [1, 2, 3, 4, 5]
        b = [1, 2, 3, 4, 5]
        res = rmse(a, b)
        self.assertEqual(res, 0)

    def test_rmse3 (self):
        a = [1, 2, 3]
        b = [-1, -2, -3]
        res = rmse(a, b)
        self.assertEqual(res, math.sqrt(56/3))

    # ----
    # rate
    # ----

    def test_rate1 (self):
        viewer_data = json.loads('{"1952305": 3.409340659340659}')
        user_id = "1952305"
        movie_info = (10, 3.180722891566265, "2000")

        result = netflix_rate(viewer_data, user_id, movie_info)
        self.assertEqual(result, 3.295031775453462)

    def test_rate2 (self):
        viewer_data = json.loads('{"975179": 3.6097560975609757}')
        user_id = "975179"
        movie_info = (10015, 3.816008316008316, "1990")

        result = netflix_rate(viewer_data, user_id, movie_info)
        self.assertEqual(result, 3.712882206784646)

    def test_rate3 (self):
        viewer_data = json.loads('{"2503691": 3.9280155642023344}')
        user_id = "2503691"
        movie_info = (10013, 3.279754843811783, "1980")

        result = netflix_rate(viewer_data, user_id, movie_info)
        self.assertEqual(result, 3.784079464207412)

    # --------
    # get_data
    # --------
    
    def test_get_data1 (self):
        # Test movie data
        datatype = 1
        data = get_netflix_data(datatype)
        
        # Expected format: {"13": 4.552}
        movie_id = "13"
        assert(movie_id in data)
        self.assertEqual(data[movie_id], 4.552)
        

    def test_get_data2 (self):
        # Test viewer data
        datatype = 0
        data = get_netflix_data(datatype)

        # Expected format: {"393892": 3.88}
        user_id = "393892"
        assert(user_id in data)
        self.assertEqual(data[user_id], 3.88)

    def test_get_data3 (self):
        # Test probe solutions
        datatype = 3
        data = get_netflix_data(datatype)
        
        # Expected format: {"4446": {"1657689": 3}}
        movie_id = "4446"
        user_id = "1657689"

        assert(movie_id in data)
        movie_data = data[movie_id]

        assert(user_id in movie_data)
        assert(type(movie_data[user_id]) is int)
        self.assertEqual(movie_data[user_id], 3)
  
    # -----
    # solve
    # -----

    def test_solve1 (self):
        r = StringIO("10015:\n975179\n829739\n1732761\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "10015:\n3.7\n3.4\n3.2\nrmse: 0.53\n")

    def test_solve2 (self):
        r = StringIO("10013:\n2503691\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "10013:\n3.8\nrmse: 0.78\n")

    def test_solve3 (self):
        r = StringIO("10017:\n2280428\n1129341\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "10017:\n3.5\n3.8\nrmse: 1.35\n")

main()
