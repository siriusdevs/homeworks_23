class Car:
    """Car instance."""
    def __init__(self, model: str, year_of_vehicle: int, price: int) -> None:
        """Car initialisation.

        Args:
            model: str - car model.
            year_of_the_vehicle: int - cars year of the vehicle.
            price: int - the price of the car.
        """
        self.model = model
        self.year_of_vehicle = year_of_vehicle
        self.price = price

    @property
    def model(self) -> str:
        """Getter of model property.

        Returns:
            str: car model.
        """
        return self._model

    @model.setter
    def model(self, new_model: str) -> None:
        """Setter of model property.

        Args:
            new_model: str - new car model.
        """
        self._model = new_model

    @property
    def year_of_vehicle(self) -> int:
        """Getter of year of the vehicle property of the instance.

        Returns:
            int: year of the vehicle.
        """
        return self._year_of_vehicle

    @year_of_vehicle.setter
    def year_of_vehicle(self, new_year_of_vehicle: int) -> None:
        """Setter of year of the vehicle property of the instance.

        Args:
            new_year_of_vehicle: int - new year of the vehicle.
        """
        self._year_of_vehicle = new_year_of_vehicle

    @property
    def price(self) -> int:
        """Getter of price property of the instance.

        Returns:
            int: price of the car.
        """
        return self._price

    @price.setter
    def price(self, new_price: int) -> int:
        """Setter of price property of the instance.

        Args:
            new_price: int - new price of the car.
        """
        self._price = new_price

    def __str__(self):
        """__str__ method.

        Returns:
            str: model + year of vehicle.
        """
        return self._model + " " + str(self._year_of_vehicle)


class PassengerCar(Car):
    """Passenger car instance."""
    def __init__(self, model: str, year_of_vehicle: int, price: int, passengers: int) -> None:
        """Passenger car initialisation.

        Args:
            model: str - car model.
            year_of_the_vehicle: int - cars year of the vehicle.
            price: int - the price of the car.
            passengers: int - number of passengers.
        """
        Car.__init__(self, model, year_of_vehicle, price)
        self.passengers = passengers

    @property
    def passengers(self) -> int:
        """Getter of car passengers property of the instance.

        Returns:
            int: number of passengers.
        """
        return self._passengers

    @passengers.setter
    def passengers(self, new_passengers: int) -> None:
        """Setter of car passengers property of the instance.

        Args:
            new_passengers: int - number of passengers.
        """
        self._passengers = new_passengers


class Truck(Car):
    """Truck car instance."""
    def __init__(self, model: str, year_of_vehicle: int,
                 price: int, lifting_capacity: int) -> None:
        """Truck initialisation.

        Args:
            model: str - car model.
            year_of_the_vehicle: int - cars year of the vehicle.
            price: int - the price of the car.
            lifting_capacity: int - load capacity of the machine
        """
        Car.__init__(self, model, year_of_vehicle, price)
        self.lifting_capacity = lifting_capacity

    @property
    def lifting_capacity(self) -> int:
        """Getter of lifting capacity property of the instance.

        Returns:
            int: lifting capacity.
        """
        return self._lifting_capacity

    @lifting_capacity.setter
    def lifting_capacity(self, new_lifting_capacity: int) -> None:
        """Setter of lifting capacity property of the instance.

        Args:
            new_lifting_capacity: int - new lifting capacity.
        """
        self._lifting_capacity = new_lifting_capacity


class CarPark:
    """Car park instance."""
    def __init__(self, cars: list((Car, PassengerCar, Truck)) = None) -> None:
        """Car park initialisation.

        Args:
            cars: list[Car or PasengerCar or Truck]: list of cars.
        """
        if cars:
            self._cars = [*cars]
        else:
            self._cars = []

    def add(self, car: (Car, PassengerCar, Truck)) -> None:
        """add car to list of cars.

        Args:
            car: (Car, PassengerCar, Truck) - a new car.
        """
        if isinstance(car, (Car, PassengerCar, Truck)):
            self._cars.append(car)
        else:
            raise TypeError(f'{car}: {type(car).__name__} should be {(Car, PassengerCar, Truck)}')

    def remove(self, car: (Car, PassengerCar, Truck)) -> None:
        """remove car from list of cars.

        Args:
            car: (Car, PassengerCar, Truck) - the car to be deleted.
        """
        if isinstance(car, (Car, PassengerCar, Truck)):
            self._cars.remove(car)
        else:
            raise TypeError(f'{car}: {type(car).__name__} should be {(Car, PassengerCar, Truck)}')

    @property
    def cars(self) -> list((Car, PassengerCar, Truck)):
        """Return list of cars

        Returns:
            list((Car, PassengerCar, Truck)): list of all cars
        """
        return self._cars

    @cars.setter
    def cars(self, cars: list((Car, PassengerCar, Truck))) -> None:
        """Return list of cars

        Returns:
            list((Car, PassengerCar, Truck)): list of all cars
        """
        return self._cars
