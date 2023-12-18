"""Module with tests for hw3."""
import pytest

from . import hw3


def test_check_type_happy(): 
    """Tests happy paths of hw3.check_type."""
    hw3.check_type(123, int)
    hw3.check_type([1, '2'], list)
    hw3.check_type('hello', str)


def test_check_type_error():
    """Tests error paths of hw3.check_type."""
    with pytest.raises(TypeError):
        hw3.check_type(123, str)
    with pytest.raises(TypeError):
        hw3.check_type('123', int)
    with pytest.raises(TypeError):
        hw3.check_type([123], tuple)
    with pytest.raises(TypeError):
        hw3.check_type(None, bool)
