"""Module for testing Passenger class."""


import pytest
from hw3_exceptions import VariableHasInvalidWriteFormat as Format_error
from passenger import Passenger

valid_test_data_for_getter = (
    (Passenger('Danilov Ilya Alekseevich', 1234567890), ('Danilov Ilya Alekseevich', 1234567890)),
    (Passenger('Romodanov Denis Denisovich', 1122334455), ('Romodanov Denis Denisovich', 1122334455)),
)

invalid_test_data_for_getter = (
    ((123, 1234567890), TypeError),
    (('Danilov Ilya Alekseevich', '1122334455'), TypeError),

    (('123', 1234567890), Format_error),
    (('abc', 1234567890), Format_error),
    (('Abc', 1234567890), Format_error),
    (('Abc Def', 1234567890), Format_error),
    (('A B  C', 1234567890), Format_error),

    (('Danilov Ilya Alekseevich', 123), Format_error),
    (('Danilov Ilya Alekseevich', -123456789), Format_error),
)

valid_test_data_for_setter = (
    (Passenger('Danilov Ilya Alekseevich', 1234567890), (0, 'Romodanov Denis Denisovich'), Passenger('Romodanov Denis Denisovich', 1234567890)),
    (Passenger('Romodanov Denis Denisovich', 1122334455), (1, 1234567890), Passenger('Romodanov Denis Denisovich', 1234567890)),
)

invalid_test_data_for_setter = (
    (Passenger('Danilov Ilya Alekseevich', 1234567890), (0, 123), TypeError),
    (Passenger('Danilov Ilya Alekseevich', 1234567890), (1, '1122334455'), TypeError),

    (Passenger('Danilov Ilya Alekseevich', 1234567890), (0, '123'), Format_error),
    (Passenger('Danilov Ilya Alekseevich', 1234567890), (0, 'abc'), Format_error),
    (Passenger('Danilov Ilya Alekseevich', 1234567890), (0, 'Abc'), Format_error),
    (Passenger('Danilov Ilya Alekseevich', 1234567890), (0, 'Abc Def'), Format_error),
    (Passenger('Danilov Ilya Alekseevich', 1234567890), (0, 'A B  C'), Format_error),

    (Passenger('Danilov Ilya Alekseevich', 1234567890), (1, 123), Format_error),
    (Passenger('Danilov Ilya Alekseevich', 1234567890), (1, -123456789), Format_error),
)


@pytest.mark.parametrize('passenger, expected', valid_test_data_for_getter)
def test_valid_test_data_for_getter(passenger: Passenger, expected: tuple):
    """Test the Passenger class getter with the valid test data.

    Args:
        passenger (Passenger): passenger with the passenger name and passport number.
        expected (tuple): expected data.
    """
    passenger_name, passport_number = expected
    assert passenger.passenger_name == passenger_name
    assert passenger.passport_number == passport_number


def test_invalid_test_data_for_getter():
    """Test the Passenger class getter with the invalid test data."""
    for passenger_data, error in invalid_test_data_for_getter:
        with pytest.raises(error):
            Passenger(*passenger_data)


@pytest.mark.parametrize('passenger, set_data, expected', valid_test_data_for_setter)
def test_valid_test_data_for_setter(passenger: Passenger, set_data: tuple, expected: tuple):
    """Test the Passenger class setter with the valid test data.

    Args:
        passenger (Passenger): passenger with the passenger name and passport number.
        set_data (tuple): set data.
        expected (tuple): expected data.
    """
    passenger_property_index, passenger_property = set_data
    passenger_propertis_names = list(passenger.__dict__.keys())
    if passenger_propertis_names[passenger_property_index] == '_passenger_name':
        passenger.passenger_name = passenger_property
    if passenger_propertis_names[passenger_property_index] == '_passport_number':
        passenger.passport_number = passenger_property
    assert passenger.__dict__ == expected.__dict__


def test_invalid_test_data_for_setter():
    """Test the Passenger class setter with the invalid test data."""
    for passenger, set_data, error in invalid_test_data_for_setter:
        passenger_property_index, passenger_property = set_data
        passenger_propertis_names = list(passenger.__dict__.keys())
        if passenger_propertis_names[passenger_property_index] == '_passenger_name':
            with pytest.raises(error):
                passenger.passenger_name = passenger_property
        if passenger_propertis_names[passenger_property_index] == '_passport_number':
            with pytest.raises(error):
                passenger.passport_number = passenger_property
