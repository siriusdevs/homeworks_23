"""Test of homework about company's department statistics."""

import pytest

from hw1 import calculate_department_statistics


def test_department_statistics():
    """Tests with correct values."""

    departments = [
        ("HR", {"Alice": 5000, "Bob": 6000}),
        ("IT", {"Charlie": 7000, "David": 8000}),
        ("Finance", {"Eve": 9000, "Frank": 10000}),
    ]

    top_3_highest, top_3_lowest = calculate_department_statistics(*departments)

    assert set(top_3_highest) == {("Finance", 9500.0), ("IT", 7500.0), ("HR", 5500.0)}
    assert set(top_3_lowest) == {("HR", 5500.0), ("IT", 7500.0), ("Finance", 9500.0)}


def test_with_excluded_departments():
    """Test with an excluded department."""

    departments = [
        ("HR", {"Alice": 5000, "Bob": 6000}),
        ("IT", {"Charlie": 7000, "David": 8000}),
        ("Finance", {"Eve": 9000, "Frank": 10000}),
    ]

    excluded_departments = ["HR"]

    top_3_highest, top_3_lowest = calculate_department_statistics(
        *departments,
        excluded_departments=excluded_departments,
        )
    assert set(top_3_highest) == set([("Finance", 9500.0), ("IT", 7500.0)])
    assert set(top_3_lowest) == set([("IT", 7500.0), ("Finance", 9500.0)])


def test_with_empty_departments():
    """Test with an empty list of departments."""

    top_3_highest, top_3_lowest = calculate_department_statistics()

    assert top_3_highest == []
    assert top_3_lowest == []


if __name__ == "__main__":
    pytest.main()
