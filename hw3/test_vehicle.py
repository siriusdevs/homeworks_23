"""Module that tests functionality class Vehicle and check type function in hw3.py."""

import pytest

from hw3 import Vehicle


def test_vehicle_creation():
    """Test for vehicle creation."""
    vehicle = Vehicle('Toyota', 'ABC143')
    assert vehicle.label == 'Toyota'
    assert vehicle.license_plate == 'ABC143'


def test_vehicle_label_change():
    """Test for vehicle label change."""
    vehicle = Vehicle('Mazda', 'ABC123')
    vehicle.label = 'Honda'
    assert vehicle.label == 'Honda'


def test_vehicle_license_plate_change():
    """Test for vehicle license plate change."""
    vehicle = Vehicle('BMW', 'VDC123')
    vehicle.license_plate = 'XYZ789'
    assert vehicle.license_plate == 'XYZ789'


def test_check_type_raises_error():
    """Test for check type raises error."""
    with pytest.raises(TypeError):
        Vehicle([12345], '67890')
    with pytest.raises(TypeError):
        Vehicle('12345', (67890,))
