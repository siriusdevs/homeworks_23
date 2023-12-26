import pytest
from hw3 import Car, PassengerCar, Truck, CarPark


passenger_car = PassengerCar('mazda', 2007, 35, 2)
car = Car('toyota', 2005, 12)
truck = Truck('mercedes', 1991, 232, 494)

car_park = CarPark([passenger_car, car])


@pytest.mark.parametrize('car, expected_value', [(car, None),
                                                 (passenger_car, None),
                                                 (truck, None)])
def test_adding_cars_in_park(car, expected_value):
    assert car_park.add(car) == expected_value


@pytest.mark.parametrize('invalid_car', [(1), ('car'), (car_park)])
def test_adding_exceptions(invalid_car):
    with pytest.raises(TypeError):
        car_park.add(invalid_car)


@pytest.mark.parametrize('car, expected_value', [(passenger_car, None), (car, None)])
def test_removing_cars_in_park(car, expected_value):
    assert car_park.remove(car) == expected_value


@pytest.mark.parametrize('invalid_car', [(1), ('car'), (car_park)])
def test_removing_exceptions_type_error(invalid_car):
    with pytest.raises(TypeError):
        car_park.remove(invalid_car)


@pytest.mark.parametrize('invalid_car', [(PassengerCar('lamborgini', 2021, 10000, 4)),
                                         (Truck('Ural', 1991, 500, 2))])
def test_removing_exceptions_value_error(invalid_car):
    with pytest.raises(ValueError):
        car_park.remove(invalid_car)
