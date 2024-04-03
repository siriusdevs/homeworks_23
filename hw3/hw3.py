class Car:
    def __init__(self, model: str, year: int, cost: float) -> None:
        self._model = model
        self._year = year
        self._cost = cost

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Model must be a string")
        self._model = value

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Year must be an integer")
        self._year = value

    @property
    def cost(self) -> float:
        return self._cost

    @cost.setter
    def cost(self, value: float) -> None:
        if not isinstance(value, float):
            raise TypeError("Cost must be a float")
        self._cost = value


class PassengerCar(Car):
    def __init__(self, model: str, year: int, cost: float, passenger_seats: int) -> None:
        super().__init__(model, year, cost)
        self._passenger_seats = passenger_seats

    @property
    def passenger_seats(self) -> int:
        return self._passenger_seats

    @passenger_seats.setter
    def passenger_seats(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Passenger seats must be an integer")
        self._passenger_seats = value


class Truck(Car):
    def __init__(self, model: str, year: int, cost: float, carrying_capacity: float) -> None:
        super().__init__(model, year, cost)
        self._carrying_capacity = carrying_capacity

    @property
    def carrying_capacity(self) -> float:
        return self._carrying_capacity

    @carrying_capacity.setter
    def carrying_capacity(self, value: float) -> None:
        if not isinstance(value, float):
            raise TypeError("Carrying capacity must be a float")
        self._carrying_capacity = value


class CarPark:
    def __init__(self) -> None:
        self._cars = []

    def add_car(self, car: Car) -> None:
        self._cars.append(car)

    def remove_car(self, car: Car) -> None:
        self._cars.remove(car)

    def get_all_cars(self) -> list[Car]:
        return self._cars

