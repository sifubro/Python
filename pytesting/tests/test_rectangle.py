import math
import pytest
from ..source.my_classes import Rectangle


# instead of initializing Rectangle(10,20) two times we can use fixtures
@pytest.fixture
def my_rectangle():
    return Rectangle(10,20)


# def test_area():
#     rectangle = Rectangle(10,20)
#     assert rectangle.area() == 10*20


# def test_perimeter():
#     rectangle = Rectangle(10,20)
#     assert rectangle.perimeter() == (2*10) + (2*20)



def test_area(my_rectangle):
    assert my_rectangle.area() == 10*20


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (2*10) + (2*20)
