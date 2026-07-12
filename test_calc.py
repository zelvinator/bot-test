#!/usr/bin/env python3
"""Tests for the calculator module."""

import pytest
from calc import add, subtract, multiply, divide


class TestAdd:
    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-1, -2) == -3

    def test_add_zero(self):
        assert add(5, 0) == 5


class TestSubtract:
    def test_subtract_positive(self):
        assert subtract(5, 3) == 2

    def test_subtract_negative_result(self):
        assert subtract(3, 5) == -2

    def test_subtract_zero(self):
        assert subtract(10, 0) == 10


class TestMultiply:
    def test_multiply_positive(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0

    def test_multiply_negative(self):
        assert multiply(-2, 3) == -6


class TestDivide:
    def test_divide_exact(self):
        assert divide(10, 2) == 5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_divide_fraction(self):
        assert divide(7, 2) == 3.5



