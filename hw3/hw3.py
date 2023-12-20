"""Module that keeps records of vehicles in the parking lot."""
from typing import Any


def check_type(elem: Any, _class: Any) -> None:
    """Check type of elements.

    Args:
        elem (Any): Element.
        _class (Any): Class that the element should have.

    Raises:
        TypeError: If the class of the elem and the _class do not converge.
    """
    value_class = type(elem).__name__
    classname = _class.__name__
    if not isinstance(elem, _class):
        raise TypeError(f'{elem} of {value_class} should be as {classname}')


class Vehicle:
    """A Vehicle that containing label and license plate."""

    def __init__(self, label: str, license_plate: str) -> None:
        """Label, license plate of vehicle.

        Args:
            label (str): Label of vehicle.
            license_plate (str): License plate of vehicle.
        """
        self.label, self.license_plate = label, license_plate

    @property
    def label(self) -> str:
        """A label of vehicle.

        Returns:
            str: Label of vehicle.
        """
        return self._label

    @label.setter
    def label(self, new_label: str) -> None:
        """Set a new label.

        Args:
            new_label (str): New label.
        """
        check_type(new_label, str)
        self._label = new_label

    @property
    def license_plate(self) -> str:
        """A license plate of vehicle.

        Returns:
            str: License plate of vehicle.
        """
        return self._license_plate

    @license_plate.setter
    def license_plate(self, new_l_p: str) -> None:
        """Set a new license plate.

        Args:
            new_l_p (str): New license plate.
        """
        check_type(new_l_p, str)
        self._license_plate = new_l_p

    def __str__(self) -> str:
        """Str representation of an object.

        Returns:
            str: String representation.
        """
        vehicle_info = [self.label, self.license_plate]
        classname = self.__class__.__name__
        return f'{classname} with {vehicle_info}'


class Car(Vehicle):
    """Car that is inherited from a Vehicle."""

    def __init__(self, label: str, license_plate: str, car_body: str) -> None:
        """Label, license plate, title of car body.

        Args:
            label (str): Label of vehicle.
            license_plate (str): License plate.
            car_body (str): Title of car body.
        """
        self.car_body = car_body
        super().__init__(label, license_plate)

    @property
    def car_body(self) -> str:
        """A title of car body.

        Returns:
            str: Title of car body.
        """
        return self._car_body

    @car_body.setter
    def car_body(self, new_car_body: str) -> None:
        """Set new title of car body.

        Args:
            new_car_body (str): New title of car body.
        """
        check_type(new_car_body, str)
        self._car_body = new_car_body

    def __str__(self) -> str:
        """Str representation of an object.

        Returns:
            str: String representation.
        """
        car_info = [self.label, self.license_plate, self.car_body]
        classname = self.__class__.__name__
        return f'{classname} {car_info}'


class Parking:
    """Parking space for vehicle."""

    def __init__(self, list_of_vehicles: list[Vehicle], capacity: int) -> None:
        """List of vehicles, parking capacity.

        Args:
            list_of_vehicles (list[Vehicle]): List of vehicles in the parking lot.
            capacity (int): Parking capacity.
        """
        self.capacity, self.list_of_vehicles = capacity, list_of_vehicles

    @property
    def capacity(self) -> int:
        """A parking capacity.

        Returns:
            int: Parking capacity.
        """
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity: int) -> None:
        """Set new parking capacity.

        Args:
            new_capacity (int): New capacity.
        """
        check_type(new_capacity, int)
        self._capacity = new_capacity

    @property
    def list_of_vehicles(self) -> list[Vehicle]:
        """A list of vehicles.

        Returns:
            list[Vehicle]: List of vehicles.
        """
        return self._list_of_vehicles

    @list_of_vehicles.setter
    def list_of_vehicles(self, new_l_o_v: list[Vehicle]) -> None:
        """Set list of vehicles.

        Args:
            new_l_o_v (list[Vehicle]): New list of vehicles.

        Raises:
            ValueError: If list of vehicles exceeds parking capacity.
        """
        check_type(new_l_o_v, list)
        if len(new_l_o_v) > self._capacity:
            raise ValueError('List of vehicles must be less than capacity')
        for vehicle in new_l_o_v:
            check_type(vehicle, Vehicle)
        self._list_of_vehicles = new_l_o_v

    def add_vehicle(self, new_vehicle: Vehicle) -> None:
        """Add vehicle into list of vehicles.

        Args:
            new_vehicle (Vehicle): New list of vehicles.

        Raises:
            ValueError: If no parking space for vehicle.
        """
        check_type(new_vehicle, Vehicle)
        if len(self.list_of_vehicles) + 1 > self.capacity:
            raise ValueError(f'There is no parking space for a vehicle {new_vehicle}')
        self.list_of_vehicles.append(new_vehicle)

    def remove_vehicle(self, vehicle: Vehicle):
        """Remove vehicle from list of vehicles.

        Args:
            vehicle (Vehicle): Vehicle, that can be removed.

        Raises:
            ValueError: If no vehicle in the list of vehicles.
        """
        check_type(vehicle, Vehicle)
        if vehicle not in self.list_of_vehicles:
            raise ValueError(f'Vehicle {vehicle} is not in list of vehicles at the moment')
        self.list_of_vehicles.remove(vehicle)

    def get_free_places(self) -> int:
        """Get free places on parking.

        Returns:
            int: Number of free places on parking
        """
        return self.capacity - len(self.list_of_vehicles)

    def get_list_of_all_vehicles(self) -> list:
        """Get list of all vehicles.

        Returns:
            list: List of Vehicles.
        """
        return list(self.list_of_vehicles)
