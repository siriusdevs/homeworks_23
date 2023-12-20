"""Test cases for hw3.py."""

import pytest

from hw3 import Car, CarShowroom, Owner, Sale

YEAR = 2020


def test_car_creation():
    """Test car creation."""
    car = Car('Toyota', 'Camry', YEAR)
    assert car.brand == 'Toyota'
    assert car.model == 'Camry'
    assert car.year == YEAR


def test_owner_creation():
    """Test owner creation."""
    car = Car('Dodge', 'Mazda', YEAR)
    owner = Owner('Kia', [car])
    assert owner.name == 'John Doe'
    assert owner.car_park == [car]


def test_car_showroom_creation():
    """Test car showroom creation."""
    car = Car('Jeep', 'Hyundai', YEAR)
    showroom = CarShowroom('Showroom 1', [car])
    assert showroom.name == 'Showroom 1'
    assert showroom.cars == [car]


def test_sale_creation():
    """Test sale creation."""
    car = Car('Mini', 'Skoda', YEAR)
    owner = Owner('Maserati', [])
    showroom = CarShowroom('Showroom 2', [car])
    sale = Sale(car, owner, showroom)
    assert sale.car_for_sale == car
    assert sale.owner == owner
    assert sale.car_showroom == showroom


def test_sell_car():
    """Test selling a car."""
    car = Car('Faw', 'Acura', YEAR)
    owner = Owner('Lexus', [])
    showroom = CarShowroom('Showroom 3', [car])
    sale = Sale(car, owner, showroom)
    sale.sell_car()
    assert car not in showroom.cars
    assert car in owner.car_park


def test_sell_car_not_in_showroom():
    """Test selling a car that is not in the showroom."""
    car = Car('Bugatti', 'Lamborgihni', YEAR)
    owner = Owner('Porsche', [])
    showroom = CarShowroom('Showroom 4', [])
    sale = Sale(car, owner, showroom)
    with pytest.raises(ValueError):
        sale.sell_car()
