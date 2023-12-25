"""Module for testing HW3 Flight class."""


import pytest

from hw3 import Flight

FLIGHT_DEFAULT = Flight('AB1234', 'Moscow', 'Ekaterinburg')
FLIGHT_TWO = Flight('CD5678', 'Sochi', 'Irkutsk')


def test_flight_valid_getter():
    """Create flight with valid values. Check getters."""
    flight = FLIGHT_DEFAULT
    assert flight.flight_id == 'AB1234'
    assert flight.from_airport == 'Moscow'
    assert flight.to_airport == 'Ekaterinburg'


def test_flight_valid_setter():
    """Change flight values. Check setters."""
    flight = FLIGHT_DEFAULT
    flight.flight_id = 'CD5678'
    flight.from_airport = 'Sochi'
    flight.to_airport = 'Irkutsk'
    assert flight.flight_id == 'CD5678'
    assert flight.from_airport == 'Sochi'
    assert flight.to_airport == 'Irkutsk'


def test_flight_getter_errors():
    """Create flight with invalid values. Check getter errors."""
    with pytest.raises(TypeError):
        Flight(1234, 'Moscow', 'Ekaterinburg')
    with pytest.raises(TypeError):
        Flight('AB1234', 123, 'Ekaterinburg')
    with pytest.raises(TypeError):
        Flight('AB1234', 'Moscow', 123)


def test_flight_setter_errors():
    """Change flight values to invalid ones. Check setter errors."""
    flight = FLIGHT_DEFAULT
    with pytest.raises(TypeError):
        flight.flight_id = 1234
    with pytest.raises(TypeError):
        flight.from_airport = 123
    with pytest.raises(TypeError):
        flight.to_airport = 123
