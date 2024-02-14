"""Module that provides classes for hw3."""


class Car:
    """Car instance."""

    def __init__(self, model: str, year_of_vehicle: int, price: int | float) -> None:
        """Car initialization.

        Args:
            model (str): car model
            year_of_vehicle (int): cars year of the vehicle.
            price (int | float): the price of the car
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
            new_year_of_vehicle (int): new year of the vehicle

        Raises:
            TypeError: if new value have wrong type
            ValueError: if new value less than zero
        """
        if not isinstance(new_year_of_vehicle, int):
            raise TypeError('Given wrong type for new_year_of_vehicle')
        if new_year_of_vehicle < 0:
            raise ValueError('Less zero!')
        self._year_of_vehicle = new_year_of_vehicle

    @property
    def price(self) -> int:
        """Getter of price property of the instance.

        Returns:
            int: price of the car.
        """
        return self._price

    @price.setter
    def price(self, new_price: int | float) -> None:
        """Setter of price property of the instance.

        Args:
            new_price (int): new price of the car.

        Raises:
            TypeError: if new value have wrong type
            ValueError: if new value less than zero
        """
        if not isinstance(new_price, (int | float)):
            raise TypeError('Given wrong type for new_price')
        if new_price < 0:
            raise ValueError('Less zero!')
        self._price = new_price

    def __str__(self):
        """__str__ method.

        Returns:
            str: model + year of vehicle.
        """
        return f'{self._model} {str(self._year_of_vehicle)}'


class PassengerCar(Car):
    """Passenger car instance."""

    def __init__(
        self,
        model: str,
        year_of_vehicle: int,
        price: int | float,
        passengers: int,
    ) -> None:
        """Passenger car initialization.

        Args:
            model (str): car model
            year_of_vehicle (int): cars year of the vehicle
            price (int | float): the price of the car
            passengers (int): number of passengers
        """
        super().__init__(self, model, year_of_vehicle, price)
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

    def __init__(
        self,
        model: str,
        year_of_vehicle: int,
        price: int,
        lifting_capacity: int | float,
    ) -> None:
        """Truck initialization.

        Args:
            model (str): car model
            year_of_vehicle (int): cars year of the vehicle
            price (int): the price of the car
            lifting_capacity (int | float): number of passangers
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
            new_lifting_capacity (int): new lifting capacity

        Raises:
            TypeError: if new value have wrong type
            ValueError: if new value less than zero
        """
        if not isinstance(new_lifting_capacity, (int | float)):
            raise TypeError('Given wrong type for new_lifting_capacity')
        if new_lifting_capacity < 0:
            raise ValueError('Less zero!')
        self._lifting_capacity = new_lifting_capacity


class CarPark:
    """Car park instance."""

    def __init__(self, cars: list[Car] = None) -> None:
        """Car park initialisation.

        Args:
            cars: list[Car or PasengerCar or Truck]: list of cars.
        """
        self._cars = cars

    def add(self, car: Car) -> None:
        """Add car to list of cars.

        Args:
            car: (Car, PassengerCar, Truck) - a new car.

        Raises:
            TypeError: if given wrong type
        """
        if isinstance(car, (Car, PassengerCar, Truck)):
            self._cars.append(car)
        else:
            raise TypeError(
                f'{car}: {type(car).__name__} should be {(Car, PassengerCar, Truck)}')

    def remove(self, car: Car) -> None:
        """Remove car from list of cars.

        Args:
            car: (Car, PassengerCar, Truck) - the car to be deleted.

        Raises:
            TypeError: if given wrong type
        """
        if not isinstance(car, (Car, PassengerCar, Truck)):
            raise TypeError(
                f'{car}: {type(car).__name__} should be {(Car, PassengerCar, Truck)}')
        if car in self.cars:
            self._cars.remove(car)

    @property
    def cars(self) -> list[Car]:
        """Return list of cars.

        Returns:
            list((Car, PassengerCar, Truck)): list of all cars
        """
        return self._cars

    @cars.setter
    def cars(self, cars: list[Car]) -> None:
        """Setter for cars.

        Args:
            cars (list[Car]): list of cars

        Raises:
            TypeError: if was given not list
            TypeError: if was given not car
        """
        if not isinstance(cars, list):
            raise TypeError('Given wrong type for cars')
        for car in cars:
            if not isinstance(car, (Car, PassengerCar, Truck)):
                raise TypeError('Given wrong type for car in new cars')
        self._cars = cars
