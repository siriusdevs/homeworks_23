"""Test module for function salary_statistics from hw1.py."""

import pytest

from hw1 import salary_statistics

TEST_SALARIES = (
        (
            (
                ('department_1', [1, 2, 3]),
                ('department_2', [1, 2, 4]),
                ('department_3', [1, 2, 5]),
                ('department_4', [1, 2, 6]),
            ), None, ([
                ('department_4', 3.0),
                ('department_3', 2.67),
                ('department_2', 2.33),
                                  ], [
                ('department_3', 2.67),
                ('department_2', 2.33),
                ('department_1', 2.0)
            ])
        ),
        (
            (
                ('department_1', [1, 2, 3]),
                ('department_2', [4, 5, 6]),
                ('department_3', [7, 8, 9]),
                ('department_4', [10, 11, 12]),
            ), 9., ([
                ('department_3', 8.0),
                ('department_2', 5.0),
                ('department_1', 2.0),
                                  ], [
                ('department_2', 5.0),
                ('department_1', 2.0),
                ('department_4', 0.0)
            ])
        ),
        (
            (
                ('department_1', [1, 2, 3]),
                ('department_2', [4, 5, 6]),
                ('department_3', [7, 8, 9]),
                ('department_4', [10, 11, 12]),
            ), .0, ([
                ('department_1', 0.0),
                ('department_2', 0.0),
                ('department_3', 0.0)
                               ], [
                ('department_2', 0.0),
                ('department_3', 0.0),
                ('department_4', 0.0)
            ])
        ),
        (
            (
                ('department_1', [1, 2, 3]),
                ('department_2', [1, 2, 4]),
                ('department_3', [1, 2, 5]),
                ('department_4', [1, 2, 6]),
            ), 6., ([
                ('department_4', 3.0),
                ('department_3', 2.67),
                ('department_2', 2.33),
                                  ], [
                ('department_3', 2.67),
                ('department_2', 2.33),
                ('department_1', 2.0)
            ])
        )
)


@pytest.mark.parametrize('departments, salary_limit, expected', TEST_SALARIES)
def test_salary_stats(departments: tuple[tuple[str, list[float]]],
                      salary_limit: float | None,
                      expected: tuple[list[tuple[str, float]], list[tuple[str, float]]]) -> None:
    """Test salary_statistics function from hw1.py.

    Args:
        departments: tuple with departments names their values.
        salary_limit: the maximum wage value (float) to be taken into account.
        expected (tuple): expected value from function.
    """
    assert salary_statistics(*departments, salary_limit=salary_limit) == expected
