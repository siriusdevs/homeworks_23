"""Module with tests for hw3.aviacompany."""

import pytest

from ..aviacompany import Aviacompany
from ..flight import Flight
from ..passenger import Passenger
from ..ticket import Ticket

T_FLIGHTS = (Flight('1', 'A', 'B'), Flight('2', 'C', 'D'))
T_PASSENGERS = (Passenger('Alice', '123456'), Passenger('Bob', '555555'))
T_TICKETS = (
    Ticket('123', T_PASSENGERS[0], T_FLIGHTS[0]),
    Ticket('321', T_PASSENGERS[1], T_FLIGHTS[1]),
)


def create_test_aviacompany() -> Aviacompany:
    """Create a test aviacompany.

    Returns:
        Aviacompany: aviacompany with test data
    """
    return Aviacompany('Fly Emirates', list(T_FLIGHTS), list(T_PASSENGERS), list(T_TICKETS))


def test_aviacompany_getters_happy():
    """Creates an aviacompany and asserts on its getters."""
    sut = Aviacompany('Aeroflot', list(T_FLIGHTS), list(T_PASSENGERS), list(T_TICKETS))
    assert sut.name == 'Aeroflot'
    assert sut.flights == list(T_FLIGHTS)
    assert sut.passengers == list(T_PASSENGERS)
    assert sut.tickets == list(T_TICKETS)


def test_aviacompany_setters_happy():
    """Uses aviacompany's setters and asserts they truly modify properties."""
    sut = create_test_aviacompany()
    sut.name = 'S7 Airlines'
    sut.flights = list(reversed(T_FLIGHTS))
    sut.passengers = list(reversed(T_PASSENGERS))
    sut.tickets = list(reversed(T_TICKETS))
    assert sut.name == 'S7 Airlines'
    assert sut.flights == list(reversed(T_FLIGHTS))
    assert sut.passengers == list(reversed(T_PASSENGERS))
    assert sut.tickets == list(reversed(T_TICKETS))


def test_aviacompany_setters_errors():
    """Asserts that aviacompany constructors raise errors on inappriate types."""
    sut = create_test_aviacompany()

    with pytest.raises(TypeError):
        sut.name = 1234
    with pytest.raises(TypeError):
        sut.tickets = Passenger('Bob', '123456')
    with pytest.raises(TypeError):
        sut.flights = 'hello'
    with pytest.raises(TypeError):
        sut.passengers = 42.0


def test_aviacompany_list_setters_errors():
    """Asserts that aviacompany constructors raise errors on inappriate types inside lists."""
    sut = create_test_aviacompany()

    with pytest.raises(TypeError):
        sut.flights = list(T_FLIGHTS[:1]) + [55]
    with pytest.raises(TypeError):
        sut.passengers = ['hello'] + list(T_PASSENGERS[:1])
    with pytest.raises(TypeError):
        sut.tickets = [Flight('5', 'A', 'B')] + list(T_TICKETS[:1])
