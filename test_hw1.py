import pytest

from hw1 import top_salary

TEST_BASIC = (
    (
        {
            'DB': {'John': 5000.0, 'Alice': 6000.0},
            'HR': {'Bob': 4000.0, 'Carol': 4500.0, 'David': 4200.0},
            'Sales': {'Emily': 5500.0, 'Frank': 5200.0}
        },
        None, ([6000.0, 5500.0, 5200.0], 48.55)
    ),
    (
        {
            'IT': {'John': 4500.0, 'Alice': 300.0},
            'HR': {'Bob': 1234.0, 'Carol': 523.0, 'David': 100.0},
            'Sales': {'Emily': 550.0, 'Frank': 12.0}
        },
        None, ([4500.0, 1234.0, 550.0], 87.05)
    ),
    (
        {
            'IT': {'John': 5000.0, 'Alice': 6000.0},
            'HR': {'Bob': 4000.0, 'Carol': 4500.0, 'David': 4200.0},
            'Sales': {'Emily': 5500.0, 'Frank': 5200.0}
        },
        5900, ([5500.0, 5200.0, 5000.0], 45.64)
    ),
    (
        {
            'IT': {'John': 5000.0, 'Alice': 6000.0},
            'HR': {'Bob': 4000.0, 'Carol': 4500.0, 'David': 4200.0},
            'Sales': {'Emily': 5500.0, 'Frank': 5200.0}
        },
        12, ([], 0.0)
    )
)


@pytest.mark.parametrize('departments, limit_salary, expected', TEST_BASIC)
def test_top_salaries_basic(departments, limit_salary, expected):
    """Test function for `top_salary` to validate basic functionality.

    Args:
        departments: A dictionary representing departments and their workers.
        limit_salary: The salary limit.
        expected: The expected output.
    """
    assert top_salary(limit_salary, **departments) == expected


TEST_ERRORS = (
    (
        {
            'IT': 'test',
            'HR': {'Bob': 4000.0, 'Carol': 4500.0, 'David': 4200.0},
            'Sales': {'Emily': 5500.0, 'Frank': 5200.0}
        },
        None, TypeError
    ),
    (
        {},
        None, ValueError
    ),
    (
        {
            12: {'Jame': 4500.0, 'Alice': 300.0},
            'HR': {'Bob': 1234.0, 'Carol': 523.0, 'David': 100.0},
            'Sales': {'Emily': 550.0, 'Frank': 12.0}
        },
        None, TypeError
    ),
    (
        {
            'IT': {12: 4500.0, 'Alice': 300.0},
            'HR': {'Bob': 1234.0, 'Carol': 523.0, 'David': 100.0},
            'Sales': {'Emily': 550.0, 'Frank': 12.0}
        },
        None, TypeError
    ),
    (
        {
            'IT': {'Jame': 1200, 'Alice': 300.0},
            'HR': {'Bob': 1234.0, 'Carol': 523.0, 'David': 100.0},
            'Sales': {'Emily': 550.0, 'Frank': 12.0}
        },
        None, TypeError
    ),
    (
        {
            'IT': {'Jame': 1200, 'Alice': 300.0},
            'HR': {'Bob': 'test', 'Carol': 523.0, 'David': 100.0},
            'Sales': {'Emily': 550.0, 'Frank': 12.0}
        },
        None, TypeError
    )
)


@pytest.mark.parametrize('departments, limit_salary, expected', TEST_ERRORS)
def test_top_salaries_errors(departments, limit_salary, expected):
    """Test function for `top_salary` to validate basic functionality.

    Args:
        departments: A dictionary representing departments and their workers.
        limit_salary: The salary limit.
        expected: The expected output.
    """
    with pytest.raises(expected):
        top_salary(limit_salary, **departments)
