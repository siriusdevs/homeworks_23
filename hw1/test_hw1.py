"""Tests for hw1."""
import pytest

from hw1 import salary_statistics

company = {
    'first': {
        'worker4': 124.4,
        'worker2': 244,
    },
    'second': {
        'worker1': 125.2422,
        'worker2': 44,
        'worker3': 1234,
    },
    'third': {
        'worker1': 100,
    },
    'forth': {
        'worker1': 232,
        'worker2': 150.245,
    },
}


@pytest.mark.parametrize('company, min_salary, excected_value', (
    (company, None, {
        'top': [1234, 244, 232],
        'ratio': 75.87,
    }),
    (company, 150, {
        'top': [1234, 244, 232],
        'ratio': 91.92,
    }),
))
def test(company, min_salary, excected_value):
    """Provide tests.

    Args:
        company (_type_):  name
        min_salary (_type_): minimal salary
        excected_value (_type_): value
    """
    assert salary_statistics(company, min_salary) == excected_value
