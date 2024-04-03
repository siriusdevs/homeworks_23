import pytest
from hw3 import Truck

TOYOTA_MODEL = 'Toyota'


def test_init():
    """Test initialization of Truck object."""
    truck = Truck(TOYOTA_MODEL, 2022, 30000.0, 1000.0)
    assert truck.model == TOYOTA_MODEL
    assert truck.year == 2022
    assert truck.cost == 30000.0
    assert truck.carrying_capacity == 1000.0


def test_invalid_carrying_capacity_type():
    """Test invalid carrying capacity type."""
    with pytest.raises(TypeError):
        Truck(TOYOTA_MODEL, 2022, 30000.0, '1000.0')


def test_empty_carrying_capacity():
    """Test empty carrying capacity."""
    with pytest.raises(TypeError):
        Truck(TOYOTA_MODEL, 2022, 30000.0, None)


def test_extra_argument():
    """Test extra argument passed to Truck."""
    with pytest.raises(TypeError):
        Truck(TOYOTA_MODEL, 2022, 30000.0, 1000.0, 'extra')
