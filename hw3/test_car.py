"""Module that tests functionality class Car and check type function in hw3.py."""

import pytest

from hw3 import Car


def test_car_creation():
    """Test for car creation."""
    car = Car('Subaru', 'ABC125', 'Sedan')
    assert car.label == 'Subaru'
    assert car.license_plate == 'ABC125'
    assert car.car_body == 'Sedan'


def test_car_body_change():
    """Test for car body change."""
    car = Car('Porsche', 'ABC13', 'Sedan')
    car.car_body = 'Hatchback'
    assert car.car_body == 'Hatchback'


def test_check_type_raises_error():
    """Test for check type raises errors."""
    with pytest.raises(TypeError):
        Car([12345], 'ABC123', 'Баклажан')
    with pytest.raises(TypeError):
        Car('YAZ', (67890,), 'Crossover')
    with pytest.raises(TypeError):
        Car('Ferrari', 'ZXC567', 000)
