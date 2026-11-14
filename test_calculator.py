import pytest
import math

from calculator import add, sub, mul, div, log, exp


def test_add():
    assert add(2, 3) == 5
    assert add(-2, 5) == 3
    assert add(0, 0) == 0


def test_subtract():
    assert sub(5, 3) == 2
    assert sub(3, 5) == -2
    assert sub(0, 0) == 0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(0, 5)


def test_logarithm():
    assert math.isclose(log(2, 8), 3)
    assert math.isclose(log(10, 100), 2)
    assert math.isclose(log(3, 27), 3)


def test_log_invalid_base():
    with pytest.raises(ValueError):
        log(1, 10)

    with pytest.raises(ValueError):
        log(-2, 10)

    with pytest.raises(ValueError):
        log(0, 10)
