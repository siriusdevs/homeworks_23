"""Test to check the functionality of the function."""

import pytest

import hw3

MARK1 = 5787
MARK2 = 4508
MARK3 = 999
CAR1 = hw3.Car('hhhh', MARK1, '4h')
CAR2 = hw3.Car('ggg', MARK2, '3g')
CAR3 = hw3.Car('asd', MARK3, 'carbon')

test_valid_car = (
    (('hfgu', 5787, 'fjgf'), 'Car hfgu 5787'),
)

test_valid_parking = (
    (
        [CAR1, CAR2],
        5,
        f'Vehicles on parking: {[CAR1, CAR2]}',
    ),
)

test_parking_values = (
    ([CAR2, CAR3], f'Vehicles on parking: {[CAR3, CAR1]}'),
)


@pytest.mark.parametrize('input_data, expected', test_valid_car)
def test_comparison_valid_car(input_data: tuple, expected: str) -> None:
    """Check for correct car values.

    Args:
        input_data: tuple - information about car.
        expected: str - expected function output.
    """
    test_str = str(hw3.Car(*input_data))
    assert test_str == expected


@pytest.mark.parametrize('vehicles, max_amount, expected', test_valid_parking)
def test_parking_valid(vehicles: list, max_amount: int, expected: str):
    """Check for correct parking values.

    Args:
        vehicles: list - list with vehicles.
        max_amount: int - maximum possiple number of vehicles.
        expected: str - expected function output.
    """
    test_parking = hw3.Parking(vehicles, max_amount).vehicles_lst()
    assert expected == test_parking


@pytest.mark.xfail
def test_car_fail_fst():
    """Check for invalid body."""
    hw3.Car('2333', 1, 2)


@pytest.mark.xfail
def test_car_fail_snd():
    """Check for invalid license plate."""
    hw3.Car('2333', 'dsd', 'metal')


@pytest.mark.xfail
def test_car_fail_trd():
    """Check for invalid mark."""
    hw3.Car(3, 'dsd', 'metal')


@pytest.mark.parametrize('vehicles, expected', test_parking_values)
def test_parking(vehicles: list[hw3.Vehicle], expected: str) -> None:
    """Check for invalid values.

    Args:
        vehicles: list[hw3.Vehicle] - list with vehicles.
        expected: str - expected function output.
    """
    parking = hw3.Parking(vehicles, 3)
    parking.remove_vehicle(CAR2)
    parking.add_vehicle(CAR1)
    parking_test = parking.vehicles_lst()
    assert parking_test == expected
