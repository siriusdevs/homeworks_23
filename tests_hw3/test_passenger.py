"""Module for testing HW3 Passenger class."""


import pytest

from ..hw3 import Passenger

PASSENGER_DEFAULT = Passenger('Alexey', '123456')
PASSENGER_TWO = Passenger('Boris', '987654')


def test_passenger_valid_getter():
    """Create passenger with valid values. Check getters."""
    passenger = PASSENGER_DEFAULT
    assert passenger.name == 'Alexey'
    assert passenger.passport_id == '123456'


def test_passenger_valid_setter():
    """Change passenger values. Check setters."""
    passenger = PASSENGER_DEFAULT
    passenger.name = 'Boris'
    passenger.passport_id = '987654'
    assert passenger.name == 'Boris'
    assert passenger.passport_id == '987654'


def test_passenger_getter_errors():
    """Create passenger with invalid values. Check getter errors."""
    with pytest.raises(TypeError):
        Passenger(413737, '123456')
    with pytest.raises(TypeError):
        Passenger('Alexey', 123456)
    with pytest.raises(ValueError):
        Passenger('Alexey', '123')
    with pytest.raises(ValueError):
        Passenger('Alexey', 'ID1234')


def test_passenger_setter_errors():
    """Change passenger values to invalid ones. Check setter errors."""
    passenger = PASSENGER_DEFAULT
    with pytest.raises(TypeError):
        passenger.name = 413737
    with pytest.raises(TypeError):
        passenger.passport_id = 123456
    with pytest.raises(ValueError):
        passenger.passport_id = '123'
    with pytest.raises(ValueError):
        passenger.passport_id = 'ID1234'
