class Car:
    def __init__(self, model, year, cost):
        self._model = model
        self._year = year
        self._cost = cost

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

class PassengerCar(Car):
    def __init__(self, model, year, cost, passenger_seats):
        super().__init__(model, year, cost)
        self._passenger_seats = passenger_seats

    @property
    def passenger_seats(self):
        return self._passenger_seats

    @passenger_seats.setter
    def passenger_seats(self, value):
        self._passenger_seats = value

    
class Truck(Car):
    def __init__(self, model, year, cost, carrying_capacity):
        super().__init__(model, year, cost)
        self._carrying_capacity = carrying_capacity

    @property
    def carrying_capacity(self):
        return self._carrying_capacity

    @carrying_capacity.setter
    def carrying_capacity(self, value):
        self._carrying_capacity = value