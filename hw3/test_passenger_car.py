import pytest

from hw3 import PassengerCar

# Tests for PassengerCar class

TOYOTA_MODEL = 'Toyota'
MODEL_YEAR = 2024
CAR_COST = 35000.0


def test_init():
    """Test initialization of PassengerCar object."""
    passenger_car = PassengerCar(TOYOTA_MODEL, MODEL_YEAR, CAR_COST, 5)
    assert passenger_car.model == TOYOTA_MODEL
    assert passenger_car.year == MODEL_YEAR
    assert passenger_car.cost == CAR_COST
    assert passenger_car.passenger_seats == 5


def test_invalid_passenger_seats_type():
    """Test invalid passenger seats type."""
    with pytest.raises(TypeError):
        PassengerCar(TOYOTA_MODEL, MODEL_YEAR, CAR_COST, '5')


def test_empty_passenger_seats():
    """Test empty passenger seats."""
    with pytest.raises(TypeError):
        PassengerCar(TOYOTA_MODEL, MODEL_YEAR, CAR_COST, None)


def test_extra_argument():
    """Test extra argument passed to PassengerCar."""
    with pytest.raises(TypeError):
        PassengerCar(TOYOTA_MODEL, MODEL_YEAR, CAR_COST, 5, 'extra')
