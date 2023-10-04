"""Test module for HW1."""
import pytest

from hw1 import dept_stat

depts = ['Programmers', 'Managers', 'ML', 'HR', 'Designers', 'DL', 'Engineers']

test_data1 = (
    (depts[0], [56.7, 89.3, 99.5]),  # 81.83
    (depts[1], [32.9, 54, 100.5, 23.1]),  # 52.62
    (depts[2], [123.4, 250.6, 100.3, 300.5]),  # 193.7
    (depts[3], [56.7, 89.3, 99.5, 123.3]),  # 92.2
    (depts[4], [32.9, 54, 100.5, 23.1]),  # 52.62
    (depts[5], [123.4, 250.6, 100.3, 300.5, 45.2, 145.3]),  # 160.88
    (depts[6], [56.7, 89.3, 99.5, 87.3, 12.4, 45.9]),  # 65.18
)

expected_data1 = (
    [('Managers', 52.62), ('Designers', 52.62), ('Engineers', 65.18)],
    [('HR', 92.2), ('DL', 160.88), ('ML', 193.7)],
)


@pytest.mark.parametrize('args, expected', [(test_data1, expected_data1)])
def test_positive_data_without_opt_arg(args, expected):
    """Positive test without optional argument.

    Args:
        args: - valid test data without optional argument
        expected: - expected result of the program
    """
    assert dept_stat(*args) == expected


dept1 = (depts[3], depts[4], depts[5], depts[2])

expected_data1 = (
    [(depts[4], 52.62), (depts[3], 92.2), (depts[5], 160.88)],
    [(depts[3], 92.2), (depts[5], 160.88), (depts[2], 193.7)],
)


@pytest.mark.parametrize('args, dept, expected', [(test_data1, dept1, expected_data1)])
def test_positive_data_with_opt_arg(args, dept, expected):
    """Positive test with optional argument.

    Args:
        args: - valid test data without optional argument
        dept: - optional argument
        expected: - expected result of the program
    """
    assert dept_stat(*args, cur_dept=dept) == expected


test_data2 = [
    (depts[0], []),
    (depts[1], []),
]


@pytest.mark.xfail(test_data2, reason=ZeroDivisionError)
def test_negative_data_division_by_zero(args):
    """Negative test with ZeroDivisionError.

    Args:
        args: - invalid test data
    """
    assert dept_stat(*args)
