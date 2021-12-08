import pytest
from math_series import __version__
from math_series.math_series import fibonacci

def test_version():
    assert __version__ == '0.1.0'

def test_zero_fibonacci():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_one_fibonacci():
    actual = fibonacci(1)
    expected = 0
    assert actual == expected
    
def test_two_fibonacci():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected
    
def test_three_fibonacci():
    actual = fibonacci(3)
    expected = 3
    assert actual == expected
    
def test_five_fibonacci():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected
