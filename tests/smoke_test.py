import pytest
from quizmake import quizmake

def test_return_string():
    assert quizmake.return_string() == 'string'
    print('we good')
