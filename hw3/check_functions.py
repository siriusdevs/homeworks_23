"""Module with check functions."""

from typing import Any, Type

import hw3_exceptions as exceptions

LEN_TICKET_NUMBER = 13
LEN_PASSPORT_NUMBER = 10


def check_type(var_name: str, var_value: Any, expected_var_type: Type) -> None:
    """Check the validly of the variable type.

    Args:
        var_name (str): name of the variable.
        var_value (Any): value of the variable.
        expected_var_type (Type): expected type of the variable.

    Raises:
        TypeError: if the var_value is not a expected_var_type instance.
    """
    if not isinstance(var_value, expected_var_type):
        expected_var_type = expected_var_type.__name__
        var_type = type(var_value).__name__
        raise TypeError(f'The {var_name} should be {expected_var_type}, not {var_type}')


def check_element_presence_in_elements(
    element_name: str,
    element_value: Any,
    elements_name: str,
    elements_values: list[Any],
) -> None:
    """Check the list of the elements for the presence of an element.

    Args:
        element_name (str): name of the element.
        element_value (Any): value of the element
        elements_name (str): name of the list of elements.
        elements_values (list[Any]): values of the list of elements.

    Raises:
        ValueError: if element_name not found in elements_name.
    """
    if element_value not in elements_values:
        raise ValueError(f'The {element_name} not found in {elements_name}')


def check_flight_number(flight_number: str) -> None:
    """Check the validly of the flight number.

    Args:
        flight_number (str): number of the flight.

    Raises:
        VariableHasInvalidWriteFormat: if flight_number has an invalid write format.
    """
    check_type('flight_number', flight_number, str)
    if flight_number.count(' ') == 1 and flight_number[2] == ' ':
        flight_number = flight_number.replace(' ', '')
    letters, numbers = flight_number[:2], flight_number[2:]
    is_letters = letters.isalpha() and letters.isupper()
    is_numbers = numbers.isdigit() and (len(numbers) <= 4 and not numbers.startswith('0'))
    if not (is_letters and is_numbers):
        raise exceptions.VariableHasInvalidWriteFormat('flight_number', flight_number)


def check_airport_name(airport_name: str) -> None:
    """Check the validly of the airport name.

    Args:
        airport_name (str): name of the airport.

    Raises:
        VariableHasInvalidWriteFormat: if airport_name has an invalid write format.
    """
    check_type('airport_name', airport_name, str)
    is_letters = airport_name.replace(' ', '').isalpha() and airport_name.istitle()
    is_words = len(airport_name.strip().split()) == airport_name.count(' ') + 1
    if not (is_letters and is_words):
        raise exceptions.VariableHasInvalidWriteFormat('airport_name', airport_name)


def check_passenger_name(passenger_name: str) -> None:
    """Check the validly of the passenger name.

    Args:
        passenger_name (str): name of the passenger.

    Raises:
        VariableHasInvalidWriteFormat: if passenger_name has an invalid write format.
    """
    check_type('passenger_name', passenger_name, str)
    words = passenger_name.strip().split(' ')
    is_letters = passenger_name.replace(' ', '').isalpha() and passenger_name.istitle()
    is_words = len(words) == 3 and passenger_name.count(' ') == 2
    is_names = []
    for word in words:
        if word[1:]:
            is_names.append(word[1:].islower())
    is_names = all(is_names) if is_names else True
    if not (is_letters and is_words and is_names):
        raise exceptions.VariableHasInvalidWriteFormat('passenger_name', passenger_name)


def check_passport_number(passport_number: int) -> None:
    """Check the validly of the passport number.

    Args:
        passport_number (int): number of the passport.

    Raises:
        VariableHasInvalidWriteFormat: if passport_number has an invalid write format.
    """
    check_type('passport_number', passport_number, int)
    len_passport_number = len(str(passport_number)) == LEN_PASSPORT_NUMBER
    is_positive = passport_number > 0
    if not (len_passport_number and is_positive):
        raise exceptions.VariableHasInvalidWriteFormat('passport_number', passport_number)


def check_ticket_number(ticket_number: int) -> None:
    """Check the validly of the ticket number.

    Args:
        ticket_number (int): number of the ticket.

    Raises:
        VariableHasInvalidWriteFormat: if ticket_number has an invalid write format.
    """
    check_type('ticket_number', ticket_number, int)
    len_ticket_numbers = len(str(ticket_number)) == LEN_TICKET_NUMBER
    is_positive = ticket_number > 0
    if not (len_ticket_numbers and is_positive):
        raise exceptions.VariableHasInvalidWriteFormat('ticket_number', ticket_number)


def check_airline_name(airline_name: str) -> None:
    """Check the validly of the airline name.

    Args:
        airline_name (str): name of the airline.

    Raises:
        VariableHasInvalidWriteFormat: if airline_name has an invalid write format.
    """
    check_type('airline_name', airline_name, str)
    is_letters_and_numbers = airline_name.replace(' ', '').isalnum()
    is_words = len(airline_name.strip().split()) == airline_name.count(' ') + 1
    if not (is_letters_and_numbers and is_words):
        raise exceptions.VariableHasInvalidWriteFormat('airline_name', airline_name)
