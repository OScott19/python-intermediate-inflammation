"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)



## add test for daily max and daily min


from inflammation.models import daily_min

def test_daily_min_integers():
    """Test that the daily_min function works for an array of positive and negative integers."""

    test_input = np.array([[ 5, 100, 4],
                           [-6, 44,  1],
                           [ 0,  0,  55]])
    test_result = np.array([-6,  0,  1])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test_input), test_result)


from inflammation.models import daily_max

def test_daily_max_integers():
    """Test that daily_max function works for an array of positive and negative integers."""

    test_input = np.array([[5, -100, -4, 1],
                           [-6, -44,  -1, 2],
                           [0, 0,    -55, 3]])
    test_result = np.array([5, 0, -1, 3])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)

### test for NaNs?

def test_daily_min_string():
    """Test for TypeError when passing strings"""

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])



# other potential tests  - check for NaNs, NAs, mixture of strings & integers, floats
# need to test things that are not valid (and that they throw errors), not just things that should work 
# best practice: keep tests small & focused 


#### now trying perameterized tests

# the "@" bit is a 'decorator', and it 'decorates' the functions
# it wraps around the function
@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0,0], [0,0], [0,0]], [0,0]), # 3*2 array of inputs, and 1*2 array of expected outputs
        ([ [1,2], [3,4], [5,6]], [3,4]),
    ]
)
def test_daily_mean(test,expected):
    """Test mean function works for array of zeroes and positive integers"""
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))

