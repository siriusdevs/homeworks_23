"""Class architecture for fleet management."""

class Car:
    """Class representing a car."""

    def __init__(self, model: str, year: int, cost: float) -> None:
        """Initialize Car object with model, year, and cost."""
        if not isinstance(model, str):
            raise TypeError('Model must be a string')
        if not model:
            raise ValueError('Model cannot be empty')
        if not isinstance(year, int):
            raise TypeError('Year must be an integer')
        if not isinstance(cost, float):
            raise TypeError('Cost must be a float')
            
        self._model, self._year, self._cost = model, year, cost

    @property
    def model(self) -> str:
        """Get the model of the car."""
        return self._model

    @model.setter
    def model(self, new_model: str) -> None:
        """Set the model of the car."""
        if not isinstance(new_model, str):
            raise TypeError('Model must be a string')
        if not new_model:
            raise ValueError('Model cannot be empty')
        self._model = new_model

    @property
    def year(self) -> int:
        """Get the year of manufacture of the car."""
        return self._year

    @year.setter
    def year(self, new_year: int) -> None:
        """Set the year of manufacture of the car."""
        if not isinstance(new_year, int):
            raise TypeError('Year must be an integer')
        self._year = new_year

    @property
    def cost(self) -> float:
        """Get the cost of the car."""
        return self._cost

    @cost.setter
    def cost(self, new_cost: float) -> None:
        """Set the cost of the car."""
        if not isinstance(new_cost, float):
            raise TypeError('Cost must be a float')
        self._cost = new_cost

    def __str__(self) -> str:
        return f'{self.model}, {self.year}, {self.cost}'

class PassengerCar(Car):
    """Class representing a passenger car, inherited from Car."""

    def __init__(self, model: str, year: int, cost: float, passenger_seats: int) -> None:
        """Initialize PassengerCar object with model, year, cost, and passenger seats."""
        super().__init__(model, year, cost)
        if not isinstance(passenger_seats, int):
            raise TypeError('Passenger seats must be an integer')
        self._passenger_seats = passenger_seats

    @property
    def passenger_seats(self) -> int:
        """Get the number of passenger seats in the car."""
        return self._passenger_seats

    @passenger_seats.setter
    def passenger_seats(self, new_passenger_seats: int) -> None:
        """Set the number of passenger seats in the car."""
        if not isinstance(new_passenger_seats, int):
            raise TypeError('Passenger seats must be an integer')
        self._passenger_seats = new_passenger_seats


class Truck(Car):
    """Class representing a truck, inherited from Car."""

    def __init__(self, model: str, year: int, cost: float, carrying_capacity: float) -> None:
        """Initialize Truck object with model, year, cost, and carrying capacity."""
        super().__init__(model, year, cost)
        if not isinstance(carrying_capacity, float):
            raise TypeError('Carrying capacity must be a float')
        self._carrying_capacity = carrying_capacity

    @property
    def carrying_capacity(self) -> float:
        """Get the carrying capacity of the truck."""
        return self._carrying_capacity

    @carrying_capacity.setter
    def carrying_capacity(self, new_carrying_capacity: float) -> None:
        """Set the carrying capacity of the truck."""
        if not isinstance(new_carrying_capacity, float):
            raise TypeError('Carrying capacity must be a float')
        self._carrying_capacity = new_carrying_capacity


class CarPark:
    """Class representing a car park."""

    def __init__(self) -> None:
        """Initialize an empty CarPark object."""
        self._cars = []

    def add_car(self, car: Car) -> None:
        """Add a car to the car park."""
        self._cars.append(car)

    def remove_car(self, car: Car) -> None:
        """Remove a car from the car park."""
        self._cars.remove(car)

    def get_all_cars(self) -> list[Car]:
        """Get a list of all cars in the car park."""
        return self._cars
