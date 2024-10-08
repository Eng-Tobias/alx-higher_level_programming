#!/usr/bin/python3
import unittest
from 1-matrix_divided import matrix_divided

class TestMatrixDivided(unittest.TestCase):
    def test_matrix_division(self):
        matrix = [[2, 4], [6, 8]]
        result = [[1, 2], [3, 4]]
        self.assertEqual(matrix_divided(matrix, 2), result)

    def test_matrix_division_errors(self):
        with self.assertRaises(TypeError):
            matrix_divided("Not a matrix", 2)
        with self.assertRaises(TypeError):
            matrix_divided([[1, 2], [3, "4"]], 2)
        with self.assertRaises(ZeroDivisionError):
            matrix_divided([[1, 2], [3, 4]], 0)

if __name__ == '__main__':
    unittest.main()
