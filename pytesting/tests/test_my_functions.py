import pytest 
from ..source.my_functions import add


def test_add():
    result = add(1,5)
    assert result == 6
