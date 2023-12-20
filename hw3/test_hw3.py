"""Module for testing the main file."""


import pytest

from hw3 import AutoPark, CargoCar, Motorcar


# test Car
def test_model_getter():
    """Test getter model."""
    motorcar = Motorcar('BMW', 2023, 50000, 2)
    assert motorcar.model == 'BMW'


def test_model_setter():
    """Test setter model."""
    motorcar = Motorcar('BMW', 2018, 50000, 2)
    motorcar.model = 'BMW M5'
    assert motorcar.model == 'BMW M5'


@pytest.mark.xfail(raises=TypeError)
def test_model_setter_non_string_value():
    """Test setter model (non_string_value)."""
    motorcar = Motorcar('BMW', 2023, 50000, 2)
    motorcar.model = 5


def test_year_getter():
    """Test getter year."""
    motorcar = Motorcar('BMW', 2019, 50000, 2)
    assert motorcar.year == 2019


def test_year_setter():
    """Test setter year."""
    motorcar = Motorcar('BMW', 2023, 50000, 2)
    motorcar.year = 2024
    assert motorcar.year == 2024


@pytest.mark.xfail(raises=ValueError)
def test_year_setter_non_string_value():
    """Test setter year (non_string_value)."""
    motorcar = Motorcar('BMW', 2023, 50000, 2)
    motorcar.year = -1


def test_price_getter():
    """Test getter price."""
    motorcar = Motorcar('BMW', 2023, 50000, 2)
    assert motorcar.price == 50000


def test_price_setter():
    """Test setter price."""
    motorcar = Motorcar('BMW', 2023, 50000, 2)
    motorcar.price = 40000
    assert motorcar.price == 40000


@pytest.mark.xfail(raises=ValueError)
def test_price_setter_non_string_value():
    """Test setter price (non_string_value)."""
    motorcar = Motorcar('BMW', 2023, 50000, 2)
    motorcar.price = -1


# test Motorcar
def test_seats_getter():
    """Test getter seats."""
    motorcar = Motorcar('Toyota', 2018, 20000, 5)
    assert motorcar.seats == 5


def test_seats_setter():
    """Test setter seats."""
    motorcar = Motorcar('Toyota', 2018, 20000, 5)
    motorcar.seats = 4
    assert motorcar.seats == 4


@pytest.mark.xfail(raises=ValueError)
def test_seats_setter_negative_value():
    """Test setter price (negative_value)."""
    motorcar = Motorcar('Toyota', 2018, 20000, 5)
    motorcar.seats = -1


@pytest.mark.xfail(raises=TypeError)
def test_seats_setter_non_integer_value():
    """Test setter price (non_integer_value)."""
    motorcar = Motorcar('Toyota', 2018, 20000, 5)
    motorcar.seats = 'five'


# test CargoCar
def test_payload_getter():
    """Test getter payload."""
    cargocar = CargoCar('NISSAN', 2021, 30000, 5)
    assert cargocar.payload == 5


def test_payload_setter():
    """Test setter payload."""
    cargocar = CargoCar('NISSAN', 2021, 30000, 5)
    CargoCar.payload = 4
    assert cargocar.payload == 4


@pytest.mark.xfail(raises=ValueError)
def test_payload_setter_negative_value():
    """Test setter price (negative_value)."""
    cargocar = CargoCar('NISSAN', 2021, 30000, 5)
    cargocar.payload = -1


@pytest.mark.xfail(raises=TypeError)
def test_payload_setter_non_integer_value():
    """Test setter price (non_integer_value)."""
    cargocar = CargoCar('NISSAN', 2021, 30000, 5)
    cargocar.payload = '100'


# test AutoPark
def test_cars_getter():
    """Test getter cars."""
    motorcar = Motorcar('BMW', 2021, 30000, 5)
    cargocar = CargoCar('MAN', 2023, 50000, 2)
    autopark = AutoPark([motorcar, cargocar])
    assert autopark.cars == ['BMW', 'MAN']


def test_cars_setter():
    """Test setter cars."""
    motorcar = Motorcar('BMW', 2021, 30000, 5)
    cargocar = CargoCar('MAN', 2023, 50000, 2)
    autopark = AutoPark()
    autopark.cars = [motorcar, cargocar]
    assert autopark.cars == ['BMW', 'MAN']


@pytest.mark.xfail(raises=TypeError)
def test_cars_setter_non_list_value():
    """Test setter price (non_list_value)."""
    autopark = AutoPark()
    autopark.cars = 'BMW'


@pytest.mark.xfail(raises=TypeError)
def test_cars_setter_non_car_value():
    """Test setter price (non_car_value)."""
    autopark = AutoPark()
    autopark.cars = ['BMW']


def test_cars_add():
    """Test add car."""
    motorcar = Motorcar('BMW', 2021, 30000, 5)
    cargocar = CargoCar('MAN', 2023, 50000, 2)
    cargocar2 = CargoCar('NISSAN', 1993, 50000, 2)
    autopark = AutoPark([motorcar, cargocar])
    autopark.add_car(cargocar2)
    assert autopark.cars == ['BMW', 'MAN', 'NISSAN']


def test_cars_remove():
    """Test remove car."""
    motorcar = Motorcar('BMW', 2021, 30000, 5)
    cargocar = CargoCar('MAN', 2023, 50000, 2)
    autopark = AutoPark([motorcar, cargocar])
    autopark.remove_car(cargocar)
    assert autopark.cars == ['BMW']


@pytest.mark.xfail(raises=TypeError)
def test_cars_add_non_car_value():
    """Test add car (non_car_value)."""
    autopark = AutoPark()
    autopark.add_car('BMW')


@pytest.mark.xfail(raises=ValueError)
def test_cars_remove_car_not_found():
    """Test remove car (car_not_found)."""
    autopark = AutoPark()
    motorcar = Motorcar('BMW', 2021, 30000, 5)
    autopark.remove_car(motorcar)


@pytest.mark.xfail(raises=TypeError)
def test_cars_remove_non_car_value():
    """Test remove car (non_car_value)."""
    autopark = AutoPark()
    autopark.remove_car('BMW')
