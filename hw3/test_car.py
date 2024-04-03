import pytest
from hw3 import Car

TOYOTA_MODEL = 'Toyota'


def test_init():
    """Test initialization of Car object."""
    car = Car(TOYOTA_MODEL, 2022, 30000.0)
    assert car.model == TOYOTA_MODEL
    assert car.year == 2022
    assert car.cost == 30000.0


def test_invalid_model_type():
    """Test invalid model type."""
    with pytest.raises(TypeError):
        Car(123, 2022, 30000.0)


def test_invalid_year_type():
    """Test invalid year type."""
    with pytest.raises(TypeError):
        Car(TOYOTA_MODEL, '2022', 30000.0)


def test_invalid_cost_type():
    """Test invalid cost type."""
    with pytest.raises(TypeError):
        Car(TOYOTA_MODEL, 2022, '30000.0')


def test_empty_model():
    """Test empty model."""
    with pytest.raises(ValueError):
        Car('', 2022, 30000.0)


def test_empty_year():
    """Test empty year."""
    with pytest.raises(TypeError):
        Car(TOYOTA_MODEL, None, 30000.0)


def test_empty_cost():
    """Test empty cost."""
    with pytest.raises(TypeError):
        Car(TOYOTA_MODEL, 2022, None)


def test_extra_argument():
    """Test extra argument passed to Car."""
    with pytest.raises(TypeError):
        Car(TOYOTA_MODEL, 2022, 30000.0, 'extra')
