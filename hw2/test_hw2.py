"""Test for hw2."""


import pytest

from hw2 import process_data, get_median_age

data_ages = (
    ([12, 15, 18], 15),
    ((12, 15, 18, 20), 16),
    ((11, 15, 18, 20), 16),
    ((12, 20, 25), 20),
)

@pytest.mark.parametrize('ages, excepted', data_ages)
def test_get_median_age(ages, excepted):
    assert get_median_age(ages) == excepted
