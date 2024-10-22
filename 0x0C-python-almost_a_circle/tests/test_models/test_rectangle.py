# tests/test_models/test_rectangle.py

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_initialization(self):
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)


    def test_id(self):
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(10, 5, id=15)
        self.assertEqual(r2.id, 15)

# Ensure you have only one blank line at the end of the file
