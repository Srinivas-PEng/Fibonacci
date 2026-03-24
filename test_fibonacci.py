import pytest
from fibonacci import Fibonacci


def test_invalid_type():
    with pytest.raises(ValueError):
        Fibonacci("10")


def test_negative_value():
    assert list(Fibonacci(-5)) == []


def test_zero():
    assert list(Fibonacci(0)) == [0]


def test_one():
    assert list(Fibonacci(1)) == [0, 1]


def test_two():
    assert list(Fibonacci(2)) == [0, 1, 1]


def test_four():
    assert list(Fibonacci(4)) == [0, 1, 1, 2, 3]


def test_ten():
    assert list(Fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]