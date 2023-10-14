"""Модуль тест для hm.1."""


import pytest

from hm1 import salary_statistics

TEST_DATA = (
    (
        {
            'north': {
                'Nikita': 50000,
                'Sasha': 70000,
                'Masha': 60000,
            },
            'south': {
                'Andrey': 125000,
                'Georgiy': 210000,
                'Anna': 540000,
            },
            'west': {
                'Misha': 4400,
                'Natasha': 8800,
                'Grisha': 3800,
            },
            'east': {
                'Kostya': 65000,
                'Vanya': 87000,
                'Kira': 71000,
            },
        },
        (['north', 'east', 'south'], ['west', 'north', 'east']),
    ),
    (
        {
            'exclude_department': ('accounting', 'financial', 'quality', 'development'),
            'accounting': {
                'Roman': 58000,
                'Kris': 71000,
                'Mariana': 66000,
            },
            'financial': {
                'Anna': 112000,
                'Josef': 21000,
                'Jostar': 54000,
            },
            'quality': {
                'Djek': 44000,
                'Vein': 88000,
                'Genry': 38000,
            },
            'development': {
                'Milana': 65000,
                'Richard': 47100,
                'Katy': 71000,
            },
        },
        ([], []),
    ),
    (
        {
            'exclude_department': ('Konoha', 'Iva'),
            'Konoha': {
                'Naruto': 1111,
                'Saske': 72323,
                'Orochimary': 3232.23,
            },
            'Iva': {
                'Deidara': 1123230,
                'Suchicage': 21000,
                'Anna': 0,
            },
            'Kiri': {
                'Mei': 44000,
                'Dzabydza': 0,
            },
            'Syna': {
                'Gaara': 632300,
                'Sasori': 130000,
            },
        },
        (['Kiri', 'Syna'], ['Kiri', 'Syna']),
    ),
)

TEST_DATA_INVALID = (
    (
        {
            'sales': {
            },
            'supplies': {
                'Peter': 44000,
            },
            'marketing': {
                'Hunry': 632300,
                'Jon': 130000,
            },
        },
        (['supplies', 'marketing'], ['supplies', 'marketing']),
    ),
)


@pytest.mark.parametrize('kwargs, expected', TEST_DATA)
def test_salary_statistics(kwargs: dict[str, float], expected: list) -> None:
    """Тест функции salary_statistics.

    Args:
        kwargs (dict[str, float]): тестовые данные
        expected (list): результат
    """
    assert salary_statistics(**kwargs) == expected


@pytest.mark.xfail(raises=Exception)
def test_invalid_salary_statistics():
    """Тест функции salary_statistics на ошибки."""
    salary_statistics(TEST_DATA_INVALID)
