import pytest 
from ..source.my_classes import Square

'''
Support you want to test a light bulb with different branch of batteries to ensure
it works with all of them. So instead of writting each separate test with each
battery, would be more efficient to write 1 test and run it for each battery 
brand. Could do it with for loop but gets messy. Instead use parametrize:

e.g. Suppose we want to calculate area of square and give it different values:
'''

# Notice the comma separated string!
@pytest.mark.parametrize("side_length, expected_area", [(5,25), (4, 16), (9,81)])
def test_multiple_square_areas(side_length, expected_area):
    assert Square(side_length).area() == expected_area

















