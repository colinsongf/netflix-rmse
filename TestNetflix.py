#!/usr/bin/env python3

from Netflix import *
from unittest import main, TestCase
from io import StringIO
import math

class TestNetflix (TestCase):
    def test_read1 (self):
        r = StringIO("123:\n1\n2\n3")
        
        line = netflix_read(r)
        self.assertEqual(line, "123:")
    
    def test_read2 (self):
        r = StringIO("123456:\n789\n12345\n4242")

        line = netflix_read(r)
        self.assertEqual(line, "123456:")

        line = netflix_read(r)
        self.assertEqual(line, "789")

        line = netflix_read(r)
        self.assertEqual(line, "12345")

        line = netflix_read(r)
        self.assertEqual(line, "4242")

    def test_read3 (self):
        r = StringIO("")
        line = netflix_read(r)
        self.assertEqual(line, "")

    def test_write1(self):
        io = StringIO()
        netflix_write(str(12345), w)
        self.assertEqual(w.getvalue(), "12345\n")

    def test_write2(self):
        io = StringIO()
        netflix_write("12345:\n" + str(6789))
        self.assertEqual(w.getvalue(), "12345:\n6789\n")

    def test_write3(self):
        io = StringIO()
        netflix_write("", w)
        self.assertEqual(w.getvalue(), "\n")

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

main()
