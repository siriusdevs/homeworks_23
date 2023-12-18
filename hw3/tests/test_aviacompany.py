"""Module with tests for hw3.aviacompany."""

import pytest

from ..aviacompany import Aviacompany
from ..flight import Flight
from ..passenger import Passenger
from ..ticket import Ticket

_T_FLIGHTS = (Flight('1', 'A', 'B'), Flight('2', 'C', 'D'))
_T_PASSENGERS = (Passenger('Alice', '123456'), Passenger('Bob', '555555'))
_T_TICKETS = (
    Ticket('123', _T_PASSENGERS[0], _T_FLIGHTS[0]),
    Ticket('321', _T_PASSENGERS[1], _T_FLIGHTS[1]),
)

def _create_test_aviacompany() -> Aviacompany:
    return Aviacompany('Fly Emirates', list(_T_FLIGHTS), list(_T_PASSENGERS), list(_T_TICKETS))

def test_aviacompany_getters_happy():
    """Creates an aviacompany and asserts on its getters."""
    sut = Aviacompany('Aeroflot', list(_T_FLIGHTS), list(_T_PASSENGERS), list(_T_TICKETS))
    assert sut.name == 'Aeroflot'
    assert sut.flights == list(_T_FLIGHTS)
    assert sut.passengers == list(_T_PASSENGERS)
    assert sut.tickets == list(_T_TICKETS)


def test_aviacompany_setters_happy():
    """Uses aviacompany's setters and asserts they truly modify properties."""
    sut = _create_test_aviacompany()
    sut.name = 'S7 Airlines'
    sut.flights = list(reversed(_T_FLIGHTS))
    sut.passengers = list(reversed(_T_PASSENGERS))
    sut.tickets = list(reversed(_T_TICKETS))
    assert sut.name == 'S7 Airlines'
    assert sut.flights == list(reversed(_T_FLIGHTS))
    assert sut.passengers == list(reversed(_T_PASSENGERS))
    assert sut.tickets == list(reversed(_T_TICKETS))


def test_aviacompany_setters_errors():
    """Asserts that aviacompany constructors raise errors on inappriate types."""
    sut = _create_test_aviacompany()

    with pytest.raises(TypeError):
        sut.name = 1234
    with pytest.raises(TypeError):
        sut.flights = 'hello'
    with pytest.raises(TypeError):
        sut.passengers = 42.0
    with pytest.raises(TypeError):
        sut.tickets = Passenger()


def test_aviacompany_list_setters_errors():
    """Asserts that aviacompany constructors raise errors on inappriate types inside lists."""
    sut = _create_test_aviacompany()

    with pytest.raises(TypeError):
        sut.flights = list(_T_FLIGHTS[:1]) + [55]
    with pytest.raises(TypeError):
        sut.passengers = ['hello'] + list(_T_PASSENGERS[:1])
    with pytest.raises(TypeError):
        sut.tickets = [Flight()] + list(_T_TICKETS[:1])


def test_add_flight_happy():
    """Asserts that adding flight to aviacompany works."""
    sut = _create_test_aviacompany()
    new_flight = _T_FLIGHTS[0]
    want_new_flights = sut.flights + list(_T_FLIGHTS[:1])
    sut.add_flight(new_flight)
    assert sut.flights == want_new_flights


def test_add_flight_error():
    """Asserts that adding flight with incorrect type raises TypeError."""
    sut = _create_test_aviacompany()
    with pytest.raises(TypeError):
        sut.add_flight(123)
