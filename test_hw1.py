"""Module that tests the main file."""

import pytest

from hw1 import get_salary_statistics

TEST_DATA = (
    (
        None,
        (42, 75, 30),
        {
            'valve': {
                'Gabe Newell': 60,
                'Mike Morasky': 30,
                'Marc Laidlaw': 20,
            },
            'gsc': {
                'Sergay Grigorovich': 75,
                'Dushinskyy Petro': 25,
            },
        },
    ),
    (
        300,
        (657, 1000, 725),
        {
            'microsoft': {
                'Bill Gaytes': 1000,
                'Gabe Newell': 250,
            },
            'sony': {
                'Akio Morita': 725,
                'Masaru Ibuka': 170,
                'Hiroki Totoki': 220,
            },
            'huawei': {
                'Ren Zhengfei': 815,
                'Xu Jidong': 445,
                'Steve': 300,
            },
        },
    ),
    (
        250,
        (0, 0, 0),
        {
            'hp': {
                'Bill Hewlett': 170,
                'Billy Herrington': 100,
            },
            'samsung': {
                'Lee Byung-chul': 240,
                'Lee Kun-hee': 99,
            },
        },
    ),
    (
        None,
        (88, 88, 88),
        {
            'kfc': {
                'Colonel Sanders': 88,
            },
        },
    ),
)


@pytest.mark.parametrize('minimal_salary, expected, departments', TEST_DATA)
def test_get_salary_statistics(
    minimal_salary: int | float,
    expected: tuple,
    departments: dict[str, dict[str, float]],
) -> None:
    """Test main module function get_salary_statistics.

    Args:
        minimal_salary: int|float - minimal salary which is used in statistics,
        expected: tuple - contains expected test outputs,
        departments: dict - key is department, value is dict - str is name, float is salary.
    """
    assert get_salary_statistics(minimal_salary, **departments) == expected
