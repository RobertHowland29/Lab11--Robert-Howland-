import pytest
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


# Addition tests
def test_add():
    assert add(2, 3) == 5
    assert add(-2, 5) == 3
    assert add(0, 0) == 0


# Subtraction tests
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0


# Multiplication tests
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 5) == -10
    assert multiply(0, 5) == 0


# Division tests
def test_divide():
    assert divide(2, 10) == 5
    assert divide(5, 20) == 4


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(0, 5)


# Logarithm tests
def test_logarithm():
    assert math.isclose(logarithm(2, 8), 3)
    assert math.isclose(logarithm(10, 100), 2)
    assert math.isclose(logarithm(3, 27), 3)


def test_log_invalid_base():
    with pytest.raises(ValueError):
        logarithm(1, 10)

    with pytest.raises(ValueError):
        logarithm(-2, 10)

    with pytest.raises(ValueError):
        logarithm(0, 10)


# Exponent tests
def test_exponent():
    assert exponent(2, 3) == 8
    assert exponent(3, 2) == 9
    assert exponent(5, 0) == 1


# Shortened function name tests
def test_sub():
    assert sub(5, 3) == 2


def test_mul():
    assert mul(2, 3) == 6


def test_div():
    assert div(2, 10) == 5


def test_log():
    assert math.isclose(log(2, 8), 3)


def test_exp():
    assert exp(2, 3) == 8


# Hypotenuse tests
def test_hypotenuse():
    assert math.isclose(hypotenuse(3, 4), 5)
    assert math.isclose(hypotenuse(5, 12), 13)


# Square root tests
def test_square_root():
    assert square_root(25) == 5
    assert square_root(16) == 4
    assert square_root(0) == 0


def test_square_root_invalid():
    with pytest.raises(ValueError):
        square_root(-9)
