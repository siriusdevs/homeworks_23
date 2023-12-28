"""Module for testing Flight class."""


import pytest
from flight import Flight
from hw3_exceptions import VariableHasInvalidWriteFormat as Format_error

valid_test_data_for_getter = (
    (Flight('AB1', 'Sochi', 'Samara'), ('AB1', 'Sochi', 'Samara')),
    (Flight('CD23', 'Samara', 'Orenburg'), ('CD23', 'Samara', 'Orenburg')),
    (Flight('EF456', 'Orenburg', 'Moskov'), ('EF456', 'Orenburg', 'Moskov')),
    (Flight('GH7890', 'Moskov', 'Sochi'), ('GH7890', 'Moskov', 'Sochi')),

    (Flight('AB 1', 'Sochi', 'Samara'), ('AB 1', 'Sochi', 'Samara')),
    (Flight('CD 23', 'Samara', 'Orenburg'), ('CD 23', 'Samara', 'Orenburg')),
    (Flight('EF 456', 'Orenburg', 'Moskov'), ('EF 456', 'Orenburg', 'Moskov')),
    (Flight('GH 7890', 'Moskov', 'Sochi'), ('GH 7890', 'Moskov', 'Sochi')),
)

invalid_test_data_for_getter = (
    ((123, 'Sochi', 'Samara'), TypeError),
    (('CD23', ['Samara'], 'Orenburg'), TypeError),
    (('EF456', 'Orenburg', (123)), TypeError),

    (('123', 'Sochi', 'Samara'), Format_error),
    (('CD', 'Samara', 'Orenburg'), Format_error),
    (('EF  456', 'Orenburg', 'Moskov'), Format_error),
    (('GH0', 'Moskov', 'Sochi'), Format_error),

    (('AB1', 'sochi', 'Samara'), Format_error),
    (('CD23', 'Samara123', 'Orenburg'), Format_error),
    (('EF456', 'Orenburg abc', 'Moskov'), Format_error),
    (('GH7890', ' Moskov ', 'Sochi'), Format_error),

    (('AB1', 'Sochi', 'samara'), Format_error),
    (('CD23', 'Samara', 'Orenburg123'), Format_error),
    (('EF456', 'Orenburg', 'Moskov abc'), Format_error),
    (('GH7890', 'Moskov', ' Sochi '), Format_error),
)

valid_test_data_for_setter = (
    (Flight('AB1', 'Sochi', 'Samara'), (0, 'AB 1'), Flight('AB 1', 'Sochi', 'Samara')),
    (Flight('CD 23', 'Samara', 'Orenburg'), (0, 'CD23'), Flight('CD23', 'Samara', 'Orenburg')),
    (Flight('EF456', 'Orenburg', 'Moskov'), (0, 'GH7890'), Flight('GH7890', 'Orenburg', 'Moskov')),
    (Flight('GH 7890', 'Moskov', 'Sochi'), (0, 'AB 1'), Flight('AB 1', 'Moskov', 'Sochi')),

    (Flight('AB1', 'Sochi', 'Samara'), (1, 'Orenburg'), Flight('AB1', 'Orenburg', 'Samara')),

    (Flight('AB1', 'Sochi', 'Samara'), (2, 'Moskov'), Flight('AB1', 'Sochi', 'Moskov')),
)

invalid_test_data_for_setter = (
    (Flight('AB1', 'Sochi', 'Samara'), (0, 123), TypeError),
    (Flight('CD23', 'Samara', 'Orenburg'), (1, ['Samara']), TypeError),
    (Flight('EF456', 'Orenburg', 'Moskov'), (2, (123)), TypeError),

    (Flight('AB1', 'Sochi', 'Samara'), (0, '123'), Format_error),
    (Flight('CD23', 'Samara', 'Orenburg'), (0, 'CD'), Format_error),
    (Flight('EF456', 'Orenburg', 'Moskov'), (0, 'EF  456'), Format_error),
    (Flight('GH7890', 'Moskov', 'Sochi'), (0, 'GH0'), Format_error),

    (Flight('AB1', 'Sochi', 'Samara'), (1, 'sochi'), Format_error),
    (Flight('CD23', 'Samara', 'Orenburg'), (1, 'Samara123'), Format_error),
    (Flight('EF456', 'Orenburg', 'Moskov'), (1, 'Orenburg abc'), Format_error),
    (Flight('GH7890', 'Moskov', 'Sochi'), (1, ' Moskov '), Format_error),

    (Flight('AB1', 'Sochi', 'Samara'), (2, 'samara'), Format_error),
    (Flight('CD23', 'Samara', 'Orenburg'), (2, 'Orenburg123'), Format_error),
    (Flight('EF456', 'Orenburg', 'Moskov'), (2, 'Moskov abc'), Format_error),
    (Flight('GH7890', 'Moskov', 'Sochi'), (2, ' Sochi '), Format_error),
)


@pytest.mark.parametrize('flight, expected', valid_test_data_for_getter)
def test_valid_test_data_for_getter(flight: Flight, expected: tuple):
    """Test the Flight class getter with the valid test data.

    Args:
        flight (Flight): flight with flight number passing from the departure airport \
        to the arrival airport.
        expected (tuple): expected data.
    """
    flight_number, departure_airpor, arrival_airport = expected
    assert flight.flight_number == flight_number
    assert flight.departure_airport == departure_airpor
    assert flight.arrival_airport == arrival_airport


def test_invalid_test_data_for_getter():
    """Test the Flight class getter with the invalid test data."""
    for flight_data, error in invalid_test_data_for_getter:
        with pytest.raises(error):
            Flight(*flight_data)


@pytest.mark.parametrize('flight, set_data, expected', valid_test_data_for_setter)
def test_valid_test_data_for_setter(flight: Flight, set_data: tuple, expected: tuple):
    """Test the Flight class setter with the valid test data.

    Args:
        flight (Flight): flight with flight number passing from the departure airport \
        to the arrival airport.
        set_data (tuple): set data.
        expected (tuple): expected data.
    """
    flight_property_index, flight_property = set_data
    flight_propertis_names = list(flight.__dict__.keys())
    if flight_propertis_names[flight_property_index] == '_flight_number':
        flight.flight_number = flight_property
    if flight_propertis_names[flight_property_index] == '_departure_airport':
        flight.departure_airport = flight_property
    if flight_propertis_names[flight_property_index] == '_arrival_airport':
        flight.arrival_airport = flight_property
    assert flight.__dict__ == expected.__dict__


def test_invalid_test_data_for_setter():
    """Test the Flight class setter with the invalid test data."""
    for flight, set_data, error in invalid_test_data_for_setter:
        flight_property_index, flight_property = set_data
        flight_propertis_names = list(flight.__dict__.keys())
        if flight_propertis_names[flight_property_index] == '_flight_number':
            with pytest.raises(error):
                flight.flight_number = flight_property
        if flight_propertis_names[flight_property_index] == '_departure_airport':
            with pytest.raises(error):
                flight.departure_airport = flight_property
        if flight_propertis_names[flight_property_index] == '_arrival_airport':
            with pytest.raises(error):
                flight.arrival_airport = flight_property
