# https://www.youtube.com/watch?v=cHYq1MRoyI0&ab_channel=freeCodeCamp.org
import math
from ..source.my_classes import Circle

'''
run as 
> python -s  test_classes.py
'''

class TestCircle():

    # runs setup code before each test method
    # for all test methods the setup_method will run at the beginning of each test
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = Circle(10)


    # teardown run code after each test method
    def teardown_method(self, method):
        print(f"Teardown method {method}")
        del self.circle


    def test_area(self):
        assert self.circle.area() == math.pi *  self.circle.radius ** 2


    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected


    def test_one(self):
        assert True


    def test_two(self):
        assert True


class TestRectangle():
    pass




