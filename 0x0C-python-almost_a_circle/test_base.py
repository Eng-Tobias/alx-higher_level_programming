# tests/test_models/test_base.py
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

if __name__ == "__main__":
    unittest.main()
