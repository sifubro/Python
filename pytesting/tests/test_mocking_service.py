'''
Mocking is used to isolate the system that we are testing and replace the 
external dependencies with controlled implementations called mocks.

e.g. Imagine you write code that fetches data from an external API using the
requests library and you don't want to call the API itself because it might be
slow, it might cost money or affect rate limits (we don't want to depend on 
the API itself) Also the API might fail and you only want to test your code.

Or for testing a database (getting a user from the DB) and you don't want to 
depend on the DB itself because the connection might fail
'''

import pytest 
from ..source.service import get_user_from_db
import unittest.mock  as mock

import sys
sys.path.append("..")

# We are using patch function from mock, to replace get_user_from_db
@mock.patch("source.service.get_user_from_db")  #path to our function
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = get_user_from_db(1)

    assert user_name == "Mocked Alice"

















