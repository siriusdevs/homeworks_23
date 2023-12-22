"""Tests for HW3."""

from typing import Any

import pytest

from hw3 import Car, CarPark, FreightCar, PassengerCar

semerka = PassengerCar('Vishnevaya Semerka', 2019, 100.0, 4)
michael = FreightCar('Noskoff3000', 2023, 500.0, 50)
semyon = PassengerCar('Komarov', 2006, 85.0, 4)
carpark = CarPark([semerka, michael])

TEST_GET_SET_DATA = (
    (semerka, 'model', 'Vishnevaya Semerka', 'Cherry 7'),
    (semerka, 'year', 2019, 2023),
    (semerka, 'price', 100.0, 500.0),
    (semerka, 'seats', 4, 5),
    (michael, 'lifting_capacity', 50, 30),
)

TEST_ERRORS_DATA = (
    (semerka, 'model', 15),
    (semerka, 'year', '2023'),
    (semerka, 'price', True),
    (semerka, 'seats', [1, 2, 3, 4]),
    (michael, 'lifting_capacity', {'lifting_capacity': 45}),
)


@pytest.mark.parametrize('car, attribute, curr_value, new_value', TEST_GET_SET_DATA)
def test_getters_setters(car: Car, attribute: str, curr_value: Any, new_value: Any) -> None:
    """Test all getters and setters.

    Args:
        car: car object that will change
        attribute: attribute that will change
        curr_value: current value of the car object
        new_value: new value of the car object
    """
    assert getattr(car, attribute) == curr_value, "Getter don't work"
    setattr(car, attribute, new_value)
    assert getattr(car, attribute) == new_value, "Setter don't work"


@pytest.mark.parametrize('car, attribute, new_value', TEST_ERRORS_DATA)
@pytest.mark.xfail(raises=TypeError)
def test_incorrect_type_setter(car: Car, attribute: str, new_value: Any):
    """Test type setter (if the value type is wrong).

    Args:
        car: car object
        attribute: attribute car object
        new_value: wrong type
    """
    setattr(car, attribute, new_value)


def test_add_cars():
    """Test add car to carpark."""
    carpark.add(semyon)
    assert carpark.get_all() == [semerka, michael, semyon]


def test_remove_cars():
    """Test remove car to carpark."""
    carpark.remove(semyon)
    assert carpark.get_all() == [semerka, michael]
