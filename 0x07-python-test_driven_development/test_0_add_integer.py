#!/usr/bin/python3
import unittest
from 0-add_integer import add_integer

class TestAddInteger(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(add_integer(1, 2), 3)
        self.assertEqual(add_integer(100, -2), 98)
        self.assertEqual(add_integer(0, 0), 0)

    def test_add_integer_errors(self):
        with self.assertRaises(TypeError):
            add_integer(10, "20")
        with self.assertRaises(TypeError):
            add_integer("hello", 1)

if __name__ == '__main__':
    unittest.main()
