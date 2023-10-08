"""Those are tests for hw1."""
import pytest

from hw1 import get_salary_stats

NAN = None


test_data = {
    'it': {
        'Bob': 1450.5,
        'Jeremy': 999.9,
        'Elijah': 1000,
        'Charlie': 150.45,
    },
    'marketing': {
        'Rimus': 1500,
        'Thomas': 1250.5,
        'Richard': 79893.12312,
        'Charlie': 150.45,
    },
    'managment': {
        'Elon': 99999999999.99999999,
        'Tim': 100,
    },
}


test_data_value = (
    (((100000000000.0, 79893.12, 1500), 100.0)),
)


data_limit_test = (
    (1000, ((1000, 999.9, 150.45), 89.57)),
    (NAN, ((100000000000.0, 79893.12, 1500), 100.0)),
    (5000, ((1500, 1450.5, 1250.5), 63.63)),
)

test_data_zero = (
    ((0, 0, 0), 100.0),
)


@pytest.mark.parametrize('expected', test_data_value)
def test_salary_stat(expected: tuple):
    """Test function.

    Args:
        expected: tuple that is expected.

    """
    assert get_salary_stats(test_data) == expected


@pytest.mark.parametrize('limit, expected', data_limit_test)
def test_salary_stat_limit(limit: int, expected: tuple):
    """Test function.

    Args:
        limit: int, limit of salary that we are not exceeding
        expected: tuple that is expected.

    """
    assert get_salary_stats(test_data, limit) == expected


@pytest.mark.parametrize('expected', test_data_zero)
def test_for_zeros(expected: tuple):
    """This is block that awaits zero in return for no salary in company.

    Args:
        expected: tuple with zeros that is supposed to be recieved due to 0 summ of salaries.

    """
    assert get_salary_stats({'it': {'Rimus': 0, 'John': 0, 'Casey': 0}}) == expected
