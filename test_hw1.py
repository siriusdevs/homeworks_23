"""Test hw1.py module."""

from hw1 import salary_stats

LIMIT = 2000
LIMIT2 = 6000


def test_salary_stats():
    """Test salary_stats function."""
    test1 = salary_stats(('Dept1', [1000, 2000, 3000, 4000, 5000]), limit=LIMIT)
    assert test1 == ([2000, 3000, 4000], 64.29)

    test2 = salary_stats(('Dept2', [1000, 2000, 3000, 4000, 5000]), limit=LIMIT2)
    assert test2 == ([], 0)

    test3 = salary_stats(('Dept3', [1000, 2000, 3000, 4000, 5000]))
    assert test3 == ([1000, 2000, 3000], 40.0)

    test4 = salary_stats(('Dept4', [0, 0, 0, 0, 0]))
    assert test4 == ([0, 0, 0], 0)
