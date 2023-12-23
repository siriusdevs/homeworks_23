"""Module for testing passenger module."""

import pytest

from .. import hw3
from ..passenger import Passenger


def test_passenger_good_setter():
    """Test for passenger setter with good outcome."""
    passenger = Passenger('vadim', '123456')
    assert passenger.name == 'vadim'
    assert passenger.passport_id == '123456'
    passenger.name = 'sasha'
    passenger.passport_id = '111111'
    assert passenger.name == 'sasha'
    assert passenger.passport_id == '111111'


def test_passenger_bad_setter():
    """Test for passenger setter with bad outcome."""
    passenger = Passenger('vadim', '123456')
    with pytest.raises(hw3.InvalidType):
        passenger.name = 12
    with pytest.raises(hw3.InvalidType):
        passenger.passport_id = 134
    with pytest.raises(ValueError):
        passenger.passport_id = '1234567'
    with pytest.raises(ValueError):
        passenger.passport_id = 'aaaaaa'
