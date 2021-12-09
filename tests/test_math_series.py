import pytest
from math_series import __version__
from math_series.math_series import fibonacci, lucas

# Fibonacci Tests
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
    actual = fibonacci(5)
    expected = 3
    assert actual == expected
    
def test_five_fibonacci():
    actual = fibonacci(10)
    expected = 34
    assert actual == expected
    
def test_five_fibonacci():
    actual = fibonacci(15)
    expected = 377
    assert actual == expected  

# =======================================================================
#       Lucas Tests

def test_zero_lucas():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_one_lucas():
    actual = lucas(1)
    expected = 1
    assert actual == expected
    
def test_two_lucas():
    actual = lucas(2)
    expected = 3
    assert actual == expected
    
def test_three_lucas():
    actual = lucas(5)
    expected = 11
    assert actual == expected
    
def test_four_lucas():
    actual = lucas(7)
    expected = 29
    assert actual == expected
    
def test_five_lucas():
    actual = lucas(8)
    expected = 47
    assert actual == expected  

# ===========================================

