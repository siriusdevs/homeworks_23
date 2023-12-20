"""Module for Homework 3"""

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
        raise ValueError(f"Expected type {expected_type}, got {type(input_value)}")
    return True

class Car:
    """Class for a car."""

    def __init__(self, brand, model, year):
        """
        Initialize the car object.

        Args:
            brand: The brand of the car.
            model: The model of the car.
            year: The year of the car.
        """
        self.model = model
        self.year = year
        self.brand = brand

    @property
    def brand(self):
        """
        Get the brand of the car.

        Returns:
            The brand of the car.
        """
        return self._brand

    @brand.setter
    def brand(self, value):
        """
        Set the brand of the car.

        Args:
            value: The brand of the car.
        """
        check_type(value, str)
        self._brand = value

    @property
    def model(self):
        """
        Get the model of the car.

        Returns:
            The model of the car.
        """
        return self._model

    @model.setter
    def model(self, value):
        """
        Set the model of the car.

        Args:
            value: The model of the car.
        """
        check_type(value, str)
        self._model = value

    @property
    def year(self):
        """
        Get the year of the car.

        Returns:
            The year of the car.
        """
        return self._year

    @year.setter
    def year(self, value):
        """
        Set the year of the car.

        Args:
            value: The year of the car.
        """
        check_type(value, int)
        self._year = value

class Owner:
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
    def name(self, value):
        """
        Set the name of the owner.

        Args:
            value: The name of the owner.
        """
        check_type(value, str)
        self._name = value

    @property
    def car_park(self):
        """
        Get the car park of the owner.

        Returns:
            The car park of the owner.
        """
        return self._car_park

    @car_park.setter
    def car_park(self, value):
        """
        Set the car park of the owner.

        Args:
            value: The car park of the owner.
        """
        check_type(value, list)
        for car in value:
            check_type(car, Car)
        self._car_park = value

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
        """
        check_type(car, Car)
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
    def name(self, value):
        """
        Set the name of the car showroom.

        Args:
            value: The name of the car showroom.
        """
        check_type(value, str)
        self._name = value

    @property
    def cars(self):
        """
        Get the cars in the car showroom.

        Returns:
            The cars in the car showroom.
        """
        return self._cars

    @cars.setter
    def cars(self, value):
        """
        Set the cars in the car showroom.

        Args:
            value: The cars in the car showroom.
        """
        check_type(value, list)
        for car in value:
            check_type(car, Car)
        self._cars = value

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
        """
        check_type(car, Car)
        self._cars.remove(car)

class Sale:
    """Class for a sale."""

    def __init__(self, car_for_sale: Car, owner: Owner, car_showroom: CarShowroom):
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
    def car_for_sale(self, value):
        """
        Set the car for sale.

        Args:
            value: The car for sale.
        """
        check_type(value, Car)
        self._car_for_sale = value

    @property
    def owner(self):
        """
        Get the owner of the car.

        Returns:
            The owner of the car.
        """
        return self._owner

    @owner.setter
    def owner(self, value):
        """
        Set the owner of the car.

        Args:
            value: The owner of the car.
        """
        check_type(value, Owner)
        self._owner = value

    @property
    def car_showroom(self):
        """
        Get the car showroom of the car.

        Returns:
            The car showroom of the car.
        """
        return self._car_showroom

    @car_showroom.setter
    def car_showroom(self, value):
        """
        Set the car showroom of the car.

        Args:
            value: The car showroom of the car.
        """
        check_type(value, CarShowroom)
        self._car_showroom = value

    def sell_car(self):
        """
        Sell the car.

        Raises:
            ValueError: If the car is not in the car showroom.
        """
        if self.car_for_sale in self.car_showroom.cars:
            self.car_showroom.remove_car(self.car_for_sale)
            self.owner.add_car(self.car_for_sale)
        else:
            raise ValueError("The car is not in the car showroom.")
