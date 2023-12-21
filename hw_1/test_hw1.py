"""Module that tests the main file."""

import pytest

from task1 import company_salary_stats
TEST_DATA_WITH_ARG = (
    (
        300,
        (657, 1000, 725),
        {
            'hasa': {
                'Ani Vbss': 1000,
                'Ohj Fsas': 250,
            },
            'qwerf': {
                'Wedo Qera': 725,
                'Werru Ruka': 170,
                'Riwasd Coki': 220,
            },
            'asdgh': {
                'Uio Ertyi': 815,
                'Kgkod Woijh': 445,
                'Svcx': 300,
            },
        },
    ),
    (
        100,
        (204, 300, 180),
        {
            'tyjkv': {
                'Rggfd Oplkd': 225,
                'Addg Cjjjh': 180,
            },
            'vbn': {
                'Edkn Olo': 300,
                'Rasd Feas': 145,
            },
            'wdfg': {
                'Pooeer Ioiu': 170,
            },
        },
    ),
    (
        250,
        (0, 0, 0),
        {
            'res': {
                'Wfcss Cgrex': 170,
                'Aghy Hgdde': 100,
            },
            'wcvfre': {
                'Lmddf Rvoii': 240,
                'Xioh Gddwe': 99,
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
    """Test main module function company_salary_stats.

    Args:
        minimal_salary: int|float - minimal salary used in statistics,
        expected: tuple - contains the expected test results,
        departments: dict - Key - department, value - dict - str name, float - salary.
    """
    assert company_salary_stats(minimal_salary, **departments) == expected


TEST_DATA_WITHOUT_ARG = (
    (
        (42, 75, 30),
        {
            'uijhbgvc': {
                'Ohj Fsas': 60,
                'Nv Morasky': 30,
                'Marc Laidlaw': 20,
            },
            'tdss': {
                'Efgg RRfddd': 75,
                'Dushinskyy Kijh': 25,
            },
        },
    ),
    (
        (88, 88, 88),
        {
            'sdd': {
                'Loi Plljng': 88,
            },
        },
    ),
    (
        (0, 0, 0),
        {
            'ikjnb': {
                'Wxxxcv Saxxx': 0,
            },
            'nbvcx': {
                'Wss Jkh': 0,
            },
            'plkmnb': {
                'Po Kerdv': 0,
            },
        },
    ),
)


@pytest.mark.parametrize('expected, departments', TEST_DATA_WITHOUT_ARG)
def test_function_without_optional_arg(
    expected: tuple,
    departments: dict[str, dict[str, float]],
) -> None:
    """Test main module function company_salary_stats.

    Args:
        expected: tuple - contains the expected test results,
        departments: dict - key is department, value is dict - str is name, float is salary.
    """
    assert company_salary_stats(**departments) == expected
