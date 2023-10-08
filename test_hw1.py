"""Testing for module 'top_salaries', homework1."""
import pytest

from hw1 import best_wage

test_data = (
    (
        (
            ('Clothes', {'Telegin': 2000, 'Sachkov': 3000}),
            ('Smartphones', {'Anegin': 20000, 'Homosov': 30000}),
            ('Laptops', {'Lozhechkov': 15000, 'Genaninov': 18000}),
            ('Radio', {'Vilkov': 35000, 'Ternov': 37000}),
            ('Headsets', {'Terrabledov': 50000, 'Monkeykingov': 52250}),
        ),
        ('Laptops', 'Clothes'),
        ([52250, 50000, 37000, '53.1%']),
    ),
    (
        (
            ('Glasses', {'Ochkova': 2000, 'Morkovova': 3000}),
            ('Bags', {'Portfelev': 20000, 'Sumochkina': 30000}),
            ('Pencils', {'Karandashov': 15000, 'Krasnikova': 18000}),
            ('Pens', {'Ruchkina': 35000, 'Nozhov': 37000}),
            ('Markers', {'Enigmov': 50000, 'Shadowfiendov': 52250}),
        ),
        ('Pens'),
        ([52250, 50000, 30000, '50.43%']),
    ),
    (
        (
            ('Jeans', {'Shortova': 2576, 'Sinikova': 3567}),
            ('Hats', {'Kepkina': 23678, 'Nikov': 38467}),
            ('Monitors', {'Acerov': 35365.345, 'Hyperova': 18123.456}),
            ('Bottles', {'Bytilkov': 35678, 'Sobytilnik': 37964}),
            ('Tables', {'Pudgov': 55368, 'Tinkerov': 53439}),
        ),
        ('Tables', 'Bottles'),
        ([38467, 35365.35, 23678, '32.05%']),
    ),
    (
        (
            ("Test's devices", {'Testovich': 2576, 'Testivina': 3567}),
            ('Windows', {'Oknovin': 1360, 'Steklovina': 2450}),
        ),
        ('Pans'),
        ([3567, 2576, 2450, '86.34%']),
    ),
    (
        (),
        (),
        (['Недостаточно данных для использования функции']),
    ),
    (
        (),
        ('Library', 'Beer'),
        (['Недостаточно данных для использования функции']),
    ),
    (
        (
            ('Books', {'Esenina': 35000, 'Bylgakov': 44000}),
            ('Cakes', {'Tortova': 42000, 'Pirozhenkov': 20000}),
        ),
        ('Books', 'Cakes'),
        (['Недостаточно не исключенных отделов для использования функции']),
    ),
    (
        (
            ('Milk', {'Yogurtova': 15500, 'Bylgakov': 23450}),
            ('Chips', {'Laysova': 24680, 'Kartoshkova': 25340}),
        ),
        ('Milk'),
        (['Недостаточно не исключенных отделов для использования функции']),
    ),
)


@pytest.mark.parametrize('departments, exclude_data, expected', test_data)
def test_top_salaries(departments, exclude_data, expected):
    """Compare result of function 'best_wages' and correct answer for every datas.

    Args:
        departments: Tuple[Tuple[str, dict]] - information about departments.
        exclude_data: Tuple[str] - excluded departments.
        expected: list[str | int] - correct answer of best_wages's result.
    """
    assert best_wage(departments, exclude_data) == expected
