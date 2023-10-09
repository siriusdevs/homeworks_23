"""Модуль тест для hm.1"""


import pytest

from hm1 import salary_statistics


test_data = (
    (
        {
            'north': {
                'Nikita': 50000,
                'Sasha': 70000,
                'Masha': 60000
            },
            'south': {
                'Andrey': 125000,
                'Georgiy': 210000,
                'Anna': 540000
            },
            'west': {
                'Misha': 4400,
                'Natasha': 8800,
                'Grisha': 3800
            },
            'east': {
                'Kostya': 65000,
                'Vanya': 87000,
                'Kira': 71000
            }
        },
        (['north', 'east', 'south'], ['west', 'north', 'east'])
    ),
    (
        {
            'exclude_department': ('north', 'south', 'west', 'east'),
            'north': {
                'Nikita': 58000,
                'Sasha': 71000,
                'Masha': 66000
            },
            'south': {
                'Andrey': 112000,
                'Georgiy': 21000,
                'Anna': 54000
            },
            'west': {
                'Misha': 44000,
                'Natasha': 88000,
                'Grisha': 38000
            },
            'east': {
                'Kostya': 65000,
                'Vanya': 47100,
                'Kira': 71000
            }
        },
        ([], [])
    ),
    (
        {
            'exclude_department': ('north', 'south'),
            'north': {
                'Nikita': 1111,
                'Sasha': 72323,
                'Masha': 3232.23
            },
            'south': {
                'Andrey': 1123230,
                'Georgiy': 21000,
                'Anna': 0
            },
            'west': {
                'Misha': 44000,
            },
            'east': {
                'Kostya': 632300,
                'Vanya': 130000
            }
        },
        (['west', 'east'], ['west', 'east'])
    ),
    (
        {
            'south': {

            },
            'west': {
                'Misha': 44000,
            },
            'east': {
                'Kostya': 632300,
                'Vanya': 130000
            }
        },
        (['west', 'east'], ['west', 'east'])
    )
)


@pytest.mark.parametrize('args, expected', test_data)
def test_worst_best_department(args: dict[str, float], expected: list) -> None:
    """Тест функции salary_statistics

    Args:
        args (dict[str, float]): тестовые данные
        expected (list): результат
    """
    assert salary_statistics(**args) == expected
