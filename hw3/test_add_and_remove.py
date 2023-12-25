"""Module for testing HW3 classes."""


import pytest

from hw3 import Passenger, Flight, Ticket, Airline

PASSENGER_DEFAULT = Passenger('Alexey', '123456')
FLIGHT_DEFAULT = Flight('AB1234', 'Moscow', 'Ekaterinburg')
TICKET_DEFAULT = Ticket(FLIGHT_DEFAULT, PASSENGER_DEFAULT, 'ID0001')
AIRLINE_DEFAULT = Airline('SpaceX', [FLIGHT_DEFAULT], [PASSENGER_DEFAULT], [TICKET_DEFAULT])

PASSENGER_TWO = Passenger('Boris', '987654')
FLIGHT_TWO = Flight('CD5678', 'Sochi', 'Irkutsk')
TICKET_TWO = Ticket(FLIGHT_TWO, PASSENGER_TWO, 'ID0002')
AIRLINE_TWO = Airline('CosmosY', [FLIGHT_TWO], [PASSENGER_TWO], [TICKET_TWO])


def test_add_passenger():
    """Check that adding a new passenger works."""
    airline = AIRLINE_DEFAULT
    airline.passengers = [PASSENGER_DEFAULT]
    airline.add_passenger(PASSENGER_TWO)
    assert airline.passengers == [PASSENGER_DEFAULT, PASSENGER_TWO]

    with pytest.raises(TypeError):
        airline.add_passenger('NotPassenger')


def test_remove_passenger():
    """Check that removing a passenger works."""
    airline = AIRLINE_DEFAULT
    airline.passengers = [PASSENGER_DEFAULT, PASSENGER_TWO]
    airline.remove_passenger(PASSENGER_DEFAULT)
    assert airline.passengers == [PASSENGER_TWO]

    with pytest.raises(ValueError):
        airline.remove_passenger(PASSENGER_DEFAULT)


def test_buy_ticket():
    """Check that buying (adding) a new ticket works."""
    airline = AIRLINE_DEFAULT
    airline.tickets = [TICKET_DEFAULT]
    airline.buy_ticket(TICKET_TWO)
    assert airline.tickets == [TICKET_DEFAULT, TICKET_TWO]

    with pytest.raises(TypeError):
        airline.buy_ticket('NotTicket')


def test_cancel_ticket():
    """Check that cancelling (removing) a ticket works."""
    airline = AIRLINE_DEFAULT
    airline.tickets = [TICKET_DEFAULT, TICKET_TWO]
    airline.cancel_ticket(TICKET_DEFAULT)
    assert airline.tickets == [TICKET_TWO]

    with pytest.raises(ValueError):
        airline.cancel_ticket(TICKET_DEFAULT)
