"""Testing module hw1.py."""
import pytest

from hw1.hw1 import calculate_salary

TEST_CASES = (
    (
        {'IT': {'John': 5000.0, 'Jane': 6000.0, 'Bob': 4500.0}},
        None,
        (100.0, [4500.0, 5000.0, 6000.0]),
    ),
    (
        {},
        None,
        (),
    ),
    (
        {'IT': {'John': 5000.0, 'Jane': 6000.0, 'Bob': 4500.0}},
        6000.0,
        (100.0, [6000.0]),
    ),
    (
        {'IT': {'John': 5000.0, 'Jane': 6000.0, 'Bob': 4500.0}},
        4500.0,
        (100.0, [4500.0, 5000.0, 6000.0]),
    ),
    (
        {'IT': {'John': 5000.0, 'Jane': 6000.0, 'Bob': 4500.0}},
        5000.0,
        (100.0, [5000.0, 6000.0]),
    ),
    (
        {'IT': {'John': -5000.0, 'Jane': -6000.0, 'Bob': -4500.0}},
        None,
        (100.0, [-6000.0, -5000.0, -4500.0]),
    ),
    (
        {'IT': {'John': 5000.0, 'Jane': 5000.0, 'Bob': 5000.0}},
        None,
        (100.0, [5000.0, 5000.0, 5000.0]),
    ),
    (
        {
            'IT': {'John': 5000.0, 'Jane': 5000.0, 'Bob': 5000.0},
            'Phones': {'Alex': 2500.66, 'Alice': 2512.1428},
        },
        None,
        (50.03, [2500.66, 2512.14, 5000.0]),
    ),
)


@pytest.mark.parametrize('departments, limit, expected_result', TEST_CASES)
def test_calculate_salary(
    departments: dict,
    limit: float | None,
    expected_result: tuple[float, list[float]],
) -> None:
    """
    Test the calculate_salary function with different scenarios.

    Args:
        departments: keyword arguments, where values containing employees' names and salaries.
        limit: Salary limit to consider.
        expected_result: Expected result tuple containing the percentage and rounded top salaries.
    """
    assert calculate_salary(limit, **departments) == expected_result
