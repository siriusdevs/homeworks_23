import pytest

from hw1 import get_median, calculate_companies_info


data_test_get_median = (
    ([], 0.0),
    ([1], 1.0),
    ([1, 2], 1.5),
    ([1, 2, 3], 2),
    ((1, 2, 3, 4), 2.5),
)


@pytest.mark.parametrize('items, expected', data_test_get_median)
def test_get_median(items, expected) -> None:
    """Test 'get_median' function for correct values.

    Args:
        items (Sequences[int | float]): Sequence of random int or float value.
        expected (float): Median value that has to be a float.
    """
    result = get_median(items)
    assert result == expected and isinstance(result, float)


data_test_calculate_companies_info = (
    (
        None,
        {
            'samsung': {
                'a': 100.0,
                'b': 200.0,
                'c': 300.0,
                'd': 400.0,
            },
            'apple': {
                'a': 2843.349834,
                'b': 324234.324234,
                'c': 12.0,
            }
        },
        {
            'samsung': (250.0, 400.0, 250.0),
            'apple': (109029.89, 324234.32, 324234.32),
        }
    ),
    (
        250.0,
        {
            'samsung': {
                'a': 100.0,
                'b': 200.0,
                'c': 300.0,
                'd': 400.0,
            },
        },
        {
            'samsung': (350.0, 400.0, 350.0),
        }
    ),
    (
        0,
        {
            'Sirius': {},
        },
        {
            'Sirius': (0, 0, 0),
        },
    ),
)


@pytest.mark.parametrize('min_salary, companies, expected', data_test_calculate_companies_info)
def test_calculate_companies_info(min_salary, companies, expected) -> None:
    """Test 'calculate_companies_info' function for correct values.

    Args:
        min_salary (None | int | float): The lower limit of salaries that we consider.
        companies (dict[str, dict[str, float]]): Companies that we consider salaries in.
        expected (dict[str, tuple[float, float, float]]): result calculation of companies.
    """
    assert calculate_companies_info(min_salary, **companies) == expected
