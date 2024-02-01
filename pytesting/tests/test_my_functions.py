import pytest 
from ..source.my_functions import add, divide, divide_custom_raise


def test_add():
    result = add(1,5)
    assert result == 6


def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(3,0)


def test_divide_custom():
    with pytest.raises(ValueError):
        divide_custom_raise(3,0)

