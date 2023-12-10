"""Module that tests the main file."""

import pytest

from hw1 import get_salary_statistics

TEST_DATA_WITH_ARG = (
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
        100,
        (204, 300, 180),
        {
            'lg': {
                'Koo In-hwoi': 225,
                'Koo Cha-kyung': 180,
            },
            'dyson': {
                'James Dyson': 300,
                'Roland Krueger': 145,
            },
            'bosch': {
                'Robert Bosch': 170,
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
)


@pytest.mark.parametrize('minimal_salary, expected, departments', TEST_DATA_WITH_ARG)
def test_function_with_optional_arg(
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


TEST_DATA_WITHOUT_ARG = (
    (
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
        (88, 88, 88),
        {
            'kfc': {
                'Colonel Sanders': 88,
            },
        },
    ),
    (
        (0, 0, 0),
        {
            'xiaomi': {
                'Lei Jun': 0,
            },
            'realme': {
                'Sky Li': 0,
            },
            'oneplus': {
                'Pete Lau': 0,
            },
        },
    ),
)


@pytest.mark.parametrize('expected, departments', TEST_DATA_WITHOUT_ARG)
def test_function_without_optional_arg(
    expected: tuple,
    departments: dict[str, dict[str, float]],
) -> None:
    """Test main module function get_salary_statistics.

    Args:
        expected: tuple - contains expected test outputs,
        departments: dict - key is department, value is dict - str is name, float is salary.
    """
    assert get_salary_statistics(**departments) == expected
