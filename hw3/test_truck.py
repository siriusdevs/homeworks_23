import pytest
from hw3 import Truck


TOYOTA_MODEL = 'Toyota'
DEFAULT_YEAR = 2022
DEFAULT_COST = 30000.0
DEFAULT_CAPACITY = 1000.0


def test_init():
    """Test initialization of Truck object."""
    truck = Truck(TOYOTA_MODEL, DEFAULT_YEAR, DEFAULT_COST, DEFAULT_CAPACITY)
    assert truck.model == TOYOTA_MODEL
    assert truck.year == DEFAULT_YEAR
    assert truck.cost == DEFAULT_COST
    assert truck.carrying_capacity == DEFAULT_CAPACITY


def test_invalid_carrying_capacity_type():
    """Test invalid carrying capacity type."""
    with pytest.raises(TypeError):
        Truck(TOYOTA_MODEL, DEFAULT_YEAR, DEFAULT_COST, '1000.0')


def test_empty_carrying_capacity():
    """Test empty carrying capacity."""
    with pytest.raises(TypeError):
        Truck(TOYOTA_MODEL, DEFAULT_YEAR, DEFAULT_COST, None)


def test_extra_argument():
    """Test extra argument passed to Truck."""
    with pytest.raises(TypeError):
        Truck(TOYOTA_MODEL, DEFAULT_YEAR, DEFAULT_COST, DEFAULT_CAPACITY, 'extra')
