"""Module for testing Airline class."""


import pytest
import valid_test_data as vtd
from airline import Airline
from hw3_exceptions import VariableHasInvalidWriteFormat as Format_error

valid_test_data_for_getter = (
    (
        Airline('Aeroflot', vtd.valid_flights_list[0], vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]),
        ('Aeroflot', vtd.valid_flights_list[0], vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]),
    ),
    (
        Airline('Ural Airlines', vtd.valid_flights_list[1], vtd.valid_passengers_list[1], vtd.valid_tickets_list[1]),
        ('Ural Airlines', vtd.valid_flights_list[1], vtd.valid_passengers_list[1], vtd.valid_tickets_list[1]),
    ),
)

invalid_test_data_for_getter = (
    ((123, vtd.valid_flights_list[0], vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]), TypeError),
    (('Aeroflot', 'flights', vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]), TypeError),
    (('Aeroflot', vtd.valid_flights_list[0], 'passengers', vtd.valid_tickets_list[0]), TypeError),
    (('Aeroflot', vtd.valid_flights_list[0], vtd.valid_passengers_list[0], 'tickets'), TypeError),

    (('Ural  Airlines', vtd.valid_flights_list[0], vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]), Format_error),
    (('___', vtd.valid_flights_list[0], vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]), Format_error),
)

valid_test_data_for_setter = (
    (
        Airline('Aeroflot', vtd.valid_flights_list[0], vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]),
        (0, 'Ural Airlines'),
        Airline('Ural Airlines', vtd.valid_flights_list[0], vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]),
    ),
    (
        Airline('Aeroflot', vtd.valid_flights_list[0], vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]),
        (1, vtd.valid_flights_list[1]),
        Airline('Aeroflot', vtd.valid_flights_list[1], vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]),
    ),
    (
        Airline('Aeroflot', vtd.valid_flights_list[0], vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]),
        (2, vtd.valid_passengers_list[1]),
        Airline('Aeroflot', vtd.valid_flights_list[0], vtd.valid_passengers_list[1], vtd.valid_tickets_list[0]),
    ),
    (
        Airline('Aeroflot', vtd.valid_flights_list[0], vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]),
        (3, vtd.valid_tickets_list[1]),
        Airline('Aeroflot', vtd.valid_flights_list[0], vtd.valid_passengers_list[0], vtd.valid_tickets_list[1]),
    ),
)

invalid_test_data_for_setter = (
    (
        Airline('Aeroflot', vtd.valid_flights_list[0], vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]),
        (0, 123),
        TypeError,
    ),
    (
        Airline('Aeroflot', vtd.valid_flights_list[0], vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]),
        (1, 'flights'),
        TypeError,
    ),
    (
        Airline('Aeroflot', vtd.valid_flights_list[0], vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]),
        (2, 'passengers'),
        TypeError,
    ),
    (
        Airline('Aeroflot', vtd.valid_flights_list[0], vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]),
        (3, 'tickets'),
        TypeError,
    ),

    (
        Airline('Aeroflot', vtd.valid_flights_list[0], vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]),
        (0, 'Ural  Airlines'),
        Format_error,
    ),
    (
        Airline('Aeroflot', vtd.valid_flights_list[0], vtd.valid_passengers_list[0], vtd.valid_tickets_list[0]),
        (0, '___'),
        Format_error,
    ),
)


@pytest.mark.parametrize('airline, expected', valid_test_data_for_getter)
def test_valid_test_data_for_getter(airline: Airline, expected: tuple):
    """Test the Airline class getter with the valid test data.

    Args:
        airline (Airline): airline containing the airline name, \
        flights, passengers and tickets.
        expected (tuple): expected data.
    """
    airline_name, flights, passengers, tickets = expected
    assert airline.airline_name == airline_name
    assert airline.flights == flights
    assert airline.passengers == passengers
    assert airline.tickets == tickets


def test_invalid_test_data_for_getter():
    """Test the Airline class getter with the invalid test data."""
    for airline_data, error in invalid_test_data_for_getter:
        with pytest.raises(error):
            Airline(*airline_data)


@pytest.mark.parametrize('airline, set_data, expected', valid_test_data_for_setter)
def test_valid_test_data_for_setter(airline: Airline, set_data: tuple, expected: tuple):
    """Test the Airline class setter with the valid test data.

    Args:
        airline (Airline): airline containing the airline name, \
        flights, passengers and tickets.
        set_data (tuple): set data.
        expected (tuple): expected data.
    """
    airline_property_index, airline_property = set_data
    airline_propertis_names = list(airline.__dict__.keys())
    if airline_propertis_names[airline_property_index] == '_airline_name':
        airline.airline_name = airline_property
    if airline_propertis_names[airline_property_index] == '_flights':
        airline.flights = airline_property
    if airline_propertis_names[airline_property_index] == '_passengers':
        airline.passengers = airline_property
    if airline_propertis_names[airline_property_index] == '_tickets':
        airline.tickets = airline_property
    assert airline.__dict__ == expected.__dict__


def test_invalid_test_data_for_setter():
    """Test the Airline class setter with the invalid test data."""
    for airline, set_data, error in invalid_test_data_for_setter:
        airline_property_index, airline_property = set_data
        airline_propertis_names = list(airline.__dict__.keys())
        if airline_propertis_names[airline_property_index] == '_airline_name':
            with pytest.raises(error):
                airline.airline_name = airline_property
        if airline_propertis_names[airline_property_index] == '_flights':
            with pytest.raises(error):
                airline.flights = airline_property
        if airline_propertis_names[airline_property_index] == '_passengers':
            with pytest.raises(error):
                airline.passengers = airline_property
        if airline_propertis_names[airline_property_index] == '_tickets':
            with pytest.raises(error):
                airline.tickets = airline_property
