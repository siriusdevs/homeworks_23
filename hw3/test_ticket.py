"""Module for testing HW3 Ticket class."""


import pytest

from hw3 import Passenger, Flight, Ticket

PASSENGER_DEFAULT = Passenger('Alexey', '123456')
FLIGHT_DEFAULT = Flight('AB1234', 'Moscow', 'Ekaterinburg')
TICKET_DEFAULT = Ticket(FLIGHT_DEFAULT, PASSENGER_DEFAULT, 'ID0001')
PASSENGER_TWO = Passenger('Boris', '987654')
FLIGHT_TWO = Flight('CD5678', 'Sochi', 'Irkutsk')
TICKET_TWO = Ticket(FLIGHT_TWO, PASSENGER_TWO, 'ID0002')


def test_ticket_valid_getter():
    """Create ticket with valid values. Check getters."""
    ticket = TICKET_DEFAULT
    assert ticket.flight == FLIGHT_DEFAULT
    assert ticket.passenger == PASSENGER_DEFAULT
    assert ticket.ticket_id == 'ID0001'


def test_ticket_valid_setter():
    """Change ticket values. Check setters."""
    ticket = TICKET_DEFAULT
    ticket.flight = FLIGHT_TWO
    ticket.passenger = PASSENGER_TWO
    ticket.ticket_id = 'ID0002'
    assert ticket.flight == FLIGHT_TWO
    assert ticket.passenger == PASSENGER_TWO
    assert ticket.ticket_id == 'ID0002'


def test_ticket_getter_errors():
    """Create ticket with invalid values. Check getter errors."""
    with pytest.raises(TypeError):
        Ticket('NotFlight', PASSENGER_DEFAULT, 'ID0001')
    with pytest.raises(TypeError):
        Ticket(FLIGHT_DEFAULT, 'NotPassenger', 'ID0001')
    with pytest.raises(TypeError):
        Ticket(FLIGHT_DEFAULT, PASSENGER_DEFAULT, 1001)


def test_ticket_setters_errors():
    """Change ticket values to invalid ones. Check setter errors."""
    ticket = TICKET_DEFAULT
    with pytest.raises(TypeError):
        ticket.flight = 'FlightForReal'
    with pytest.raises(TypeError):
        ticket.passenger = FLIGHT_DEFAULT
    with pytest.raises(TypeError):
        ticket.ticket_id = ['hiii i am id']
