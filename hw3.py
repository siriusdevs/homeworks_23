"""Module."""
from typing import Any


def check_type(elem: Any, _class: Any) -> None:
    try:
        if not isinstance(elem, _class):
            raise TypeError(f'Value {elem} is {type(elem).__name__}, expected {_class.__name__}')
    except TypeError as err:
        with open('errors_log.txt', 'w') as errors_file:
            errors_file.write(f'Произошла ошибка: {str(err)}\n')
        exit()

class Vehicle:
    def __init__(self, label: str, license_plate: str) -> None:
        self.label, self.license_plate = label, license_plate
    
    @property
    def label(self) -> str:
        return self._label
    
    @label.setter
    def label(self, new_label: str) -> None:
        check_type(new_label, str)
        self._label = new_label

    @property
    def license_plate(self) -> str:
        return self._license_plate
    
    @license_plate.setter
    def license_plate(self, new_l_p: str) -> None:
        check_type(new_l_p, str)
        self._license_plate = new_l_p

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.label} {self.license_plate}'


class Car(Vehicle):
    def __init__(self, label: str, license_plate: str, car_body: str) -> None:
        self.car_body = car_body
        super().__init__(label, license_plate)

    @property
    def car_body(self) -> str:
        return self._car_body
    
    @car_body.setter
    def car_body(self, new_car_body: str) -> None:
        check_type(new_car_body, str)
        self._car_body = new_car_body

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.label} {self.license_plate} {self.car_body}'


class Parking:
    def __init__(self, list_of_vehicles: list[Vehicle], capacity: int) -> None:
        self.capacity, self.list_of_vehicles = capacity, list_of_vehicles

    @property
    def capacity(self) -> int:
        return self._capacity
    
    @capacity.setter
    def capacity(self, new_capacity: int) -> None:
        check_type(new_capacity, int)
        self._capacity = new_capacity

    @property
    def list_of_vehicles(self) -> list[Vehicle]:
        return self._list_of_vehicles
    
    @list_of_vehicles.setter
    def list_of_vehicles(self, new_l_o_v: list[Vehicle]) -> None:
        check_type(new_l_o_v, list)
        try:
            if len(new_l_o_v) > self._capacity:
                raise ValueError(f'List of vehicles must be less than capacity')
        except ValueError as err:
            with open('errors_log.txt', 'w') as errors_file:
                errors_file.write(f'Произошла ошибка: {str(err)}\n')
            exit()
        for vehicle in new_l_o_v:
            check_type(vehicle, Vehicle)
        self._list_of_vehicles = new_l_o_v

    def add_vehicle(self, new_vehicle: Vehicle) -> None:
        check_type(new_vehicle, Vehicle)
        try:
            if len(self.list_of_vehicles) + 1 > self.capacity:
                raise ValueError(f'There is no parking space for a vehicle {new_vehicle}')
        except ValueError as err:
            with open('errors_log.txt', 'w') as errors_file:
                errors_file.write(f'Произошла ошибка: {str(err)}\n')
            exit()
        self.list_of_vehicles.append(new_vehicle)
    
    def remove_vehicle(self, vehicle: Vehicle):
        check_type(vehicle, Vehicle)
        try:
            if not vehicle in self.list_of_vehicles:
                raise ValueError(f'Vehicle {vehicle} is not in list of vehicle at the moment')
        except ValueError as err:
            with open('errors_log.txt', 'w') as errors_file:
                errors_file.write(f'Произошла ошибка: {str(err)}\n')
            exit()
        self.list_of_vehicles.remove(vehicle)

    def get_free_places(self) -> int:
        return self.capacity - len(self.list_of_vehicles)
    
    def get_list_of_vehicles(self) -> list[Vehicle]:
        return self.list_of_vehicles


