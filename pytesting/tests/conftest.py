import pytest 
from ..source.my_classes import Rectangle

@pytest.fixture
def my_rectangle():
    return Rectangle(10,20)


@pytest.fixture
def weird_rectangle():
    return Rectangle(5,6)
