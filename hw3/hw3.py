"""Main module."""
from abc import ABC, abstractmethod
from typing import Optional


class NegativeNumberError(ValueError):
    """Error for negative numbers."""

    def __init__(self, new_value):
        """Init Error.

        Args:
            new_value (any): negative number
        """
        super().__init__(f'{new_value} should be more than zero')


class InvalidTypeError(TypeError):
    """Error for wrong type."""

    def __init__(self, new_value, _type: str):
        """Init Error.

        Args:
            new_value (any): incorrect value
            _type (str): type of correct value
        """
        super().__init__(f'{new_value} is not a {_type}')


class Car(ABC):
    """Car with details."""

    @abstractmethod
    def __init__(self, model: str, year: int, price: int) -> None:
        """Init Car.

        Args:
            model (str): car type
            year (int): car creation date
            price (int): price of a car
        """
        self.model, self.year, self.price = model, year, price

    @property
    def model(self) -> str:
        """Get model of the car.

        Returns:
            str: model of the car
        """
        return self._model

    @model.setter
    def model(self, new_model: str) -> None:
        """Set new model for the car.

        Args:
            new_model (str): model of the car

        Raises:
            InvalidTypeError: If given model is not a string
        """
        if not isinstance(new_model, str):
            raise InvalidTypeError(new_model, 'str')
        self._model = new_model

    @property
    def year(self) -> int:
        """Get year of the car.

        Returns:
            int: year of the car
        """
        return self._year

    @year.setter
    def year(self, new_year: int) -> None:
        """Set new year for the car.

        Args:
            new_year (int): year for the car

        Raises:
            NegativeNumberError: If given year is less than zero
            InvalidTypeError: If given year is not a number
        """
        if new_year <= 0:
            raise NegativeNumberError(new_year)
        if not isinstance(new_year, int):
            raise InvalidTypeError(new_year, 'int')
        self._year = new_year

    @property
    def price(self) -> int:
        """Get price of the car.

        Returns:
            int: price of the car
        """
        return self._price

    @price.setter
    def price(self, new_price: int) -> None:
        """Set new price for the car.

        Args:
            new_price (int): price of the car

        Raises:
            NegativeNumberError: If given price is less than zero
            InvalidTypeError: If given price is not a number
        """
        if new_price <= 0:
            raise NegativeNumberError(new_price)
        if not isinstance(new_price, int):
            raise InvalidTypeError(new_price, 'int')
        self._price = new_price

    def __str__(self) -> str:
        """Get string presentation for car.

        Returns:
            str: model of the car
        """
        return f'{self._model}'


class Motorcar(Car):
    """Motorcar model."""

    def __init__(self, model: str, year: int, price: int, seats: int) -> None:
        """Init Motorcar.

        Args:
            model (str): car type
            year (int): car creation date
            price (int): price of a car
            seats (int): seats of the car
        """
        super().__init__(model, year, price)
        self.seats = seats

    @property
    def seats(self) -> int:
        """Get seats of the car.

        Returns:
            int: seats of the car.
        """
        return self._seats

    @seats.setter
    def seats(self, new_seats: int) -> None:
        """Set new seats for the car.

        Args:
            new_seats (int): seats of the car

        Raises:
            NegativeNumberError: If given seats is less than zero
            InvalidTypeError: If given seats is not a number
        """
        if new_seats <= 0:
            raise NegativeNumberError(new_seats)
        if not isinstance(new_seats, int):
            raise InvalidTypeError(new_seats, 'int')
        self._seats = new_seats


class CargoCar(Car):
    """CargoCar model."""

    def __init__(self, model: str, year: int, price: int, payload: int) -> None:
        """Init CargoCar.

        Args:
            model (str): car type
            year (int): car creation date
            price (int): price of a car
            payload (int): payload of the car
        """
        super().__init__(model, year, price)
        self.payload = payload

    @property
    def payload(self) -> int:
        """Get payload of the car.

        Returns:
            int: payload of the car.
        """
        return self._payload

    @payload.setter
    def payload(self, new_payload: int | float) -> None:
        """Set new payload for the car.

        Args:
            new_payload (int): payload for the car

        Raises:
            NegativeNumberError: If given payload is less than zero
            InvalidTypeError: If given payload is not a number
        """
        if new_payload <= 0:
            raise NegativeNumberError(new_payload)
        if not isinstance(new_payload, (int, float)):
            raise InvalidTypeError(new_payload, 'number')
        self._payload = new_payload


class AutoPark:
    """AutoPark with cars."""

    def __init__(self, cars: Optional[list[Car]] = None) -> None:
        """Init AutoPark.

        Args:
            cars (list[Car], optional): list with car. Defaults to None.
        """
        self.cars = cars if cars else []

    @property
    def cars(self) -> list[Car]:
        """Get cars from AutoPark.

        Returns:
            list[Car]: cars from AutoPark
        """
        return [str(car) for car in self._cars]

    @cars.setter
    def cars(self, new_cars: list[Car]) -> None:
        """Set cars in AutoPark.

        Args:
            new_cars (list[Car]): car in AutoPark

        Raises:
            TypeError: If given cars is not array
            TypeError: If given car is not car
        """
        if not isinstance(new_cars, list):
            raise TypeError(f'{new_cars} is not array')
        for car in new_cars:
            if not isinstance(car, Car):
                raise TypeError(f'{car} is not a Car')
        self._cars = new_cars

    def add_car(self, car) -> None:
        """Add car in AutoPark.

        Args:
            car (Car): car for AutoPark

        Raises:
            TypeError: If given car is not car
        """
        if not isinstance(car, Car):
            raise TypeError(f'{car} is not a Car')
        self._cars.append(car)

    def remove_car(self, car) -> None:
        """Remove car in AutoPark.

        Args:
            car (Car): car for AutoPark

        Raises:
            TypeError: If given car is not car
            ValueError: If given car not not found in AutoPark
        """
        if not isinstance(car, Car):
            raise TypeError(f'{car} is not a Car')
        if car not in self._cars:
            raise ValueError(f'{car} not found in AutoPark')
        self._cars.remove(car)
