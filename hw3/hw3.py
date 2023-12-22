"""Homework №3.

Учет автомобилей и их владельцев

Архитектура классов для учета автомобилей и их владельцев:

Класс "Автомобиль":
Поля:
Марка автомобиля
Модель автомобиля
Год выпуска автомобиля
Методы:
Геттеры и сеттеры для полей

Класс "Владелец":
Поля:
Имя владельца
Список автомобилей владельца (массив или список объектов класса "Автомобиль")
Методы:
Геттеры и сеттеры для полей
Добавить автомобиль в список автомобилей владельца
Удалить автомобиль из списка автомобилей владельца
Получить список всех автомобилей владельца

Класс "Автосалон":
Поля:
Название автосалона
Список доступных автомобилей для продажи (массив или список объектов класса "Автомобиль")
Методы:
Геттеры и сеттеры для полей
Добавить автомобиль в список доступных автомобилей
Удалить автомобиль из списка доступных автомобилей

Класс "Продажа":
Поля:
Автомобиль, который продается (объект класса "Автомобиль")
Владелец автомобиля (объект класса "Владелец")
Автосалон, в котором происходит продажа (объект класса "Автосалон")
Методы:
Геттеры и сеттеры для полей
Произвести продажу автомобиля (удалить автомобиль из списка доступных автомобилей автосалона
и добавить его в список автомобилей владельца)
"""
from typing import Any, Callable


def _check_simple_type(attr_name: str, attr_value: Any, expected_type: Any) -> None:
    if not isinstance(attr_value, expected_type):
        error_msg = '{0}: {1} should be {2}'.format(
            attr_name,
            type(attr_value).__name__,
            expected_type,
        )
        raise TypeError(error_msg)


def _check_complex_type(
    attr_name: str,
    attr_values: list[Any] | tuple[Any],
    expected_type: Any,
) -> None:
    _check_simple_type(attr_name, attr_values, list | tuple)
    for attr_value in attr_values:
        _check_simple_type(attr_name, attr_value, expected_type)


def _check_positive_int(attr_name: str, attr_value: int) -> None:
    _check_simple_type(attr_name, attr_value, int)
    if attr_value < 0:
        raise ValueError(f'{attr_name}: {attr_value} should be positive int')


def _ensure(attr: str, checker: Callable, expected_type: Any | None = None) -> Callable:
    def add_property(class_: type) -> type:
        def getter(self):
            return getattr(self, f'_{attr}')

        def setter(self, new_attr_value: Any) -> None:
            if expected_type:
                checker(attr, new_attr_value, expected_type)
            else:
                checker(attr, new_attr_value)
            setattr(self, f'_{attr}', new_attr_value)

        setattr(class_, attr, property(getter, setter))
        return class_
    return add_property


@_ensure('brand', _check_simple_type, str)
@_ensure('model', _check_simple_type, str)
@_ensure('year_of_release', _check_positive_int)
class Car:
    """Car for sale."""

    def __init__(self, brand: str, model: str, year_of_release: int) -> None:
        """Initialize car with brand, model and year of reliase.

        Args:
            brand: str - car brand.
            model: str - car model.
            year_of_release: int - the year of manufacture of the car.
        """
        self.brand, self.model, self.year_of_release = brand, model, year_of_release

    def __str__(self) -> str:
        """Present an instance as a string.

        Returns:
            string of the instance.
        """
        return '{0} {1} {2} {3} year'.format(
            type(self).__name__,
            self.brand,
            self.model,
            self.year_of_release,
        )


@_ensure('name', _check_simple_type, str)
@_ensure('cars', _check_complex_type, Car)
class Owner:
    """Car owner."""

    def __init__(self, name: str, cars: list[Car]) -> None:
        """Initialize the name of the owner and his cars.

        Args:
            name: str - owner's name.
            cars: list[Car] - list of the owner's cars.
        """
        self.name, self.cars = name, cars

    def add_car(self, car: Car) -> None:
        """Add a car to the owner's car list.

        Args:
            car: Car - the car that needs to be added.
        """
        _check_simple_type('car', car, Car)
        self.cars.append(car)

    def remove_car(self, car: Car) -> None:
        """Remove a car from the owner's car list.

        Args:
            car: Car - the machine that needs to be removed.

        Raises:
            ValueError: the owner does not have this car.
        """
        if car in self.cars:
            while car in self.cars:
                self.cars.remove(car)
        else:
            raise ValueError(f'{self.cars} does not contain {car}')


@_ensure('available_cars', _check_complex_type, Car)
class CarDilership:
    """A car dealership where cars are sold."""

    def __init__(self, available_cars: list[Car]) -> None:
        """Initialize CarDilership.

        Args:
            available_cars: list[Car] - list of available cars for sale.
        """
        self.available_cars = available_cars

    def add_car(self, car: Car) -> None:
        """Add a car to the list of available car dealerships.

        Args:
            car: Car - the car that needs to be added.
        """
        _check_simple_type('car', car, Car)
        self.available_cars.append(car)

    def remove_car(self, car: Car) -> None:
        """Remove a car from the list of available dealership cars.

        Args:
            car: Car - the machine that needs to be removed.

        Raises:
            ValueError: the car is not in the dealership.
        """
        if car in self.available_cars:
            self.available_cars.remove(car)
        else:
            raise ValueError(f'{self.available_cars} does not contain {car}')


@_ensure('car_on_sale', _check_simple_type, Car)
@_ensure('car_owner', _check_simple_type, Owner)
@_ensure('car_dilership', _check_simple_type, CarDilership)
class Sale:
    """Car sale from a car dealership."""

    def __init__(self, car_on_sale: Car, car_owner: Owner, car_dilership: CarDilership) -> None:
        """Initialize Sale.

        Args:
            car_on_sale: Car - the car that is being sold.
            car_owner: Owner - car owner.
            car_dilership: CarDilership - the car dealership where the sale takes place.
        """
        self.car_on_sale = car_on_sale
        self.car_owner = car_owner
        self.car_dilership = car_dilership

    def sale(self) -> None:
        """Sell a car from a car dealership."""
        self.car_dilership.remove_car(self.car_on_sale)
        self.car_owner.add_car(self.car_on_sale)
