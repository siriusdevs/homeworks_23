"""Test module for HW1."""
import pytest

from hw1 import department_statistics

DEPARTMENTS_NAMES = (
    'Programmers',
    'Managers',
    'ML',
    'HR',
    'Designers',
    'DL',
    'Engineers',
)

TEST_DATA1 = (
    (DEPARTMENTS_NAMES[0], [56.7, 89.3, 99.5]),  # 81.83
    (DEPARTMENTS_NAMES[1], [32.9, 54, 100.5, 23.1]),  # 52.62
    (DEPARTMENTS_NAMES[2], [123.4, 250.6, 100.3, 300.5]),  # 193.7
    (DEPARTMENTS_NAMES[3], [56.7, 89.3, 99.5, 123.3]),  # 92.2
    (DEPARTMENTS_NAMES[4], [32.9, 54, 100.5, 23.1]),  # 52.62
    (DEPARTMENTS_NAMES[5], [123.4, 250.6, 100.3, 300.5, 45.2, 145.3]),  # 160.88
    (DEPARTMENTS_NAMES[6], [56.7, 89.3, 99.5, 87.3, 12.4, 45.9]),  # 65.18
)

EXPECTED_DATA1 = (
    [DEPARTMENTS_NAMES[1], DEPARTMENTS_NAMES[4], DEPARTMENTS_NAMES[6]],
    [DEPARTMENTS_NAMES[3], DEPARTMENTS_NAMES[5], DEPARTMENTS_NAMES[2]],
)


@pytest.mark.parametrize('departments, expected', [(TEST_DATA1, EXPECTED_DATA1)])
def test_positive_data_without_optional_argument(departments, expected):
    """Positive test without optional argument.

    Args:
        departments: - valid test data without optional argument
        expected: - expected result of the program
    """
    assert department_statistics(*departments) == expected


SPECIFIC_DEPARTMENTS = (
    DEPARTMENTS_NAMES[3],
    DEPARTMENTS_NAMES[4],
    DEPARTMENTS_NAMES[5],
    DEPARTMENTS_NAMES[2],
)

EXPECTED_DATA2 = (
    [
        DEPARTMENTS_NAMES[4],
        DEPARTMENTS_NAMES[3],
        DEPARTMENTS_NAMES[5],
    ],
    [
        DEPARTMENTS_NAMES[3],
        DEPARTMENTS_NAMES[5],
        DEPARTMENTS_NAMES[2],
    ],
)


@pytest.mark.parametrize(
    'departments, required_departments, expected',
    [(TEST_DATA1, SPECIFIC_DEPARTMENTS, EXPECTED_DATA2)],
)
def test_positive_data_with_optional_argument(
    departments, required_departments, expected,
):
    """Positive test with optional argument.

    Args:
        departments: - valid test data without optional argument
        required_departments: - optional argument
        expected: - expected result of the program
    """
    assert department_statistics(
        *departments,
        specific_departments=required_departments,
    ) == expected


TEST_DATA2 = [
    (DEPARTMENTS_NAMES[0], []),
    (DEPARTMENTS_NAMES[1], []),
]


@pytest.mark.xfail(TEST_DATA2, reason=ZeroDivisionError)
def test_negative_data_division_by_zero(departments):
    """Negative test with ZeroDivisionError.

    Args:
        departments: - invalid test data
    """
    assert department_statistics(*departments)
