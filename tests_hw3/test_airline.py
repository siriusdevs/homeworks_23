"""Module for testing HW3 classes."""


import pytest

from ..hw3 import Passenger, Flight, Ticket, Airline

PASSENGER_DEFAULT = Passenger('Alexey', '123456')
FLIGHT_DEFAULT = Flight('AB1234', 'Moscow', 'Ekaterinburg')
TICKET_DEFAULT = Ticket(FLIGHT_DEFAULT, PASSENGER_DEFAULT, 'ID0001')
AIRLINE_DEFAULT = Airline('SpaceX', [FLIGHT_DEFAULT], [PASSENGER_DEFAULT], [TICKET_DEFAULT])

PASSENGER_TWO = Passenger('Boris', '987654')
FLIGHT_TWO = Flight('CD5678', 'Sochi', 'Irkutsk')
TICKET_TWO = Ticket(FLIGHT_TWO, PASSENGER_TWO, 'ID0002')
AIRLINE_TWO = Airline('CosmosY', [FLIGHT_TWO], [PASSENGER_TWO], [TICKET_TWO])


def test_airline_valid_getter():
    """Create airline with valid values. Check getters."""
    airline = AIRLINE_DEFAULT
    assert airline.title == 'SpaceX'
    assert airline.flights == [FLIGHT_DEFAULT]
    assert airline.passengers == [PASSENGER_DEFAULT]
    assert airline.tickets == [TICKET_DEFAULT]


def test_airline_valid_setter():
    """Change ticket values. Check setters."""
    airline = AIRLINE_DEFAULT
    airline.title = 'CosmosY'
    airline.flights = [FLIGHT_TWO]
    airline.passengers = [PASSENGER_TWO]
    airline.tickets = [TICKET_TWO]
    assert airline.title == 'CosmosY'
    assert airline.flights == [FLIGHT_TWO]
    assert airline.passengers == [PASSENGER_TWO]
    assert airline.tickets == [TICKET_TWO]


def test_airline_getter_errors():
    """Create airline with invalid values. Check getter errors."""
    with pytest.raises(TypeError):
        Airline(123, [FLIGHT_DEFAULT], [PASSENGER_DEFAULT], [TICKET_DEFAULT])
    with pytest.raises(TypeError):
        Airline('SpaceX', 'NotFlight', [PASSENGER_DEFAULT], [TICKET_DEFAULT])
    with pytest.raises(TypeError):
        Airline('SpaceX', [FLIGHT_DEFAULT], 'NotPassenger', [TICKET_DEFAULT])
    with pytest.raises(TypeError):
        Airline('SpaceX', [FLIGHT_DEFAULT], [PASSENGER_DEFAULT], 'NotTicket')


def test_airline_setter_errors():
    """Change ticket values to invalid ones. Check setter errors."""
    airline = AIRLINE_DEFAULT
    with pytest.raises(TypeError):
        airline.title = ['TitleAbsolutely']
    with pytest.raises(TypeError):
        airline.flights = 'FlightForReal'
    with pytest.raises(TypeError):
        airline.passengers = ['hiiii', 'we are passengers!!']
    with pytest.raises(TypeError):
        airline.tickets = [TICKET_DEFAULT, TICKET_TWO, 'TICKET_THREE']
