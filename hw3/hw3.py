"""class architecture for fleet management."""


class Car:  # noqa: WPS214 (too many methods, but it is according to the task)
    """Class representing a car."""

    def __init__(self, model: str, year: int, cost: float) -> None:
        """Initialize Car object with model, year, and cost.

        Args:
            model (str): The model of the car.
            year (int): The year the car was manufactured.
            cost (float): The cost of the car.
        """
        self.model, self.year, self.cost = model, year, cost

    @property
    def model(self) -> str:
        """Get the model of the car.

        Returns:
            str: The model of the car.
        """
        return self._model

    @model.setter
    def model(self, new_model: str) -> None:
        """Set the model of the car.

        Raises:
            ValueError: If new_model is not a non-empty string.
            TypeError: Model must be an string.

        Args:
            new_model (str): The new model of the car.
        """
        if not isinstance(new_model, str):
            raise TypeError('Model must be an string')
        if not new_model:
            raise ValueError('Model must be a non-empty string')
        self._model = new_model

    @property
    def year(self) -> int:
        """Get the year of manufacture of the car.

        Returns:
            int: The year of manufacture of the car.
        """
        return self._year

    @year.setter
    def year(self, new_year: int) -> None:
        """Set the year of manufacture of the car.

        Args:
            new_year (int): The new year of manufacture of the car.

        Raises:
            TypeError: If new_year is not an integer.
        """
        if not isinstance(new_year, int):
            raise TypeError('Year must be an integer')
        self._year = new_year

    @property
    def cost(self) -> float:
        """Get the cost of the car.

        Returns:
            float: The cost of the car.
        """
        return self._cost

    @cost.setter
    def cost(self, new_cost: float) -> None:
        """Set the cost of the car.

        Args:
            new_cost (float): The new cost of the car.

        Raises:
            TypeError: If new_cost is not a float.
        """
        if not isinstance(new_cost, float):
            raise TypeError('Cost must be a float')
        self._cost = new_cost

    def __str__(self) -> str:
        """Magic method str.

        Returns:
            str.
        """
        return f'{self.model}, {self.year}, {self.cost}'


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
        self.passenger_seats = passenger_seats

    @property
    def passenger_seats(self) -> int:
        """Get the number of passenger seats in the car.

        Returns:
            int: The number of passenger seats in the car.
        """
        return self._passenger_seats

    @passenger_seats.setter
    def passenger_seats(self, new_passenger_seats: int) -> None:
        """Set the number of passenger seats in the car.

        Args:
            new_passenger_seats (int): The new number of passenger seats in the car.

        Raises:
            TypeError: If new_passenger_seats is not an integer.
        """
        if not isinstance(new_passenger_seats, int):
            raise TypeError('Passenger seats must be an integer')
        self._passenger_seats = new_passenger_seats


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
        self.carrying_capacity = carrying_capacity

    @property
    def carrying_capacity(self) -> float:
        """Get the carrying capacity of the truck.

        Returns:
            float: The carrying capacity of the truck.
        """
        return self._carrying_capacity

    @carrying_capacity.setter
    def carrying_capacity(self, new_carrying_capacity: float) -> None:
        """Set the carrying capacity of the truck.

        Args:
            new_carrying_capacity (float): The new carrying capacity of the truck.

        Raises:
            TypeError: If new_carrying_capacity is not a float.
        """
        if not isinstance(new_carrying_capacity, float):
            raise TypeError('Carrying capacity must be a float')
        self._carrying_capacity = new_carrying_capacity


class CarPark:
    """Class representing a car park."""

    def __init__(self) -> None:
        """Initialize an empty CarPark object."""
        self._cars = []

    def add_car(self, car: Car) -> None:
        """Add a car to the car park.

        Args:
            car (Car): The car to be added to the car park.

        Raises:
            TypeError: If the provided object is not an instance of Car or its subclasses.
        """
        if not isinstance(car, (Car, PassengerCar, Truck)):
            raise TypeError('The provided object is not a Car or its subclass')
        self.cars = self.cars + [car]

    def remove_car(self, car: Car) -> None:
        """Remove a car from the car park.

        Args:
            car (Car): The car to be removed from the car park.

        Raises:
            ValueError: If the provided car is not in the car park.
        """
        if car not in self._cars:
            raise ValueError('Car not found in the car park')
        self.cars = [ca for ca in self.cars if ca != car]

    def get_all_cars(self) -> list[Car]:
        """Get a list of all cars in the car park.

        Returns:
            list[Car]: A list of all cars in the car park.
        """
        return self._cars

    @property
    def cars(self) -> list:
        """Get the list of cars in the car park.

        Returns:
            list: The list of cars in the car park.
        """
        return self._cars

    @cars.setter
    def cars(self, new_cars: list) -> None:
        """Set the list of cars in the car park.

        Args:
            new_cars (list): The new list of cars in the car park.

        Raises:
            TypeError: If the provided object is not a list.
        """
        if not isinstance(new_cars, list):
            raise TypeError('Cars must be a list')
        self._cars = new_cars
