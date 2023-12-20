"""Module with tests for Aviacompany's aggregation methods."""


import pytest

from ..flight import Flight
from ..passenger import Passenger
from ..ticket import Ticket
from . import test_aviacompany as ta


def test_add_flight():
    """Asserts that adding flight to aviacompany works and raises."""
    sut = ta.create_test_aviacompany()
    new_flight = ta.T_FLIGHTS[0]
    want_new_flights = sut.flights + list(ta.T_FLIGHTS[:1])
    sut.add_flight(new_flight)
    assert sut.flights == want_new_flights

    with pytest.raises(TypeError):
        sut.add_flight(123)


def test_delete_flight():
    """Asserts that deleting a flight works and raises."""
    sut = ta.create_test_aviacompany()
    sut.delete_flight(ta.T_FLIGHTS[0])
    assert sut.flights == list(ta.T_FLIGHTS[1:])

    with pytest.raises(ValueError):
        sut.delete_flight(Flight('5', 'X', 'Y'))


def test_add_passenger():
    """Asserts that adding passenger to aviacompany works and raises."""
    sut = ta.create_test_aviacompany()
    new_passenger = ta.T_PASSENGERS[0]
    want_new_passengers = sut.passengers + list(ta.T_PASSENGERS[:1])
    sut.add_passenger(new_passenger)
    assert sut.passengers == want_new_passengers

    with pytest.raises(TypeError):
        sut.add_passenger({})


def test_delete_passenger():
    """Asserts that deleting a passenger works and raises."""
    sut = ta.create_test_aviacompany()
    sut.delete_passenger(ta.T_PASSENGERS[0])
    assert sut.passengers == list(ta.T_PASSENGERS[1:])

    with pytest.raises(ValueError):
        sut.delete_passenger(Passenger('Sam', '888888'))


def test_add_ticket():
    """Asserts that adding ticket to aviacompany works and raises."""
    sut = ta.create_test_aviacompany()
    new_ticket = ta.T_TICKETS[0]
    want_new_tickets = sut.tickets + list(ta.T_TICKETS[:1])
    sut.add_ticket(new_ticket)
    assert sut.tickets == want_new_tickets

    with pytest.raises(TypeError):
        sut.add_ticket('ticket')


def test_delete_ticket():
    """Asserts that deleting a ticket works."""
    sut = ta.create_test_aviacompany()
    sut.delete_ticket(ta.T_TICKETS[0])
    assert sut.tickets == list(ta.T_TICKETS[1:])

    with pytest.raises(ValueError):
        sut.delete_ticket(Ticket('123', Passenger('Alice', '444444'), Flight('4', 'W', 'Z')))
