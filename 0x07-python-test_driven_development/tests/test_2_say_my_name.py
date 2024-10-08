#!/usr/bin/python3
import unittest
from 2-say_my_name import say_my_name

class TestSayMyName(unittest.TestCase):
    def test_say_my_name(self):
        self.assertEqual(say_my_name("John", "Doe"), "My name is John Doe")

    def test_say_my_name_errors(self):
        with self.assertRaises(TypeError):
            say_my_name(123, "Doe")
        with self.assertRaises(TypeError):
            say_my_name("John", 456)

if __name__ == '__main__':
    unittest.main()
