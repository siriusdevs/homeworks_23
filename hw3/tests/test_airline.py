"""Module for testing airline module."""
import pytest

from .. import hw3
from ..airline import Airline
from ..flight import Flight
from ..passenger import Passenger
from ..ticket import Ticket


def test_airline_setter_good():
    """Test for airline setter with good outcome."""
    airline = Airline(None, None, None)
    passenger = Passenger('Vadim', '111111')
    flight = Flight(1, 'some_airport', 'another_airport')
    ticket = Ticket(1, flight, passenger)
    airline.tickets = [ticket]
    assert airline.tickets == [ticket]


def test_airline_setter_bad():
    """Test for airline getter with bad outcome."""
    airline = Airline(None, None, None)
    passenger = Passenger('Vadim', '111111')
    flight = Flight(1, 'some_airport', 'another_airport')
    ticket = Ticket(1, flight, passenger)
    with pytest.raises(hw3.InvalidType):
        airline.tickets = 'some_string'
    with pytest.raises(hw3.InvalidType):
        airline.tickets = [ticket, 'some_string']


def test_add_passenger():
    """Test for adding passenger."""
    airline = Airline(None, None, None)
    with pytest.raises(hw3.InvalidType):
        airline.add_passenger('some_sring')


def test_del_passengers():
    """Test for deleting passenger."""
    passenger = Passenger('some_not_existing_passenger', '111111')
    airline = Airline(None, None, None)
    with pytest.raises(hw3.InvalidType):
        airline.del_passenger('invalid_type')
    with pytest.raises(ValueError):
        airline.del_passenger(passenger)


def test_add_flight():
    """Test for adding flight."""
    airline = Airline(None, None, None)
    with pytest.raises(hw3.InvalidType):
        airline.add_flight('some_sring')


def test_del_flight():
    """Test for deleting flight."""
    flight = Flight(1, 'sheremetyevo', 'domodedovo')
    airline = Airline(None, None, None)
    with pytest.raises(hw3.InvalidType):
        airline.del_flight('invalid_type')
    with pytest.raises(ValueError):
        airline.del_flight(flight)


def test_buy_ticket():
    """Test for adding ticket."""
    airline = Airline(None, None, None)
    with pytest.raises(hw3.InvalidType):
        airline.buy_ticket('some_text')


def test_cancel_ticket():
    """Test for deleting ticket."""
    flight = Flight(1, 'sheremetyevo', 'domodedovo')
    passenger = Passenger('Vadim', '112121')
    not_existing_ticket = Ticket(1, flight, passenger)
    airline = Airline(None, None, None)
    with pytest.raises(hw3.InvalidType):
        airline.cancel_ticket('invalid_type')
    with pytest.raises(ValueError):
        airline.cancel_ticket(not_existing_ticket)
