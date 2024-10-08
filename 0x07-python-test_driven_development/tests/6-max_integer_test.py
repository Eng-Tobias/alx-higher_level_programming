#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([]), None)

if __name__ == "__main__":
    unittest.main()
