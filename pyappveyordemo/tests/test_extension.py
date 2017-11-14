from pyappveyordemo.extension import some_function
from nose.tools import assert_equal
import xmltodict

def test_some_function():
    assert_equal(some_function(0, 0), 2)
    assert_equal(some_function(0, 42), 0)
    assert_equal(some_function(41, 2), 1)
    assert_equal(some_function(1, 2), 1)
