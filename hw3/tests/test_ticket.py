"""Module with tests for hw3.ticket."""

import pytest

from ..flight import Flight
from ..passenger import Passenger
from ..ticket import Ticket

_T_PASSENGER = Passenger('Alice', '123456')
_T_FLIGHT = Flight('456', 'A', 'B')


def test_ticket_constructor_and_getters_happy():
    """Create a ticket and assert on its getters."""
    ticket = Ticket('123', _T_PASSENGER, _T_FLIGHT)
    assert ticket.ticket_id == '123'
    assert ticket.passenger == _T_PASSENGER
    assert ticket.flight == _T_FLIGHT


def test_ticket_setters_happy():
    """Create a ticket, use its setters, and assert on result."""
    ticket = Ticket('999', _T_PASSENGER, _T_FLIGHT)
    new_ticket_id = '111'
    new_passenger = Passenger('Bob', '888888')
    new_flight = Flight('456', 'Adler', 'Sheremetyevo')
    ticket.ticket_id = new_ticket_id
    ticket.passenger = new_passenger
    ticket.flight = new_flight
    assert ticket.ticket_id == new_ticket_id
    assert ticket.passenger == new_passenger
    assert ticket.flight == new_flight


def test_ticket_constructor_errors():
    """Assert that creating ticket with incorrect values raises an error."""
    with pytest.raises(TypeError):
        Ticket(123, _T_PASSENGER, _T_FLIGHT)
    with pytest.raises(TypeError):
        Ticket('999', 'fake passenger', _T_FLIGHT)
    with pytest.raises(TypeError):
        Ticket('333', _T_PASSENGER, 'fake flight')


def test_ticket_setters_errors():
    """Creates a ticket and asserts that trying to set invalid values throws."""
    ticket = Ticket('999', _T_PASSENGER, _T_FLIGHT)
    with pytest.raises(TypeError):
        ticket.ticket_id = []
    with pytest.raises(TypeError):
        ticket.passenger = {}
    with pytest.raises(TypeError):
        ticket.flight = 444
