"""Test for calculating salary statistics module."""
import pytest

from hw1 import salary_statistics

company = {
    'first': {
        'worker1.1': 124.4,
        'worker2.1': 244,
    },
    'second': {
        'worker1.2': 125.2422,
        'worker2.2': 44,
        'worker3.2': 1234,
    },
    'third': {
        'worker1.3': 100,
    },
    'forth': {
        'worker1.4': 232,
        'worker2.4': 150.245,
    },
}


@pytest.mark.parametrize('company, min_salary, excected_value', ((company, None,
                                                                  {
                                                                      'top': [1234, 244, 232],
                                                                      'ratio': 75.87,
                                                                  }),
                                                                 (company,
                                                                  150,
                                                                  {
                                                                      'top': [1234, 244, 232],
                                                                      'ratio': 91.92,
                                                                  })))
def test(company, min_salary, excected_value):
    """Final test.

    Args:
        company: company
        min_salary: min salary
        excected_value: excected value
    """
    assert salary_statistics(company, min_salary) == excected_value
