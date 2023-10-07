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
            ('Headsets', {'Terrabled': 50000, 'Monkeykingov': 52250}),
        ),
        ('Laptops', 'Clothes'),
        ([52250, 50000, 37000, '53.1%']),
    ),
    (
        (
            ('Clothes', {'Telegin': 2000, 'Sachkov': 3000}),
            ('Smartphones', {'Anegin': 20000, 'Homosov': 30000}),
            ('Laptops', {'Lozhechkov': 15000, 'Genaninov': 18000}),
            ('Radio', {'Vilkov': 35000, 'Ternov': 37000}),
            ('Headsets', {'Terrabled': 50000, 'Monkeykingov': 52250}),
        ),
        ('Radio'),
        ([52250, 50000, 30000, '50.43%']),
    ),
    (
        (
            ('Jeans', {'Telegin': 2576, 'Sachkov': 3567}),
            ('Hats', {'Anegin': 23678, 'Homosov': 38467}),
            ('Monitors', {'Lozhechkov': 35365.345, 'Genaninov': 18123.456}),
            ('Bottles', {'Vilkov': 35678, 'Ternov': 37964}),
            ('Tables', {'Terrabled': 55368, 'Monkeykingov': 53439}),
        ),
        ('Tables', 'Bottles'),
        ([38467, 35365.35, 23678, '32.05%']),
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
