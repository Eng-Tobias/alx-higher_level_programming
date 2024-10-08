#!/usr/bin/python3
import unittest
from 4-text_indentation import text_indentation
from io import StringIO
import sys

class TestTextIndentation(unittest.TestCase):
    def test_text_indentation(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        text_indentation("Hello. My name is John? Yes!")
        sys.stdout = sys.__stdout__
        expected_output = "Hello.\n\n My name is John?\n\n Yes!\n\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_text_indentation_errors(self):
        with self.assertRaises(TypeError):
            text_indentation(12345)

if __name__ == '__main__':
    unittest.main()
