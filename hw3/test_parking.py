"""Module that tests functionality class parking and check type function in hw3.py."""

import pytest

from hw3 import Parking, Vehicle


def setup_vehicles():
    """Create vehicles.

    Returns:
        _type_: List of Vehicles.
    """
    vehicle1 = Vehicle('Toyota', 'ABC123')
    vehicle2 = Vehicle('Honda', 'XYZ789')
    return [vehicle1, vehicle2]


def test_parking_creation():
    """Test for Parking creation."""
    parking = Parking(setup_vehicles(), 10)
    assert parking.capacity == 10
    assert len(parking.list_of_vehicles) == 2


def test_add_vehicle_to_parking():
    """Test for add vehicle to parking."""
    parking = Parking([setup_vehicles()[0]], 5)
    parking.add_vehicle(setup_vehicles()[1])
    assert len(parking.list_of_vehicles) == 2


def test_remove_vehicle_from_parking():
    """Test for remove vehicle from parking."""
    vehicles = setup_vehicles()
    parking = Parking(vehicles, 10)
    parking.remove_vehicle(vehicles[0])
    assert len(parking.list_of_vehicles) == 1


def test_get_free_places():
    """Test for get free places on parking."""
    parking = Parking(setup_vehicles(), 3)
    assert parking.get_free_places() == 1


def test_check_type_raises_error():
    """Test for check type raises errors."""
    with pytest.raises(TypeError):
        Parking('Car', 10)
    with pytest.raises(TypeError):
        Parking(setup_vehicles(), '67890')
    with pytest.raises(TypeError):
        Parking([Vehicle('BMW', 'OY567T'), 'Vehicle'], '67890')


def test_check_value_raises_error():
    """Test for check value raises errors."""
    with pytest.raises(ValueError):
        vehicle = setup_vehicles()
        parking = Parking(vehicle, 10)
        parking.remove_vehicle(Vehicle('Car', 'RT432J'))
    with pytest.raises(ValueError):
        vehicle = setup_vehicles()
        parking = Parking(vehicle, 2)
        parking.add_vehicle(Vehicle('Auto', 'RT932J'))
    with pytest.raises(ValueError):
        vehicle = setup_vehicles()
        parking = Parking(vehicle, 1)
