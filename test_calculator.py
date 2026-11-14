import unittest
import math

from calculator import (
    add,
    subtract,
    multiply,
    divide,
    logarithm,
    hypotenuse,
    square_root
)


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)

    def test_sqrt(self):
        self.assertEqual(square_root(25), 5)


if __name__ == "__main__":
    unittest.main()


if __name__ == "__main__":
    unittest.main()
