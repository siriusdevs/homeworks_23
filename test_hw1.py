"""Tests for hw1.py."""

from hw1 import get_salary_stats


def test_get_salary_stats_no_limit():
    """Test get_salary_stats with no limit."""
    stats = get_salary_stats(
        IT={'Alice': 1000.0, 'Bob': 2000.0, 'Charlie': 3000.0},
        HR={'Dave': 4000.0, 'Eve': 5000.0, 'Frank': 6000.0},
    )
    assert stats == ([1000.0, 2000.0, 3000.0], 28.57)


def test_get_salary_stats_with_limit():
    """Test get_salary_stats with a limit."""
    stats = get_salary_stats(
        ('IT',),
        IT={'Alice': 1000.0, 'Bob': 2000.0, 'Charlie': 3000.0},
        HR={'Dave': 4000.0, 'Eve': 5000.0, 'Frank': 6000.0},
    )
    assert stats == ([1000.0, 2000.0, 3000.0], 100.0)


def test_get_salary_stats_no_salaries():
    """Test get_salary_stats with no salaries."""
    stats = get_salary_stats()
    assert stats == ([], 0)
