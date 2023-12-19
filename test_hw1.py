"""Test for hw1.py module."""
import pytest

from hw1 import salary_stat


def test_without_exclude():
    """Test salary_stat function without exclude argument."""
    assert salary_stat(
        ('Marketing', [100.0, 200.0, 300.0]),
        ('hr', [400.0, 500.0, 600.0]),
        ('Prodazh', [700.0, 800.0, 900.0]),
    ) == ([900.0, 800.0, 700.0], 53.33)


def test_with_exclude():
    """Test salary_stat function with exclude argument."""
    assert salary_stat(
        ('IT', [100.0, 200.0, 300.0]),
        ('HR', [400.0, 500.0, 600.0]),
        ('Sales', [700.0, 800.0, 900.0]),
        exclude=('HR', 'Sales'),
    ) == ([300.0, 200.0, 100.0], 100.0)


def test_with_type_error():
    """Test salary_stat function with TypeError."""
    with pytest.raises(TypeError):
        salary_stat(
            ('it', [100.0, 200.0, 300.0]),
            ('HR', [400.0, 500.0, 600.0]),
            ('zakupok', [700.0, 800.0, '900.0']),
        )


def test_with_value_error():
    """Test salary_stat function with ValueError."""
    with pytest.raises(ValueError):
        salary_stat(
            ('IT', [100.0, 200.0, 300.0]),
            ('zakupok', [400.0, 500.0, 600.0]),
            ('Sales', [700.0, 800.0, -900.0]),
        )
