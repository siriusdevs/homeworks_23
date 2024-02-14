import pytest
from hw3 import Car, PassengerCar, Truck, CarPark


@pytest.fixture
def car():
    return Car('toyota', 2005, 12)


@pytest.fixture
def passenger_car():
    return PassengerCar('mazda', 2007, 35, 2)


@pytest.fixture
def truck():
    return Truck('mercedes', 1991, 232, 494)


@pytest.fixture
def car_park():
    return CarPark()

@pytest.mark.parametrize('car, expected_value', [
    (Car('toyota', 2005, 12), None),
    (PassengerCar('mazda', 2007, 35, 2), None),
    (Truck('mercedes', 1991, 232, 494), None)
])
def test_add_car(car, expected_value):
    cart_park = CarPark()

    assert cart_park.add(car) == expected_value


@pytest.mark.parametrize('invalid_car', [
    (1),
    ('car'),
    (car_park)
])
def test_adding_exceptions(invalid_car):
    car_park = CarPark()
    with pytest.raises(TypeError):
        car_park.add(invalid_car)


def test_removing_cars_in_park():
    passenger_car = PassengerCar('mazda', 2007, 35, 2)
    car = Car('toyota', 2005, 12)

    car_park = CarPark([passenger_car, car])

    assert car_park.remove(car) == None
    assert car_park.remove(passenger_car) == None


def test_removing_exceptions_type_error():
    passenger_car = PassengerCar('mazda', 2007, 35, 2)
    car = Car('toyota', 2005, 12)
    truck = Truck('mercedes', 1991, 232, 494)

    car_park = CarPark([passenger_car, car])

    with pytest.raises(TypeError):
        car_park.remove("car")
        car_park.remove(CarPark())


def test_removing_exceptions_value_error():                   
    passenger_car = PassengerCar('mazda', 2007, 35, 2)
    car = Car('toyota', 2005, 12)
    truck = Truck('mercedes', 1991, 232, 494)
    car2 = Car('toyota', 2007, 13)

    car_park = CarPark([passenger_car, car])

    with pytest.raises(ValueError):
        car_park.remove(truck)
        car_park.remove(car2)