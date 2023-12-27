"""Module for testing flight module."""

import pytest

from .. import hw3
from ..flight import Flight


def test_flight_setter_error():
    """Test for flight setter with bad outcome."""
    flight = Flight(1, 'sheremetyevo', 'domodedovo')
    with pytest.raises(hw3.InvalidType):
        flight.flight_num = 'a'
    with pytest.raises(hw3.NegativeNumber):
        flight.flight_num = -1
    with pytest.raises(hw3.InvalidType):
        flight.approaching_arirport = 12313
    with pytest.raises(hw3.InvalidType):
        flight.outcome_airport = 12313


def test_flight_setter_good():
    """Test for flight setter with good outcome."""
    flight = Flight(1, 'some_airport', 'another_airport')
    flight.flight_num = 2
    assert flight.flight_num == 2
    flight.outcome_airport = 'sheremetyevo'
    assert flight.outcome_airport == 'sheremetyevo'
    flight.approaching_arirport = 'babushkino'
    assert flight.approaching_arirport == 'babushkino'
