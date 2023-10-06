"""Test module for HW1."""
import pytest

from hw1 import department_statistics

departments_names = [
    'Programmers',
    'Managers',
    'ML',
    'HR',
    'Designers',
    'DL',
    'Engineers',
]

test_data1 = (
    (departments_names[0], [56.7, 89.3, 99.5]),  # 81.83
    (departments_names[1], [32.9, 54, 100.5, 23.1]),  # 52.62
    (departments_names[2], [123.4, 250.6, 100.3, 300.5]),  # 193.7
    (departments_names[3], [56.7, 89.3, 99.5, 123.3]),  # 92.2
    (departments_names[4], [32.9, 54, 100.5, 23.1]),  # 52.62
    (departments_names[5], [123.4, 250.6, 100.3, 300.5, 45.2, 145.3]),  # 160.88
    (departments_names[6], [56.7, 89.3, 99.5, 87.3, 12.4, 45.9]),  # 65.18
)

expected_data1 = (
    [('Managers', 52.62), ('Designers', 52.62), ('Engineers', 65.18)],
    [('HR', 92.2), ('DL', 160.88), ('ML', 193.7)],
)


@pytest.mark.parametrize('departments, expected', [(test_data1, expected_data1)])
def test_positive_data_without_optional_argument(departments, expected):
    """Positive test without optional argument.

    Args:
        departments: - valid test data without optional argument
        expected: - expected result of the program
    """
    assert department_statistics(*departments) == expected


specific_departments = (
    departments_names[3],
    departments_names[4],
    departments_names[5],
    departments_names[2],
)

expected_data1 = (
    [
        (departments_names[4], 52.62),
        (departments_names[3], 92.2),
        (departments_names[5], 160.88),
    ],
    [
        (departments_names[3], 92.2),
        (departments_names[5], 160.88),
        (departments_names[2], 193.7),
    ],
)


@pytest.mark.parametrize(
    'departments, required_departments, expected',
    [(test_data1, specific_departments, expected_data1)],
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


test_data2 = [
    (departments_names[0], []),
    (departments_names[1], []),
]


@pytest.mark.xfail(test_data2, reason=ZeroDivisionError)
def test_negative_data_division_by_zero(departments):
    """Negative test with ZeroDivisionError.

    Args:
        departments: - invalid test data
    """
    assert department_statistics(*departments)
