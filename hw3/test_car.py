import pytest
from hw3 import Car


def test_init():
    car = Car('Toyota', 2022, 30000.0)
    assert car.model == 'Toyota'
    assert car.year == 2022
    assert car.cost == 30000.0


def test_invalid_model_type():
    with pytest.raises(TypeError):
        Car(123, 2022, 30000.0)


def test_invalid_year_type():
    with pytest.raises(TypeError):
        Car('Toyota', '2022', 30000.0)


def test_invalid_cost_type():
    with pytest.raises(TypeError):
        Car('Toyota', 2022, '30000.0')


def test_empty_model():
    with pytest.raises(ValueError):
        Car('', 2022, 30000.0)


def test_empty_year():
    with pytest.raises(TypeError):
        Car('Toyota', None, 30000.0)


def test_empty_cost():
    with pytest.raises(TypeError):
        Car('Toyota', 2022, None)


def test_extra_argument():
    with pytest.raises(TypeError):
        Car('Toyota', 2022, 30000.0, 'extra')
