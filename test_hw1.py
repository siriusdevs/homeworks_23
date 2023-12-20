"""Test hw1.py module."""

import pytest

from hw1 import salary_stats


def test_salary_stats():
    """Test salary_stats function."""

    result = salary_stats(("Dept1", [1000, 2000, 3000, 4000, 5000]), limit=2000)
    assert result == ([3000, 4000, 5000], 75.0)

    result = salary_stats(("Dept1", [1000, 2000, 3000, 4000, 5000]), limit=6000)
    assert result == ([], 0)

    result = salary_stats(("Dept1", [1000, 2000, 3000, 4000, 5000]))
    assert result == ([1000, 2000, 3000], 30.0)

    result = salary_stats(("Dept1", [0, 0, 0, 0, 0]))
    assert result == ([0, 0, 0], 0)
