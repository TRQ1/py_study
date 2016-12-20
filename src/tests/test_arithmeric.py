import pytest

import arithmetic


def test_add():
    assert arithmetic.add(1, 4) == 5

def test_multiply():
    assert arithmetic.multiply(2, 2) == 4

def test_divide():
    assert arithmetic.divide(4, 3) == 

def test_subtract():
    assert arithmetic.subtract(5, 4) == 1

def test_divdie_by_zero():
    with pytest.raises(ZeroDivisionError):
        arithmetic.divide(3, 0)

def test_duble_divide():
    assert arithmetic.duble_divide(4, 3) == 1
