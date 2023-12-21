"""This module contains classes for managing a vehicle fleet."""

from typing import Any, Optional


def check_type(
    input_value: Any, types: tuple[type, ...] | type,
    check_positive: Optional[bool] = False,
) -> None:
    """
    Check if value is of type `types`.

    Args:
        input_value (Any): The value to check.
        types (tuple[type, ...]): The type to check against.
        check_positive (Optional[bool], optional): Check if value is positive. Defaults to False.

    Raises:
        TypeError: If value is not of type `types`.
        ValueError: If value is not positive.
    """
    if not isinstance(input_value, types):
        value_type = type(input_value)
        error_msg = f'Expected type {types}, got {value_type}'
        raise TypeError(error_msg)
    if check_positive and input_value < 0:
        raise ValueError(f'Expected positive value, but got {input_value}')


class Vehicle:
    """Class representing a Vehicle."""

    def __init__(self, model: str, year_of_issue: int, price: int | float) -> None:
        """
        Initialize a Vehicle object.

        Args:
            model (str): The model of the vehicle.
            year_of_issue (int): The year of issue of the vehicle.
            price (int | float): The price of the vehicle in dollars.
        """
        self.model = model
        self.year_of_issue = year_of_issue
        self.price = price

    @property
    def model(self) -> str:
        """
        Return the model of the vehicle.

        Returns:
            str: The model of the vehicle.
        """
        return self._model

    @model.setter
    def model(self, model: str) -> None:
        """
        Set the model of the vehicle.

        Args:
            model (str): The model of the vehicle.
        """
        check_type(model, str)
        self._model = model

    @property
    def year_of_issue(self) -> int:
        """
        Return the year of issue of the vehicle.

        Returns:
            int: The year of issue of the vehicle.
        """
        return self._year_of_issue

    @year_of_issue.setter
    def year_of_issue(self, year_of_issue: int) -> None:
        """
        Set the year of issue of the vehicle.

        Args:
            year_of_issue (int): The year of issue of the vehicle.
        """
        check_type(year_of_issue, int, check_positive=True)
        self._year_of_issue = year_of_issue

    @property
    def price(self) -> int | float:
        """
        Return the price of the vehicle in dollars.

        Returns:
            int | float: The price of the vehicle in dollars.
        """
        return self._price

    @price.setter
    def price(self, price: int | float) -> None:
        """
        Set the price of the vehicle in dollars.

        Args:
            price (int | float): The price of the vehicle in dollars.
        """
        check_type(price, int | float, check_positive=True)
        self._price = price


class Car(Vehicle):
    """Class representing a Car."""

    def __init__(
        self, model: str,
        year_of_issue: int,
        price: int | float,
        passenger_seats: int,
    ) -> None:
        """
        Initialize a Car object.

        Args:
            model (str): The model of the car.
            year_of_issue (int): The year of issue of the car.
            price (int | float): The price of the car in dollars.
            passenger_seats (int): The passenger seats in the car.
        """
        super().__init__(model, year_of_issue, price)
        self.passenger_seats = passenger_seats

    @property
    def passenger_seats(self) -> int:
        """
        Return the passenger seats in the car.

        Returns:
            int: The passenger seats in the car.
        """
        return self._passenger_seats

    @passenger_seats.setter
    def passenger_seats(self, passenger_seats: int) -> None:
        """
        Set the passenger seats in the car.

        Args:
            passenger_seats (int): The passenger seats in the car.
        """
        check_type(passenger_seats, int, check_positive=True)
        self._passenger_seats = passenger_seats


class Truck(Vehicle):
    """Class representing a Truck."""

    def __init__(
        self, model: str,
        year_of_issue: int,
        price: int | float,
        lift_capacity: int | float,
    ) -> None:
        """
        Initialize a Truck object.

        Args:
            model (str): The model of the truck.
            year_of_issue (int): The year of issue of the truck.
            price (int | float): The price of the truck in dollars.
            lift_capacity (int | float): The lifting capacity of the truck in kilograms.
        """
        super().__init__(model, year_of_issue, price)
        self.lift_capacity = lift_capacity

    @property
    def lift_capacity(self) -> int | float:
        """
        Return the lifting capacity of the truck in kilograms.

        Returns:
            int | float: The lifting capacity of the truck in kilograms.
        """
        return self._lift_capacity

    @lift_capacity.setter
    def lift_capacity(self, lift_capacity: int | float) -> None:
        """
        Set the lifting capacity of the truck in kilograms.

        Args:
            lift_capacity (int | float): The lifting capacity of the truck in kilograms.
        """
        check_type(lift_capacity, int | float, check_positive=True)
        self._lift_capacity = lift_capacity


class Parking:
    """Class representing a Parking."""

    def __init__(self, vehicles: list['Vehicle']) -> None:
        """
        Initialize a Parking object.

        Args:
            vehicles (list[Vehicle]): The vehicles on the parking.
        """
        self._vehicles = vehicles

    def add_vehicle(self, new_vehicle: 'Vehicle') -> None:
        """
        Add a new vehicle to the list of vehicles.

        Args:
            new_vehicle (Vehicle): The vehicle to add.

        Raises:
            ValueError: If the vehicle is already in the list of vehicles.
        """
        check_type(new_vehicle, Vehicle)
        if new_vehicle in self.vehicles:
            raise ValueError(f'Vehicle {new_vehicle.model} is already in the list of vehicles')
        self.vehicles.append(new_vehicle)

    def remove_vehicle(self, vehicle: 'Vehicle') -> None:
        """
        Remove a vehicle from the list of vehicles.

        Args:
            vehicle (Vehicle): The vehicle to remove.

        Raises:
            RuntimeError: If the vehicle is not in the list of vehicles.
        """
        if vehicle not in self.vehicles:
            raise RuntimeError(f'Vehicle {vehicle.model} is not in the list of vehicles')
        self.vehicles.remove(vehicle)

    @property
    def vehicles(self) -> None:
        """
        Get a vehicle from the list of vehicles.

        Returns:
            list[Vehicle]: The vehicles on the parking.
        """
        return self._vehicles
