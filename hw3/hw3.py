"""A module for fleet management"""
class Car:
    """Class representing a car."""

    def __init__(self, model: str, year: int, cost: float) -> None:
        """Initialize Car object with model, year, and cost.

        Args:
            model (str): The model of the car.
            year (int): The year the car was manufactured.
            cost (float): The cost of the car.
        """
        self._model, self._year, self._cost = model, year, cost

    @property
    def model(self) -> str:
        """Get the model of the car.

        Returns:
            str: The model of the car.
        """
        return self._model

    @model.setter
    def model(self, value: str) -> None:
        """Set the model of the car.

        Args:
            value (str): The new model of the car.

        Raises:
            TypeError: If value is not a string.
        """
        if not isinstance(value, str):
            raise TypeError("Model must be a string")
        self._model = value

    @property
    def year(self) -> int:
        """Get the year of manufacture of the car.

        Returns:
            int: The year of manufacture of the car.
        """
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        """Set the year of manufacture of the car.

        Args:
            value (int): The new year of manufacture of the car.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("Year must be an integer")
        self._year = value

    @property
    def cost(self) -> float:
        """Get the cost of the car.

        Returns:
            float: The cost of the car.
        """
        return self._cost

    @cost.setter
    def cost(self, value: float) -> None:
        """Set the cost of the car.

        Args:
            value (float): The new cost of the car.

        Raises:
            TypeError: If value is not a float.
        """
        if not isinstance(value, float):
            raise TypeError("Cost must be a float")
        self._cost = value


class PassengerCar(Car):
    """Class representing a passenger car, inherited from Car."""

    def __init__(self, model: str, year: int, cost: float, passenger_seats: int) -> None:
        """Initialize PassengerCar object with model, year, cost, and passenger seats.

        Args:
            model (str): The model of the car.
            year (int): The year the car was manufactured.
            cost (float): The cost of the car.
            passenger_seats (int): The number of passenger seats in the car.
        """
        super().__init__(model, year, cost)
        self._passenger_seats = passenger_seats

    @property
    def passenger_seats(self) -> int:
        """Get the number of passenger seats in the car.

        Returns:
            int: The number of passenger seats in the car.
        """
        return self._passenger_seats

    @passenger_seats.setter
    def passenger_seats(self, value: int) -> None:
        """Set the number of passenger seats in the car.

        Args:
            value (int): The new number of passenger seats in the car.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("Passenger seats must be an integer")
        self._passenger_seats = value


class Truck(Car):
    """Class representing a truck, inherited from Car."""

    def __init__(self, model: str, year: int, cost: float, carrying_capacity: float) -> None:
        """Initialize Truck object with model, year, cost, and carrying capacity.

        Args:
            model (str): The model of the truck.
            year (int): The year the truck was manufactured.
            cost (float): The cost of the truck.
            carrying_capacity (float): The carrying capacity of the truck.
        """
        super().__init__(model, year, cost)
        self._carrying_capacity = carrying_capacity

    @property
    def carrying_capacity(self) -> float:
        """Get the carrying capacity of the truck.

        Returns:
            float: The carrying capacity of the truck.
        """
        return self._carrying_capacity

    @carrying_capacity.setter
    def carrying_capacity(self, value: float) -> None:
        """Set the carrying capacity of the truck.

        Args:
            value (float): The new carrying capacity of the truck.

        Raises:
            TypeError: If value is not a float.
        """
        if not isinstance(value, float):
            raise TypeError("Carrying capacity must be a float")
        self._carrying_capacity = value


class CarPark:
    """Class representing a car park."""

    def __init__(self) -> None:
        """Initialize an empty CarPark object."""
        self._cars = []

    def add_car(self, car: Car) -> None:
        """Add a car to the car park.

        Args:
            car (Car): The car to be added to the car park.
        """
        self._cars.append(car)

    def remove_car(self, car: Car) -> None:
        """Remove a car from the car park.

        Args:
            car (Car): The car to be removed from the car park.
        """
        self._cars.remove(car)

    def get_all_cars(self) -> list[Car]:
        """Get a list of all cars in the car park.

        Returns:
            list[Car]: A list of all cars in the car park.
        """
        return self._cars
