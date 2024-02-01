
'''
Add metadata to your tests. Think of it as tagging your test with labels that
influence how the test runs or is ported. 

purpose
e.g. label or tag your tests as "slow", or as to "skip", conditionally execure your tests
'''


import pytest 
import time
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

# adding metadata
@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = add(1,5)
    assert result == 6

# to run the slow tests do 
# >pytest -m slow


# adding metadata to skip  (flagged as s)
@pytest.mark.skip(reason="Currently Broken")
def test_add_skipped():
    assert add(1,5) == 6



# adding metadata that xfail  (flagged as x)
@pytest.mark.xfail(reason="Cannot divide by 0")
def test_divide_xfailed():
    divide(3,0)