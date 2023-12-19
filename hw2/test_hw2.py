"""Test for hw2."""


import json

import pytest
from ages_operations import get_average_age, get_median_age

import hw2

BASE_PACKAGE = 'hw2/test_data_hw2/'
BASE_INPUT = 'data_hw2_'
BASE_TEST_OUTPUT = 'test_output_'
BASE_OUTPUT = 'output_hw2_'
JSON_TYPE = '.json'

INPUT = f'{BASE_PACKAGE}{BASE_INPUT}'
TEST_OUTPUT = f'{BASE_PACKAGE}{BASE_TEST_OUTPUT}'
OUTPUT = f'{BASE_PACKAGE}{BASE_OUTPUT}'

data_median_ages = (
    ([12, 15, 18], 15),
    ((12, 15, 18, 20), 16),
    ((11, 15, 18, 20), 16),
    ((12, 20, 25), 20),
)

data_average_ages = (
    ([12, 15, 18], 15),
    ((1, 19, 60), 27),
    ((11, 15, 18, 20), 16),
    ((12, 20, 25), 19),
)

data_ratio = (
    (12, 100, 12),
    (35, 350, 10),
    (12, 960, 1.25),
    (45, 745, 6.04),
)

data_years_statistic = [
    (f'{INPUT}{num}{JSON_TYPE}', f'{OUTPUT}{num}{JSON_TYPE}') for num in range(4)
]

data_users_statistic = [
    (f'{INPUT}{num}{JSON_TYPE}',
     f'{TEST_OUTPUT}{num}{JSON_TYPE}',
     f'{OUTPUT}{num}{JSON_TYPE}',
     ) for num in range(4)
]


@pytest.mark.parametrize('ages, excepted', data_median_ages)
def test_get_median_age(ages, excepted):
    """Test getting a median age.

    Args:
        ages: the ages
        excepted: an excepted answer
    """
    assert get_median_age(ages) == excepted


@pytest.mark.parametrize('ages, excepted', data_average_ages)
def test_get_average_age(ages, excepted):
    """Test getting an average age.

    Args:
        ages: the ages
        excepted: an excepted answer
    """
    assert get_average_age(ages) == excepted


@pytest.mark.parametrize('figure, to_figure, excepted', data_ratio)
def test_ratio(figure, to_figure, excepted):
    """Testing the ratio.

    Args:
        figure: the number whose difference we will check
        to_figure: from what date will we look at the ratio
        excepted: an excepted answer
    """
    assert hw2.ratio(figure, to_figure) == excepted


def test_check_ages_type():
    """Testing check ages type."""
    with pytest.raises(TypeError):
        hw2.check_ages_type('some wrong value')


@pytest.mark.xfail(raises=ValueError)
def test_get_users_from_json_exception():
    """Checking that the function throws exceptions with incorrect files."""
    hw2.get_users_from_json('asd')
    hw2.get_users_from_json('test_data_hw2/some_text.txt')


def test_process_data_exception():
    """Checking that the function throws exceptions with incorrect files."""
    hw2.process_data('test_data_hw2/wrong_data.json', 'test_data_hw2/t.json')
    with open(f'{BASE_PACKAGE}t.json') as test_file:
        with open(f'{BASE_PACKAGE}age_is_not_found.json') as real_file:
            assert test_file.readline() == real_file.readline()


@pytest.mark.parametrize('input_path, output', data_years_statistic)
def test_get_years_statistic(input_path, output):
    """Test process data.

    Args:
        input_path: that's where we get the file from
        output: the file with the correct statistics
    """
    users = hw2.get_users_from_json(input_path)
    with open(output) as file_users:
        excepted = json.load(file_users)['statictic']
        assert hw2.get_years_statistic(users) == excepted


@pytest.mark.xfail(raises=ValueError)
def test_get_years_statistic_exception():
    """Test raises exception if data is wrong."""
    users = hw2.get_users_from_json(f'{BASE_PACKAGE}wrong_data.json')
    hw2.get_years_statistic(users)


@pytest.mark.parametrize('input_path, test_output, real_output', data_users_statistic)
def test_process_data(input_path, test_output, real_output):
    """Test processing data.

    Args:
        input_path: that's where we get the file from
        test_output: that's Where the file is saved
        real_output: The data that should be in the new file
    """
    hw2.process_data(input_path, test_output)
    test_users = hw2.get_users_from_json(test_output)
    real_users = hw2.get_users_from_json(real_output)
    assert test_users == real_users
