"""Module for Homework 3."""

from typing import Any


def check_type(input_value: Any, expected_type: type) -> bool:
    """
    Check if the input value is of the expected type.

    Args:
        input_value: The input value to check.
        expected_type: The expected type of the input value.

    Returns:
        True if the input value is of the expected type.

    Raises:
        ValueError: If the input value is not of the expected type.
    """
    if not isinstance(input_value, expected_type):
        raise ValueError('The input value is not of the expected type.')
    return True


class Car:
    """Class for a car."""

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Initialize the car object.

        Args:
            brand: The brand of the car.
            model: The model of the car.
            year: The year of the car.
        """
        self.brand = brand
        self.model = model
        self.year = year

    @property
    def brand(self):
        """
        Get the brand of the car.

        Returns:
            The brand of the car.
        """
        return self._brand

    @brand.setter
    def brand(self, new_brand: str) -> None:
        """
        Set the brand of the car.

        Args:
            new_brand: The brand of the car.
        """
        check_type(new_brand, str)
        self._brand = new_brand

    @property
    def model(self):
        """
        Get the model of the car.

        Returns:
            The model of the car.
        """
        return self._model

    @model.setter
    def model(self, new_model: str) -> None:
        """
        Set the model of the car.

        Args:
            new_model: The model of the car.
        """
        check_type(new_model, str)
        self._model = new_model

    @property
    def year(self):
        """
        Get the year of the car.

        Returns:
            The year of the car.
        """
        return self._year

    @year.setter
    def year(self, new_year: int) -> None:
        """
        Set the year of the car.

        Args:
            new_year: The year of the car.
        """
        check_type(new_year, int)
        self._year = new_year


class OneOwner:
    """Class for an owner."""

    def __init__(self, name: str, car_park: list[Car]):
        """
        Initialize the owner object.

        Args:
            name: The name of the owner.
            car_park: The car park of the owner.
        """
        self.name = name
        self.car_park = car_park

    @property
    def name(self):
        """
        Get the name of the owner.

        Returns:
            The name of the owner.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Set the name of the owner.

        Args:
            new_name: The name of the owner.
        """
        check_type(new_name, str)
        self._name = new_name

    @property
    def car_park(self):
        """
        Get the car park of the owner.

        Returns:
            The car park of the owner.
        """
        return self._car_park

    @car_park.setter
    def car_park(self, new_car_park: list[Car]) -> None:
        """
        Set the car park of the owner.

        Args:
            new_car_park: The car park of the owner.
        """
        check_type(new_car_park, list)
        for car in new_car_park:
            check_type(car, Car)
        self._car_park = new_car_park


class Owner(OneOwner):
    """Class for an owner."""

    def add_car(self, car: Car):
        """
        Add a car to the car park.

        Args:
            car: The car to add to the car park.
        """
        check_type(car, Car)
        self._car_park.append(car)

    def remove_car(self, car: Car):
        """
        Remove a car from the car park.

        Args:
            car: The car to remove from the car park.

        Raises:
            ValueError: if the car is not in car_park.
        """
        check_type(car, Car)
        if car not in self.car_park:
            raise ValueError('There are no such cars')
        self._car_park.remove(car)

    def get_all_cars(self):
        """
        Get all the cars in the car park.

        Returns:
            The cars in the car park.
        """
        return self._car_park


class CarShowroom:
    """Class for a car showroom."""

    def __init__(self, name: str, cars: list[Car]):
        """
        Initialize the car showroom object.

        Args:
            name: The name of the car showroom.
            cars: The cars in the car showroom.
        """
        self.name = name
        self.cars = cars

    @property
    def name(self):
        """
        Get the name of the car showroom.

        Returns:
            The name of the car showroom.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Set the name of the car showroom.

        Args:
            new_name: The name of the car showroom.
        """
        check_type(new_name, str)
        self._name = new_name

    @property
    def cars(self):
        """
        Get the cars in the car showroom.

        Returns:
            The cars in the car showroom.
        """
        return self._cars

    @cars.setter
    def cars(self, new_cars: list[Car]) -> None:
        """
        Set the cars in the car showroom.

        Args:
            new_cars: The cars in the car showroom.
        """
        check_type(new_cars, list)
        for car in new_cars:
            check_type(car, Car)
        self._cars = new_cars

    def add_car(self, car: Car):
        """
        Add a car to the car showroom.

        Args:
            car: The car to add to the car showroom.
        """
        check_type(car, Car)
        self._cars.append(car)

    def remove_car(self, car: Car):
        """
        Remove a car from the car showroom.

        Args:
            car: The car to remove from the car showroom.

        Raises:
            ValueError: The machine does not exist..
        """
        check_type(car, Car)
        if car not in self.cars:
            raise ValueError('The car is out of stock')
        self._cars.remove(car)


class AbstractSale:
    """Class for a sale."""

    def __init__(self, car_for_sale: Car, owner: OneOwner, car_showroom: CarShowroom):
        """
        Initialize the sale object.

        Args:
            car_for_sale: The car for sale.
            owner: The owner of the car.
            car_showroom: The car showroom of the car.
        """
        self.car_for_sale = car_for_sale
        self.owner = owner
        self.car_showroom = car_showroom

    @property
    def car_for_sale(self):
        """
        Get the car for sale.

        Returns:
            The car for sale.
        """
        return self._car_for_sale

    @car_for_sale.setter
    def car_for_sale(self, new_car_for_sale: Car) -> None:
        """
        Set the car for sale.

        Args:
            new_car_for_sale: The car for sale.
        """
        check_type(new_car_for_sale, Car)
        self._car_for_sale = new_car_for_sale

    @property
    def owner(self):
        """
        Get the owner of the car.

        Returns:
            The owner of the car.
        """
        return self._owner

    @owner.setter
    def owner(self, new_owner: OneOwner) -> None:
        """
        Set the owner of the car.

        Args:
            new_owner: The owner of the car.
        """
        check_type(new_owner, Owner)
        self._owner = new_owner

    @property
    def car_showroom(self):
        """
        Get the car showroom of the car.

        Returns:
            The car showroom of the car.
        """
        return self._car_showroom

    @car_showroom.setter
    def car_showroom(self, new_car_showroom: CarShowroom) -> None:
        """
        Set the car showroom of the car.

        Args:
            new_car_showroom: The car showroom of the car.
        """
        check_type(new_car_showroom, CarShowroom)
        self._car_showroom = new_car_showroom


class Sale(AbstractSale):
    """Class for a sale."""

    def sell_car(self):
        """Sell the car."""
        self.car_showroom.remove_car(self.car_for_sale)
        self.owner.add_car(self.car_for_sale)
