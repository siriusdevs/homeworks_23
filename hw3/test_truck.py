# pylint: disable=W0611
import pytest
from hw3 import Truck


def test_init():
    truck = Truck('Toyota', 2022, 30000.0, 1000.0)
    assert truck.model == 'Toyota'
    assert truck.year == 2022
    assert truck.cost == 30000.0
    assert truck.carrying_capacity == 1000.0


def test_invalid_carrying_capacity_type():
    with pytest.raises(TypeError):
        Truck('Toyota', 2022, 30000.0, '1000.0')


def test_empty_carrying_capacity():
    with pytest.raises(TypeError):
        Truck('Toyota', 2022, 30000.0, None)


def test_extra_argument():
    with pytest.raises(TypeError):
        Truck('Toyota', 2022, 30000.0, 1000.0, 'extra')
