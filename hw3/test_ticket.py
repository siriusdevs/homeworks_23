"""Module for testing Ticket class."""


import pytest
from hw3_exceptions import VariableHasInvalidWriteFormat as Format_error
from ticket import Ticket
from valid_test_data import valid_flights_list, valid_passengers_list

valid_test_data_for_getter = (
    (Ticket(1234567890123, valid_flights_list[0][0], valid_passengers_list[0][0]), (1234567890123, valid_flights_list[0][0], valid_passengers_list[0][0])),
    (Ticket(1122334455667, valid_flights_list[0][1], valid_passengers_list[0][1]), (1122334455667, valid_flights_list[0][1], valid_passengers_list[0][1])),
)

invalid_test_data_for_getter = (
    (('1234567890123', valid_flights_list[0][0], valid_passengers_list[0][0]), TypeError),
    ((1234567890123, 'flight', valid_passengers_list[0][0]), TypeError),
    ((1234567890123, valid_flights_list[0][0], 'passenger'), TypeError),

    ((123, valid_flights_list[0], valid_passengers_list[0]), Format_error),
    ((-123456789012, valid_flights_list[0][0], valid_passengers_list[0][0]), Format_error),
)


valid_test_data_for_setter = (
    (Ticket(1234567890123, valid_flights_list[0][0], valid_passengers_list[0][0]), (0, 1122334455667), Ticket(1122334455667, valid_flights_list[0][0], valid_passengers_list[0][0])),
    (Ticket(1234567890123, valid_flights_list[0][0], valid_passengers_list[0][0]), (1, valid_flights_list[0][1]), Ticket(1234567890123, valid_flights_list[0][1], valid_passengers_list[0][0])),
    (Ticket(1234567890123, valid_flights_list[0][0], valid_passengers_list[0][0]), (2, valid_passengers_list[0][1]), Ticket(1234567890123, valid_flights_list[0][0], valid_passengers_list[0][1])),
)

invalid_test_data_for_setter = (
    (Ticket(1234567890123, valid_flights_list[0][0], valid_passengers_list[0][0]), (0, '1234567890123'), TypeError),
    (Ticket(1234567890123, valid_flights_list[0][0], valid_passengers_list[0][0]), (1, 'flight'), TypeError),
    (Ticket(1234567890123, valid_flights_list[0][0], valid_passengers_list[0][0]), (2, 'passenger'), TypeError),

    (Ticket(1234567890123, valid_flights_list[0][0], valid_passengers_list[0][0]), (0, 123), Format_error),
    (Ticket(1234567890123, valid_flights_list[0][0], valid_passengers_list[0][0]), (0, -123456789012), Format_error),
)


@pytest.mark.parametrize('ticket, expected', valid_test_data_for_getter)
def test_valid_test_data_for_getter(ticket: Ticket, expected: tuple):
    """Test the Ticket class getter with the valid test data.

    Args:
        ticket (Ticket): ticket with ticket name, flight and passenger.
        expected (tuple): expected data.
    """
    ticket_number, flight, passenger = expected
    assert ticket.ticket_number == ticket_number
    assert ticket.flight == flight
    assert ticket.passenger == passenger


def test_invalid_test_data_for_getter():
    """Test the Ticket class getter with the invalid test data."""
    for ticket_data, error in invalid_test_data_for_getter:
        with pytest.raises(error):
            Ticket(*ticket_data)


@pytest.mark.parametrize('ticket, set_data, expected', valid_test_data_for_setter)
def test_valid_test_data_for_setter(ticket: Ticket, set_data: tuple, expected: tuple):
    """Test the Ticket class setter with the valid test data.

    Args:
        ticket (Ticket): ticket with ticket name, flight and passenger.
        set_data (tuple): set data.
        expected (tuple): expected data.
    """
    ticket_property_index, ticket_property = set_data
    ticket_propertis_names = list(ticket.__dict__.keys())
    if ticket_propertis_names[ticket_property_index] == '_ticket_number':
        ticket.ticket_number = ticket_property
    if ticket_propertis_names[ticket_property_index] == '_flight':
        ticket.flight = ticket_property
    if ticket_propertis_names[ticket_property_index] == '_passenger':
        ticket.passenger = ticket_property
    assert ticket.__dict__ == expected.__dict__


def test_invalid_test_data_for_setter():
    """Test the Ticket class setter with the invalid test data."""
    for ticket, set_data, error in invalid_test_data_for_setter:
        ticket_property_index, ticket_property = set_data
        ticket_propertis_names = list(ticket.__dict__.keys())
        if ticket_propertis_names[ticket_property_index] == '_ticket_number':
            with pytest.raises(error):
                ticket.ticket_number = ticket_property
        if ticket_propertis_names[ticket_property_index] == '_flight':
            with pytest.raises(error):
                ticket.flight = ticket_property
        if ticket_propertis_names[ticket_property_index] == '_passenger':
            with pytest.raises(error):
                ticket.passenger = ticket_property
