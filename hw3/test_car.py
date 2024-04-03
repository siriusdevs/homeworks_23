"""Tests for Car class."""
import pytest
from hw3 import Car


TOYOTA_MODEL = 'Toyota'
MODEL_YEAR = 2024
CAR_COST = 35000.0


def test_init():
    """Test initialization of Car object."""
    car = Car(TOYOTA_MODEL, MODEL_YEAR, CAR_COST)
    assert car.model == TOYOTA_MODEL
    assert car.year == MODEL_YEAR
    assert car.cost == CAR_COST


def test_invalid_model_type():
    """Test invalid model type."""
    with pytest.raises(TypeError):
        Car(123, MODEL_YEAR, CAR_COST)


def test_invalid_year_type():
    """Test invalid year type."""
    with pytest.raises(TypeError):
        Car(TOYOTA_MODEL, '2022', CAR_COST)


def test_invalid_cost_type():
    """Test invalid cost type."""
    with pytest.raises(TypeError):
        Car(TOYOTA_MODEL, MODEL_YEAR, '30000.0')


def test_empty_model():
    """Test empty model."""
    with pytest.raises(ValueError):
        Car('', MODEL_YEAR, CAR_COST)


def test_empty_year():
    """Test empty year."""
    with pytest.raises(TypeError):
        Car(TOYOTA_MODEL, None, CAR_COST)


def test_empty_cost():
    """Test empty cost."""
    with pytest.raises(TypeError):
        Car(TOYOTA_MODEL, MODEL_YEAR, None)


def test_extra_argument():
    """Test extra argument passed to Car."""
    with pytest.raises(TypeError):
        Car(TOYOTA_MODEL, MODEL_YEAR, CAR_COST, 'extra')
