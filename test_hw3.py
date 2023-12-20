"""Test module for the classes and functions defined in hw3.py."""

import pytest

from hw3 import Car, Parking, Truck, Vehicle, check_type

YEAR2020 = 2020
YEAR2003 = 2003
YEAR1974 = 1974
YEAR2000 = 2000

PRICE40000 = 40000.0
PRICE150000 = 150000.0
PRICE100000 = 100000.0

SEATS3 = 3
SEATS4 = 4
SEATS5 = 5

LIFT14000 = 14000


def test_check_type():
    """Test the check type function."""
    assert check_type(5, int) is None
    with pytest.raises(TypeError):
        check_type(5, str)
    with pytest.raises(ValueError):
        check_type(-5, int, check_positive=True)


def test_vehicle():
    """Test the Vehicle class."""
    vehicle = Vehicle('Volkswagen Golf mk8', YEAR2020, PRICE40000)
    assert vehicle.model == 'Volkswagen Golf mk8'
    assert vehicle.year_of_issue == YEAR2020
    assert vehicle.price == PRICE40000


def test_car():
    """Test the Car class."""
    car = Car('Porsche 911', YEAR2020, PRICE150000, SEATS3)
    assert car.model == 'Porsche 911'
    assert car.year_of_issue == YEAR2020
    assert car.price == PRICE150000
    assert car.passenger_seats == SEATS3


def test_truck():
    """Test the Truck class."""
    truck = Truck('Kamaz 65111', YEAR2003, PRICE100000, LIFT14000)
    assert truck.model == 'Kamaz 65111'
    assert truck.year_of_issue == YEAR2003
    assert truck.price == PRICE100000
    assert truck.lift_capacity == LIFT14000


def test_parking():
    """Test the Parking class."""
    vehicle = Car('zhigul', YEAR1974, float('inf'), SEATS4)
    without_parking = Car('lada', YEAR2000, PRICE40000, SEATS5)
    test_parking_vehicle = Parking([vehicle])
    with pytest.raises(ValueError):
        test_parking_vehicle.add_vehicle(vehicle)
    with pytest.raises(RuntimeError):
        test_parking_vehicle.remove_vehicle(without_parking)
    assert test_parking_vehicle.vehicles == [vehicle]
