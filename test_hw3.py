"""Testing HW3 classes."""


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


def test_passenger_valid():
    """Create passenger with valid values. Check getters and setters."""
    passenger = PASSENGER_DEFAULT
    assert passenger.name == 'Alexey'
    assert passenger.passport_id == '123456'
    passenger.name = 'Boris'
    passenger.passport_id = '987654'
    assert passenger.name == 'Boris'
    assert passenger.passport_id == '987654'
    

def test_passenger_errors():
    """Create passenger with invalid values. Check value and type errors."""
    with pytest.raises(TypeError):
        Passenger(413737, '123456')
    with pytest.raises(TypeError):
        Passenger('Alexey', 123456)
    with pytest.raises(ValueError):
        Passenger('Alexey', '123')
    with pytest.raises(ValueError):
        Passenger('Alexey', 'ID1234')

    passenger = PASSENGER_DEFAULT
    with pytest.raises(TypeError):
        passenger.name = 413737
    with pytest.raises(TypeError):
        passenger.passport_id = 123456
    with pytest.raises(ValueError):
        passenger.passport_id = '123'
    with pytest.raises(ValueError):
        passenger.passport_id = 'ID1234'


def test_flight_valid():
    """Create flight with valid values. Check getters and setters."""
    flight = FLIGHT_DEFAULT
    assert flight.flight_id == 'AB1234'
    assert flight.from_airport == 'Moscow'
    assert flight.to_airport == 'Ekaterinburg'

    flight.flight_id = 'CD5678'
    flight.from_airport = 'Sochi'
    flight.to_airport = 'Irkutsk'
    assert flight.flight_id == 'CD5678'
    assert flight.from_airport == 'Sochi'
    assert flight.to_airport == 'Irkutsk'


def test_flight_errors():
    """Create flight with invalid values. Check type errors."""
    with pytest.raises(TypeError):
        Flight(1234, 'Moscow', 'Ekaterinburg')
    with pytest.raises(TypeError):
        Flight('AB1234', 123, 'Ekaterinburg')
    with pytest.raises(TypeError):
        Flight('AB1234', 'Moscow', 123)

    flight = FLIGHT_DEFAULT
    with pytest.raises(TypeError):
        flight.flight_id = 1234
    with pytest.raises(TypeError):
        flight.from_airport = 123
    with pytest.raises(TypeError):
        flight.to_airport = 123


def test_ticket_valid():
    """Create ticket with valid values. Check getters and setters."""
    ticket = TICKET_DEFAULT
    assert ticket.flight == FLIGHT_DEFAULT
    assert ticket.passenger == PASSENGER_DEFAULT
    assert ticket.ticket_id == 'ID0001'

    ticket.flight = FLIGHT_TWO
    ticket.passenger = PASSENGER_TWO
    ticket.ticket_id = 'ID0002'
    assert ticket.flight == FLIGHT_TWO
    assert ticket.passenger == PASSENGER_TWO
    assert ticket.ticket_id == 'ID0002'


def test_ticket_errors():
    """Create ticket with invalid values. Check value and type errors."""
    with pytest.raises(TypeError):
        Ticket('NotFlight', PASSENGER_DEFAULT, 'ID0001')
    with pytest.raises(TypeError):
        Ticket(FLIGHT_DEFAULT, 'NotPassenger', 'ID0001')
    with pytest.raises(TypeError):
        Ticket(FLIGHT_DEFAULT, PASSENGER_DEFAULT, 1001)

    ticket = TICKET_DEFAULT
    with pytest.raises(TypeError):
        ticket.flight = 'FlightForReal'
    with pytest.raises(TypeError):
        ticket.passenger = FLIGHT_DEFAULT
    with pytest.raises(TypeError):
        ticket.ticket_id = ['hiii i am id']


def test_airline_valid():
    """Create airline with valid values. Check getters and setters."""
    airline = AIRLINE_DEFAULT
    assert airline.title == 'SpaceX'
    assert airline.flights == list(FLIGHT_DEFAULT)
    assert airline.passengers == list(PASSENGER_DEFAULT)
    assert airline.tickets == list(TICKET_DEFAULT)

    airline.title = 'CosmosY'
    airline.flights = list(FLIGHT_TWO)
    airline.passengers = list(PASSENGER_TWO)
    airline.tickets = list(TICKET_TWO)
    assert airline.title == 'CosmosY'
    assert airline.flights == list(FLIGHT_TWO)
    assert airline.passengers == list(PASSENGER_TWO)
    assert airline.tickets == list(TICKET_TWO)


def test_airline_errors():
    """Create airline with invalid values. Check getters and setters."""
    with pytest.raises(TypeError):
        Airline(123, [FLIGHT_DEFAULT], [PASSENGER_DEFAULT], [TICKET_DEFAULT])
    with pytest.raises(TypeError):
        Airline('SpaceX', 'NotFlight', [PASSENGER_DEFAULT], [TICKET_DEFAULT])
    with pytest.raises(TypeError):
        Airline('SpaceX', [FLIGHT_DEFAULT], 'NotPassenger', [TICKET_DEFAULT])
    with pytest.raises(TypeError):
        Airline('SpaceX', [FLIGHT_DEFAULT], [PASSENGER_DEFAULT], 'NotTicket')

    airline = AIRLINE_DEFAULT
    with pytest.raises(TypeError):
        airline.title = ['TitleAbsolutely']
    with pytest.raises(TypeError):
        airline.flights = 'FlightForReal'
    with pytest.raises(TypeError):
        airline.passengers = ['hiiii', 'we are passengers!!']
    with pytest.raises(TypeError):
        airline.tickets = [TICKET_DEFAULT, TICKET_TWO, 'TICKET_THREE']


def test_add_flight():
    """Check that adding a new flight works."""
    airline = AIRLINE_DEFAULT
    airline.add_flight(FLIGHT_TWO)
    assert airline.flights == [FLIGHT_DEFAULT, FLIGHT_TWO]

    with pytest.raises(TypeError):
        airline.add_flight('NotFlight')


def test_remove_flight():
    """Check that removing a flight works."""
    airline = AIRLINE_DEFAULT
    airline.remove_flight(FLIGHT_DEFAULT)
    assert airline.flights == []

    with pytest.raises(ValueError):
        airline.remove_flight(FLIGHT_TWO)


def test_add_passenger():
    """Check that adding a new passenger works."""
    airline = AIRLINE_DEFAULT
    airline.add_passenger(PASSENGER_TWO)
    assert airline.passengers == [PASSENGER_DEFAULT, PASSENGER_TWO]

    with pytest.raises(TypeError):
        airline.add_passenger('NotPassenger')


def test_remove_passenger():
    """Check that removing a passenger works."""
    airline = AIRLINE_DEFAULT
    airline.remove_passenger(PASSENGER_DEFAULT)
    assert airline.passengers == []

    with pytest.raises(ValueError):
        airline.remove_passenger(FLIGHT_TWO)


def test_buy_ticket():
    """Check that buying (adding) a new ticket works."""
    airline = AIRLINE_DEFAULT
    airline.buy_ticket(TICKET_TWO)
    assert airline.tickets == [TICKET_DEFAULT, TICKET_TWO]

    with pytest.raises(TypeError):
        airline.buy_ticket('NotTicket')


def test_cancel_ticket():
    """Check that cancelling (removing) a ticket works."""
    airline = AIRLINE_DEFAULT
    airline.cancel_ticket(TICKET_DEFAULT)
    assert airline.passengers == []

    with pytest.raises(ValueError):
        airline.cancel_ticket(TICKET_TWO)