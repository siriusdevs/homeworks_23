"""Module with tests for hw3.flight module."""

import pytest

from ..flight import Flight


def test_flight_getters_happy():
    """Create a flight and assert on its getters."""
    flight = Flight('123', 'Sheremetyevo', 'Dubai')
    assert flight.flight_id == '123'
    assert flight.from_airport == 'Sheremetyevo'
    assert flight.to_airport == 'Dubai'


def test_flight_setters_happy():
    """Create a flight and assert on its setters."""
    flight = Flight('333', 'A', 'B')
    flight.flight_id = '321'
    flight.from_airport = 'Adler'
    flight.to_airport = 'Moscow'
    assert flight.flight_id == '321'
    assert flight.from_airport == 'Adler'
    assert flight.to_airport == 'Moscow'


def test_flight_constructor_errors():
    """Assert that Flight's constructor raises errors for incorrect types."""
    with pytest.raises(TypeError):
        Flight(123, 'C', 'D')
    with pytest.raises(TypeError):
        Flight('444', 42.0, 'Pulkovo')
    with pytest.raises(TypeError):
        Flight('321', 'Anapa', 50.0)


def test_flight_setters_errors():
    """Assert that Flight's setters raise errors for incorrect types."""
    flight = Flight('555', 'Anapa', 'Ekaterinburg')
    with pytest.raises(TypeError):
        flight.flight_id = 42
    with pytest.raises(TypeError):
        flight.from_airport = []
    with pytest.raises(TypeError):
        flight.to_airport = 17
