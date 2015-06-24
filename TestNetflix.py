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

main()
