"""Module for testing tikcet module."""

import pytest

from .. import hw3
from ..flight import Flight
from ..passenger import Passenger
from ..ticket import Ticket


def test_ticket_setter_good():
    """Test for ticket setter whith good outcome."""
    passenger = Passenger('Vadim', '111111')
    flight = Flight(1, 'some_airport', 'another_airport')
    ticket = Ticket(1, flight, passenger)
    new_passenger = Passenger('Den', '666666')
    new_flight = Flight(2, 'sheremetyevo', 'domodedovo')
    ticket.ticket_id = 2
    assert ticket.ticket_id == 2
    ticket.passenger = new_passenger
    assert ticket.passenger == new_passenger
    ticket.flight = new_flight
    assert ticket.flight == new_flight


def test_ticket_setter_bad():
    """Test for ticket setter with bad outcome."""
    passenger = Passenger('Vadim', '111111')
    flight = Flight(1, 'some_airport', 'another_airport')
    ticket = Ticket(1, flight, passenger)
    with pytest.raises(hw3.InvalidType):
        ticket.ticket_id = 'a'
    with pytest.raises(hw3.NegativeNumber):
        ticket.ticket_id = -1
    with pytest.raises(hw3.InvalidType):
        ticket.flight = 1
    with pytest.raises(hw3.InvalidType):
        ticket.passenger = 1
