"""HW3."""
from abc import ABC, abstractmethod
from typing import Any


def check_type(new_value: Any, correct_type: type[Any]):
    """Check object type.

    Args:
        new_value: value to check type
        correct_type: correct type for value

    Raises:
        TypeError: if the value type is wrong, there will be an error with the text
    """
    if not isinstance(new_value, correct_type):
        value_type = type(new_value).__name__
        raise TypeError(f'{new_value} must be {correct_type.__name__}, not {value_type}')


class Car(ABC):
    """Abstract class for different car type."""

    @abstractmethod
    def __init__(self, model: str, year: int, price: float) -> None:
        """Car initialization.

        Args:
            model: the model of car
            year: year of manufacture of the car
            price: car cost
        """
        self.model, self.year, self.price = model, year, price

    @property
    def model(self) -> str:
        """Getter for car model property.

        Returns:
            car model - str
        """
        return self._model

    @model.setter
    def model(self, new_model: str):
        """Setter for car model property.

        Args:
            new_model: new value for model
        """
        check_type(new_model, str)
        self._model = new_model

    @property
    def year(self) -> int:
        """Getter for car year property.

        Returns:
            car year - int
        """
        return self._year

    @year.setter
    def year(self, new_year: int):
        """Setter for car year property.

        Args:
            new_year: new value for year
        """
        check_type(new_year, int)
        self._year = new_year

    @property
    def price(self) -> float:
        """Getter for car price property.

        Returns:
            car price - float
        """
        return self._price

    @price.setter
    def price(self, new_price: float):
        """Setter for car price property.

        Args:
            new_price: new value for price
        """
        check_type(new_price, float)
        self._price = new_price

    def __str__(self) -> str:
        """Representation to string.

        Returns:
            class name, model, year and price of car
        """
        class_name = self.__class__.__name__
        return f'{class_name} model={self.model}, year={self.year}, price={self.price}'


class PassengerCar(Car):
    """Class for passenger car."""

    def __init__(self, model: str, year: int, price: float, seats: int) -> None:
        """Passenger car initialization.

        Args:
            model: the model of car
            year: year of manufacture of the car
            price: car cost
            seats: number of seats for passengers
        """
        super().__init__(model, year, price)
        self.seats = seats

    @property
    def seats(self) -> int:
        """Getter for passenger car seats property.

        Returns:
            passenger car seats - int
        """
        return self._seats

    @seats.setter
    def seats(self, new_seats: int):
        """Setter for passenger car seats property.

        Args:
            new_seats: new value for seats
        """
        check_type(new_seats, int)
        self._seats = new_seats


class FreightCar(Car):
    """Class for freight car."""

    def __init__(self, model: str, year: int, price: float, lifting_capacity: int) -> None:
        """Freight car initialization.

        Args:
            model: the model of car
            year: year of manufacture of the car
            price: car cost
            lifting_capacity: lifting capacity freight car
        """
        super().__init__(model, year, price)
        self.lifting_capacity = lifting_capacity

    @property
    def lifting_capacity(self) -> int:
        """Getter for freight car lifting capacity property.

        Returns:
            freight car lifting capacity - int
        """
        return self._lifting_capacity

    @lifting_capacity.setter
    def lifting_capacity(self, new_lifting_capacity: int):
        """Setter for freight car lifting capacity property.

        Args:
            new_lifting_capacity: new value for lifting capacity
        """
        check_type(new_lifting_capacity, int)
        self._lifting_capacity = new_lifting_capacity


class CarPark:
    """Class for park of cars."""

    def __init__(self, cars: list[Car]) -> None:
        """Car Park initialization.

        Args:
            cars: list of all cars
        """
        self.cars = cars

    def add(self, new_car: Car) -> None:
        """Add a car.

        Args:
            new_car: new value for Car
        """
        check_type(new_car, Car)
        self.cars.append(new_car)

    def remove(self, new_car: Car) -> None:
        """Remove a car.

        Args:
            new_car: new value for Car

        Raises:
            ValueError: if you delete a car that is not in the list it will give an error
        """
        check_type(new_car, Car)
        if new_car not in self.cars:
            raise ValueError('The car you want to delete is not in the list')
        self.cars.remove(new_car)

    def get_all(self) -> list[Car]:
        """Get all cars in car park.

        Returns:
            all cars in car park - list of car type
        """
        return self.cars
