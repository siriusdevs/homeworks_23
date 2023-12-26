"""Test of homework about company's department statistics."""

from hw1 import calculate_department_statistics

HR: str = 'HR'
IT: str = 'IT'
Finance: str = 'Finance'
Empty: list = []
departments = [
    (HR, {'Alice': 5000, 'Bob': 6000}),
    (IT, {'Charlie': 7000, 'David': 8000}),
    (Finance, {'Eve': 9000, 'Frank': 10000}),
]


def test_department_statistics():
    """Tests with correct values."""
    top_three_highest, top_three_lowest = calculate_department_statistics(*departments)

    assert set(top_three_highest) == {(Finance, 9500.0), (IT, 7500.0), (HR, 5500.0)}
    assert set(top_three_lowest) == {(HR, 5500.0), (IT, 7500.0), (Finance, 9500.0)}


def test_with_excluded_departments():
    """Test with an excluded department."""
    excluded_departments = {HR}

    top_three_highest, top_three_lowest = calculate_department_statistics(
        *departments,
        excluded_departments=excluded_departments,
    )
    assert set(top_three_highest) == {(Finance, 9500.0), (IT, 7500.0)}
    assert set(top_three_lowest) == {(IT, 7500.0), (Finance, 9500.0)}


def test_with_empty_departments():
    """Test with an empty list of departments."""
    top_three_highest, top_three_lowest = calculate_department_statistics()

    assert top_three_highest == Empty
    assert top_three_lowest == Empty
