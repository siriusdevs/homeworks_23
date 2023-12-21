"""Module for testing hw1.py."""


from typing import Optional

import pytest

from hw1 import get_departments_rating

DEPARTMENT_A = 'Department A'
DEPARTMENT_B = 'Department B'
DEPARTMENT_C = 'Department C'
DEPARTMENT_D = 'Department D'

EMPLOYEE_A = 'Employee A'
EMPLOYEE_B = 'Employee B'
EMPLOYEE_C = 'Employee C'
EMPLOYEE_D = 'Employee D'
EMPLOYEE_E = 'Employee E'
EMPLOYEE_F = 'Employee F'
EMPLOYEE_G = 'Employee G'
EMPLOYEE_H = 'Employee H'

SALARY_A = 90000
SALARY_B = 100000
SALARY_C = 500000
SALARY_D = 150000
SALARY_F = -50000

VALID_TEST_DATA = (
    ({}, None, ([], [])),
    ({}, (), ([], [])),
    (
        {},
        (
            DEPARTMENT_A,
            DEPARTMENT_B,
            DEPARTMENT_C,
        ),
        ([], []),
    ),
    (
        {
            DEPARTMENT_A: {
                EMPLOYEE_A: SALARY_A,
                EMPLOYEE_B: SALARY_B,
            },
            DEPARTMENT_B: {
                EMPLOYEE_C: SALARY_C,
                EMPLOYEE_D: SALARY_C,
                EMPLOYEE_E: SALARY_C,
                EMPLOYEE_F: SALARY_C,
                EMPLOYEE_G: SALARY_C,
            },
            DEPARTMENT_C: {
                EMPLOYEE_H: SALARY_D,
            },
        },
        None,
        (
            [
                DEPARTMENT_B,
                DEPARTMENT_C,
                DEPARTMENT_A,
            ],
            [
                DEPARTMENT_A,
                DEPARTMENT_C,
                DEPARTMENT_B,
            ],
        ),
    ),
    (
        {
            DEPARTMENT_A: {
                EMPLOYEE_A: SALARY_A,
                EMPLOYEE_B: SALARY_B,
            },
            DEPARTMENT_B: {
                EMPLOYEE_C: SALARY_C,
                EMPLOYEE_D: SALARY_C,
                EMPLOYEE_E: SALARY_C,
                EMPLOYEE_F: SALARY_C,
                EMPLOYEE_G: SALARY_C,
            },
            DEPARTMENT_C: {
                EMPLOYEE_H: SALARY_D,
            },
        },
        (
            DEPARTMENT_A,
            DEPARTMENT_C,
        ),
        (
            [
                DEPARTMENT_C,
                DEPARTMENT_A,
            ],
            [
                DEPARTMENT_A,
                DEPARTMENT_C,
            ],
        ),
    ),
    (
        {
            DEPARTMENT_A: {
                EMPLOYEE_A: SALARY_A,
                EMPLOYEE_B: SALARY_B,
            },
            DEPARTMENT_B: {
                EMPLOYEE_C: SALARY_C,
                EMPLOYEE_D: SALARY_C,
                EMPLOYEE_E: SALARY_C,
                EMPLOYEE_F: SALARY_C,
                EMPLOYEE_G: SALARY_C,
            },
            DEPARTMENT_C: {
                EMPLOYEE_H: SALARY_D,
            },
            DEPARTMENT_D: {},
        },
        (
            DEPARTMENT_A,
            DEPARTMENT_C,
            DEPARTMENT_D,
        ),
        (
            [
                DEPARTMENT_C,
                DEPARTMENT_A,
            ],
            [
                DEPARTMENT_A,
                DEPARTMENT_C,
            ],
        ),
    ),
)


@pytest.mark.parametrize('departments, include_deps, expected', VALID_TEST_DATA)
def test_get_stats(
    departments: dict[str, dict[str, float]],
    include_deps: Optional[tuple[str]],
    expected: tuple,
):
    """Check the correctness of the calculated statistics.

    Args:
        departments (dict): company departments with employee salaries.
        include_deps (tuple | None): departments included in the statistics, defaults to None.
        expected (tuple): the expected return.
    """
    assert get_departments_rating(departments, include_deps) == expected


invalid_test_data = (
    (
        {
            DEPARTMENT_A: {
                EMPLOYEE_A: SALARY_F,
            },
        },
    ),
)


@pytest.mark.xfail(raises=ValueError)
def test_invalid_test_data():
    """Check error handling."""
    for invalid_test_data_elem in invalid_test_data:
        get_departments_rating(*invalid_test_data_elem)
