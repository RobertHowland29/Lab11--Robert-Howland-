import unittest
import math

from calculator import (
    add,
    subtract,
    multiply,
    divide,
    logarithm,
    exponent,
    sub,
    mul,
    div,
    log,
    exp,
    hypotenuse,
    square_root
)


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 5), 3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(5, 20), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 27), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)

        with self.assertRaises(ValueError):
            logarithm(-2, 10)

        with self.assertRaises(ValueError):
            logarithm(0, 10)

    def test_exponent(self):
        self.assertEqual(exponent(2, 3), 8)
        self.assertEqual(exponent(3, 2), 9)
        self.assertEqual(exponent(5, 0), 1)

    def test_sub(self):
        self.assertEqual(sub(5, 3), 2)

    def test_mul(self):
        self.assertEqual(mul(2, 3), 6)

    def test_div(self):
        self.assertEqual(div(2, 10), 5)

    def test_log(self):
        self.assertAlmostEqual(log(2, 8), 3)

    def test_exp(self):
        self.assertEqual(exp(2, 3), 8)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)

    def test_square_root(self):
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(0), 0)

    def test_square_root_invalid(self):
        with self.assertRaises(ValueError):
            square_root(-9)


if __name__ == "__main__":
    unittest.main()
