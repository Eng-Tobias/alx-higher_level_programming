#!/usr/bin/python3
import unittest
from 3-print_square import print_square
from io import StringIO
import sys

class TestPrintSquare(unittest.TestCase):
    def test_print_square(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        print_square(2)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "##\n##\n")

    def test_print_square_errors(self):
        with self.assertRaises(TypeError):
            print_square("4")
        with self.assertRaises(ValueError):
            print_square(-1)

if __name__ == '__main__':
    unittest.main()
