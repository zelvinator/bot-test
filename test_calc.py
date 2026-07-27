"""Tests for calculator functions."""

import unittest
from calc import add, subtract, multiply, divide, power


class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)


class TestSubtract(unittest.TestCase):
    def test_subtract_positive(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative(self):
        self.assertEqual(subtract(-1, -1), 0)

    def test_subtract_zero(self):
        self.assertEqual(subtract(0, 0), 0)


class TestMultiply(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-2, 3), -6)

    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 5), 0)

    def test_multiply_by_one(self):
        self.assertEqual(multiply(5, 1), 5)


class TestDivide(unittest.TestCase):
    def test_divide_exact(self):
        self.assertEqual(divide(6, 3), 2.0)

    def test_divide_with_remainder(self):
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_by_zero_raises_valueerror(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_divide_negative(self):
        self.assertEqual(divide(-6, 3), -2.0)


class TestPower(unittest.TestCase):
    def test_power_positive_exponent(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)

    def test_power_one_exponent(self):
        self.assertEqual(power(3, 1), 3)


if __name__ == "__main__":
    unittest.main()