"""Test module for function salary_statistics."""

import pytest

from hw1 import salary_statistics

TEST_SALARIES = (
    (
        (
            ('department_1', [1, 2, 3]),
            ('department_2', [1, 2, 4]),
            ('my_department', [1, 2, 5]),
            ('strange_department', [1, 2, 6]),
        ), None, ([
            ('strange_department', 3.),
            ('my_department', 2.67),
            ('department_2', 2.33),
        ], [
            ('my_department', 2.67),
            ('department_2', 2.33),
            ('department_1', 2.),
        ]),
    ),
    (
        (
            ('department_11', [1, 2, 3]),
            ('department_25', [4, 5, 6]),
            ('new_department', [7, 8, 9]),
            ('very_strange_department', [10, 11, 12]),
        ), 9., ([
            ('new_department', 8.),
            ('department_25', 5.),
            ('department_11', 2.),
        ], [
            ('department_25', 5.),
            ('department_11', 2.),
            ('very_strange_department', .0),
        ]),
    ),
    (
        (
            ('department_71', [1, 2, 3]),
            ('department_72', [4, 5, 6]),
            ('not_my_department', [7, 8, 9]),
            ('not_strange_department', [10, 11, 12]),
        ), .0, ([
            ('department_71', .0),
            ('department_72', .0),
            ('not_my_department', .0),
        ], [
            ('department_72', .0),
            ('not_my_department', .0),
            ('not_strange_department', .0),
        ]),
    ),
    (
        (
            ('department_100', [1, 2, 3]),
            ('department_200', [1, 2, 4]),
            ('my_favorite_department', [1, 2, 5]),
            ('department', [1, 2, 6]),
        ), 6., ([
            ('department', 3.),
            ('my_favorite_department', 2.67),
            ('department_200', 2.33),
        ], [
            ('my_favorite_department', 2.67),
            ('department_200', 2.33),
            ('department_100', 2.),
        ]),
    ),
)


@pytest.mark.parametrize('departments, salary_limit, expected', TEST_SALARIES)
def test_salary_stats(
    departments: tuple[tuple],
    salary_limit: float | None,
    expected: tuple[list],
) -> None:
    """Test salary_statistics function from hw1.py.

    Args:
        departments: tuple with departments names their values.
        salary_limit: the maximum wage value (float) to be taken into account.
        expected (tuple): expected value from function.
    """
    assert salary_statistics(*departments, salary_limit=salary_limit) == expected
