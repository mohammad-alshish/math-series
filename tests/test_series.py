import pytest
from math_series.series import fibonacci,Lucas ,sum_series

# fibonacci tests.
def test_fibonacci_ten():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected


def test_fibonacci_negative():
    actual = fibonacci(-1)
    expected = 'Enter a whole number >= 0'
    assert actual == expected


def test_fibonacci_strings():
    actual = fibonacci("ok")
    expected = 'Enter a number please'
    assert actual == expected
# lucas.
def test_lucas_one():
    actual = Lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_zero():
    actual = Lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_seven():
    actual = Lucas(7)
    expected = 29
    assert actual == expected

def test_lucas_negative():
    actual = Lucas(-1)
    expected = 'Enter a whole number >= 0'
    assert actual == expected

def test_lucas_strings():
    actual = Lucas("ok")
    expected = 'Enter a number please'
    assert actual == expected


# sum_series tests
def test_sum_series_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_sum_series_two():
    actual = sum_series(2)
    expected = 1
    assert actual == expected

def test_sum_series_six():
    actual = sum_series(6)
    expected = 8
    assert actual == expected

def test_sum_series_luca_zero():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected

def test_sum_series_luca_one():
    actual = sum_series(1, 2, 1)
    expected = 1
    assert actual == expected