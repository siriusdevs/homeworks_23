"""Учет транспортных средств на автомобильной парковке.

Опишем архитектуру классов для учета транспортных средств на автомобильной парковке.
В этом задании также будут использованы наследование, инкапсуляция и агрегация.

Класс "Транспортное средство":
Поля:
Марка транспортного средства
Номерной знак транспортного средства
Методы:
Геттеры и сеттеры для полей

Класс "Автомобиль", наследуется от класса "Транспортное средство":
Поля:
Тип кузова (седан, хэтчбек и т.д.)
Методы:
Геттеры и сеттеры для полей

Класс "Парковка":
Поля:
Список транспортных средств на парковке (массив или список объектов класса "Транспортное средство")
Вместимость парковки (максимальное количество транспортных средств)
Методы:
Геттеры и сеттеры для полей
Добавить транспортное средство на парковку
Удалить транспортное средство с парковки
Получить количество свободных мест на парковке
Получить список всех транспортных средств на парковке
"""


def check_type(var_name, var_value, expected_type) -> None:
    """Check variable type.

    Args:
        var_name: str - variable name.
        var_value: Any - variable value.
        expected_type: tuple[Any] | Any - expected type of variable.

    Raises:
        TypeError: if type of variable is different from expected.
    """
    if not isinstance(var_value, expected_type):
        raise TypeError(f'{var_name}: {type(var_value).__name__} should be {expected_type}')


class Vehicle:
    """Vehicle instance."""

    def __init__(self, mark: str, license_plate: int) -> None:
        """Vehicle initialisation.

        Args:
            mark: str - mark of vehicle.
            license_plate: int - license plate of vehicle.
        """
        self.mark = mark
        self.license_plate = license_plate

    @property
    def mark(self) -> str:
        """Getter of mark property of the instance.

        Returns:
            str: mark of the vehicle.
        """
        return self._mark

    @mark.setter
    def mark(self, new_mark: str) -> None:
        """Setter of mark property of the instance.

        Args:
            new_mark: str - new mark of vehicle.
        """
        check_type('mark', new_mark, str)
        self._mark = new_mark

    @property
    def license_plate(self) -> int:
        """Getter of license plate property of the instance.

        Returns:
            int: license plate of vehicle.
        """
        return self._license_plate

    @license_plate.setter
    def license_plate(self, new_lp: int) -> None:
        """Setter of license plate property of the instance.

        Args:
            new_lp: int - new license plate of vehicle.
        """
        check_type('license', new_lp, int)
        self._license_plate = new_lp

    def __str__(self) -> str:
        """Representation of the instance in string.

        Returns:
            str: string visualisation of the instance.
        """
        return f'{self.__class__.__name__} {self.mark} {self.license_plate}'


class Car(Vehicle):
    """Car instance."""

    def __init__(self, mark: str, license_plate: int, body: str) -> None:
        """Car initialisation.

        Args:
            mark: str - mark of the car.
            license_plate: int - license plate of the car
            body: str - car body.
        """
        super().__init__(mark, license_plate)
        self.body = body

    @property
    def body(self) -> str:
        """Getter of car body property of the instance.

        Returns:
            str: car body.
        """
        return self._body

    @body.setter
    def body(self, new_body: str) -> None:
        """Setter of car body property of the instance.

        Args:
            new_body: str - new car body.
        """
        check_type('car body', new_body, str)
        self._body = new_body


class ParkingMethods:
    """Parking methods."""

    def add_vehicle(self, new_vehicle: Vehicle) -> None:
        """Add one vehicle to the list with vehicles.

        Args:
            new_vehicle: Vehicle - new vehilce.
        """
        check_type('Vehicle', new_vehicle, Vehicle)
        if len(self._vehicles) < self._max_amount:
            self._vehicles.append(new_vehicle)

    def remove_vehicle(self, vehicle: Vehicle) -> None:
        """Remove one vehicle from the list with vehicles.

        Args:
            vehicle: Vehicle - vehicle that was given.

        Raises:
            ValueError: if there is not this vehicle in the list.
        """
        check_type('Vehicle', vehicle, Vehicle)
        if vehicle not in self._vehicles:
            raise ValueError(f'There is not vehicle {vehicle}')
        self._vehicles.remove(vehicle)

    def free_places(self) -> int:
        """Return the number of free parking spaces.

        Returns:
            int: free parking spaces.
        """
        return self.max_amount - len(self.vehicles)

    def vehicles_lst(self) -> list[Vehicle]:
        """Return the list with vehicles on the parking.

        Returns:
            list[Vehicle]: vehicles on the parking.
        """
        return f'Vehicles on parking: {self._vehicles}'


class Parking(ParkingMethods):
    """Parking instance."""

    def __init__(self, vehicles: list[Vehicle], max_amount: int) -> None:
        """Parking initialisation.

        Args:
            vehicles: list[Vehicle] - list with vehilces.
            max_amount: int - maximum amount of vehicles.
        """
        self.max_amount = max_amount
        self.vehicles = vehicles

    @property
    def max_amount(self) -> int:
        """Getter of maximum amount property of the instance.

        Returns:
            int: maximum amount of vehicles.
        """
        return self._max_amount

    @max_amount.setter
    def max_amount(self, new_max: int) -> None:
        """Setter of maximum amount property of the instance.

        Args:
            new_max: int - new maximum amount of vehicles.
        """
        check_type('maximum amount', new_max, int)
        self._max_amount = new_max

    @property
    def vehicles(self) -> list[Vehicle]:
        """Getter of vehicles property of the instance.

        Returns:
            list[Vehicle]: list with vehicles.
        """
        return self._vehicles

    @vehicles.setter
    def vehicles(self, new_vehicles: list[Vehicle]) -> None:
        """Setter of vehicles property of the instance.

        Args:
            new_vehicles: list[Vehicle] - list with new vehicles.

        Raises:
            ValueError: if length of new list with vehicles is bigger than maximum.
        """
        check_type('Vehicles', new_vehicles, list | tuple)
        if len(new_vehicles) > self.max_amount:
            raise ValueError('More vehicle than maximum')
        for veh in new_vehicles:
            check_type('Vehicle', veh, Vehicle)
        self._vehicles = new_vehicles
