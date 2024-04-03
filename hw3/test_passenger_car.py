import pytest
from hw3 import PassengerCar


def test_init():
    passenger_car = PassengerCar('Toyota', 2022, 30000.0, 5)
    assert passenger_car.model == 'Toyota'
    assert passenger_car.year == 2022
    assert passenger_car.cost == 30000.0
    assert passenger_car.passenger_seats == 5


def test_invalid_passenger_seats_type():
    with pytest.raises(TypeError):
        PassengerCar('Toyota', 2022, 30000.0, '5')


def test_empty_passenger_seats():
    with pytest.raises(TypeError):
        PassengerCar('Toyota', 2022, 30000.0, None)


def test_extra_argument():
    with pytest.raises(TypeError):
        PassengerCar('Toyota', 2022, 30000.0, 5, 'extra')
