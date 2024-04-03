"""Tests for PassengerCar class."""
import pytest
from hw3 import PassengerCar


TOYOTA_MODEL = 'Toyota'


def test_init():
    """Test initialization of PassengerCar object."""
    passenger_car = PassengerCar(TOYOTA_MODEL, 2022, 30000.0, 5)
    assert passenger_car.model == TOYOTA_MODEL
    assert passenger_car.year == 2022
    assert passenger_car.cost == 30000.0
    assert passenger_car.passenger_seats == 5


def test_invalid_passenger_seats_type():
    """Test invalid passenger seats type."""
    with pytest.raises(TypeError):
        PassengerCar(TOYOTA_MODEL, 2022, 30000.0, '5')


def test_empty_passenger_seats():
    """Test empty passenger seats."""
    with pytest.raises(TypeError):
        PassengerCar(TOYOTA_MODEL, 2022, 30000.0, None)


def test_extra_argument():
    """Test extra argument passed to PassengerCar."""
    with pytest.raises(TypeError):
        PassengerCar(TOYOTA_MODEL, 2022, 30000.0, 5, 'extra')
