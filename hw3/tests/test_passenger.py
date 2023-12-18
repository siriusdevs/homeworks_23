"""Module with tests for hw3.passenger module."""

import pytest

from ..passenger import Passenger


def test_passenger_happy():
    """Create a passenger, assert on its getters and use its setters."""
    test_passenger = Passenger('Vasya', '424242')
    assert test_passenger.name == 'Vasya'
    assert test_passenger.passport_num == '424242'
    test_passenger.name = 'Petya'
    test_passenger.passport_num = '654321'
    assert test_passenger.name == 'Petya'
    assert test_passenger.passport_num == '654321'


def test_passenger_constructor_errors():
    """Assert that creating a passenger with invalid values raises an error."""
    with pytest.raises(TypeError):
        Passenger(42, '123123')
    with pytest.raises(TypeError):
        Passenger('Misha', 123456)
    with pytest.raises(ValueError):
        Passenger('Misha', '123')
    with pytest.raises(ValueError):
        Passenger('Misha', '12345A')


def test_passenger_setter_errors():
    """Create a passenger and assert that trying to set invalid values fails."""
    test_passenger = Passenger('Volodya', '123456')
    with pytest.raises(TypeError):
        test_passenger.name = 999
    with pytest.raises(TypeError):
        test_passenger.passport_num = 654321
    with pytest.raises(ValueError):
        test_passenger.passport_num = '321'
    with pytest.raises(ValueError):
        test_passenger.passport_num = 'AAA333'
