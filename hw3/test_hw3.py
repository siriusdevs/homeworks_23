"""Test module for HW3."""

import pytest

from hw3 import Car, CarDilership, Owner, Sale


def test_invalid_instance_creation():
    """Test the creation of a class with invalid attributes."""
    with pytest.raises(TypeError):
        Car('ferrari', 'GTS812', '2020')
    with pytest.raises(TypeError):
        Owner('Slavik', '[ferrari, lamborghini]')
    with pytest.raises(TypeError):
        CarDilership('[supra]')
    with pytest.raises(TypeError):
        Sale('Car', 'Owner', 'CarDilership')


def test_valid_car_instance_creation():
    """Test the creation of a Car instance with correct attributes."""
    year_of_release_supra = 1993
    supra = Car('Toyota', 'A80', year_of_release_supra)
    assert supra.brand == 'Toyota'
    assert supra.model == 'A80'
    assert supra.year_of_release == year_of_release_supra


def test_valid_owner_instance_creation():
    """Test the creation of a Owner instance with correct attributes."""
    year_of_release_batmobile = 1966
    batmobile = Car('Batmobile', 'V1', year_of_release_batmobile)
    alfred = Owner('Alfred', [batmobile])
    assert alfred.name == 'Alfred'
    assert alfred.cars == [batmobile]


def test_valid_cardilership_instance_creation():
    """Test the creation of a CarDilership instance with correct attributes."""
    year_of_release_lada = 2011
    year_of_release_porsche = 1963
    available_cars = [
        Car('Laga', 'Granta', year_of_release_lada),
        Car('Porsche', '911', year_of_release_porsche),
    ]
    three_bolts = CarDilership(available_cars)
    assert three_bolts.available_cars == available_cars


def test_valid_sale_instance_creation():
    """Test the creation of a Sale instance with correct attributes."""
    year_of_release_bmw = 1984
    owner_cars = [Car('BMW', 'M5', year_of_release_bmw)]
    anti_slavik = Owner('Anti-Slavik', owner_cars)

    year_of_release_mercedes = 1954
    available_cars = [Car('Mercedes-Benz', 'S-CLASS ', year_of_release_mercedes)]
    povareshka = CarDilership(available_cars)

    sale = Sale(available_cars[0], anti_slavik, povareshka)
    assert sale.car_on_sale == available_cars[0]
    assert sale.car_owner.name == anti_slavik.name
    assert sale.car_dilership.available_cars == available_cars


def test_correct_sale_operation():
    """Test the correctness of car sales."""
    year_of_release_rolls = 1971
    owner_cars = [Car('Rolls-Royce', 'Corniche', year_of_release_rolls)]
    bob = Owner('Bob', owner_cars)

    year_of_release_mercedes = 1954
    available_cars = [Car('Mercedes-Benz', 'S-CLASS ', year_of_release_mercedes)]
    povareshka = CarDilership(available_cars)

    sale = Sale(available_cars[0], bob, povareshka)
    sale.sale()
    assert not povareshka.available_cars
    assert bob.cars == owner_cars + available_cars


@pytest.mark.xfail()
def test_negative_sale_operations():
    """Test the sale of a car from an empty cardilership."""
    year_of_release_audi = 2024
    owner_cars = [Car('Audi', 'Q4 SportBack', year_of_release_audi)]
    stas = Owner('Stas', owner_cars)

    available_cars = []
    bednaya_dolina = CarDilership(available_cars)

    sale = Sale(available_cars[0], stas, bednaya_dolina)
    sale.sale()
