"""Test cases for hw3.py"""

import pytest

from hw3 import Car, Owner, CarShowroom, Sale


def test_car_creation():
    car = Car("Toyota", "Camry", 2020)
    assert car.brand == "Toyota"
    assert car.model == "Camry"
    assert car.year == 2020

def test_owner_creation():
    car = Car("Toyota", "Camry", 2020)
    owner = Owner("John Doe", [car])
    assert owner.name == "John Doe"
    assert owner.car_park == [car]

def test_car_showroom_creation():
    car = Car("Toyota", "Camry", 2020)
    showroom = CarShowroom("Showroom 1", [car])
    assert showroom.name == "Showroom 1"
    assert showroom.cars == [car]

def test_sale_creation():
    car = Car("Toyota", "Camry", 2020)
    owner = Owner("John Doe", [])
    showroom = CarShowroom("Showroom 1", [car])
    sale = Sale(car, owner, showroom)
    assert sale.car_for_sale == car
    assert sale.owner == owner
    assert sale.car_showroom == showroom

def test_sell_car():
    car = Car("Toyota", "Camry", 2020)
    owner = Owner("John Doe", [])
    showroom = CarShowroom("Showroom 1", [car])
    sale = Sale(car, owner, showroom)
    sale.sell_car()
    assert car not in showroom.cars
    assert car in owner.car_park

def test_sell_car_not_in_showroom():
    car = Car("Toyota", "Camry", 2020)
    owner = Owner("John Doe", [])
    showroom = CarShowroom("Showroom 1", [])
    sale = Sale(car, owner, showroom)
    with pytest.raises(ValueError):
        sale.sell_car()
