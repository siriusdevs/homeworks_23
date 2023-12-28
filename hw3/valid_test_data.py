"""Module with valid data for test classes."""


from flight import Flight
from passenger import Passenger
from ticket import Ticket

valid_flights_list = [
    [
        Flight('AB1', 'Sochi', 'Samara'),
        Flight('CD23', 'Samara', 'Orenburg'),
    ],
    [
        Flight('CD23', 'Samara', 'Orenburg'),
        Flight('AB1', 'Sochi', 'Samara'),
    ],
]

valid_passengers_list = [
    [
        Passenger('Danilov Ilya Alekseevich', 1234567890),
        Passenger('Romodanov Denis Denisovich', 1122334455),
    ],
    [
        Passenger('Romodanov Denis Denisovich', 1122334455),
        Passenger('Danilov Ilya Alekseevich', 1234567890),
    ],
]

valid_tickets_list = [
    [
        Ticket(1234567890123, valid_flights_list[0][0], valid_passengers_list[0][0]),
        Ticket(1122334455667, valid_flights_list[0][1], valid_passengers_list[0][1]),
    ],
    [
        Ticket(1122334455667, valid_flights_list[1][0], valid_passengers_list[1][0]),
        Ticket(1234567890123, valid_flights_list[1][1], valid_passengers_list[1][1]),
    ],
]
