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
from ..source.service import get_users
import unittest.mock  as mock

# import sys
# sys.path.append("..")


# We are using patch function from mock, to replace the request.get
# we want to mock the request.get function
# (we don't want to test the API itself)
@mock.patch("requests.get")  #path to our function
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": 1,
        "name": "Joe Doe"
    }
    mock_get.return_value  = mock_response
    data = get_users()

    assert data == { "id": 1, "name": "Joe Doe"}








