"""Airline module, uses aggregation Passenger, Flight -> Ticket -> Airline."""


from typing import Any


def check(new_value: Any, class_: type) -> None:
    """Check if new value is an instance of a class.

    Args:
        new_value (Any): New value of an object.
        class_ (type): Class to compare with.

    Raises:
        TypeError: When new value of an object doesn't match with given class.
    """
    if not isinstance(new_value, class_):
        value_type = type(new_value).__name__
        raise TypeError(f'{new_value} must be {class_.__name__} instance, got {value_type}')


class Passenger:
    """Passenger of a flight. Has passport (id)."""

    def __init__(self, name: str, passport_id: str) -> None:
        """Create a passenger with name and passport.

        Args:
            name (str): Passenger's name.
            passport_id (str): Passport ID of a passenger.
        """
        self.name, self.passport_id = name, passport_id

    @property
    def name(self) -> str:
        """Name of a passenger.

        Returns:
            str: Name.
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Set new name of a passenger.

        Args:
            name (str): New name.
        """
        check(name, str)
        self._name = name

    @property
    def passport_id(self) -> str:
        """Passport ID of a passenger.

        Returns:
            str: Passport ID.
        """
        return self._passport_id

    @passport_id.setter
    def passport_id(self, new_id: str):
        """Set new numeric passport ID of a passenger, must be six-digit number.

        Args:
            new_id (str): New 6-digit passport ID.

        Raises:
            ValueError: When ID isn't 6 characters long.
            ValueError: When ID contains non-digit characters.
        """
        check(new_id, str)
        id_length = len(new_id)
        if id_length != 6:
            raise ValueError(f'Passport ID must contain 6 characters, got {id_length}')
        if not all(char.isdigit() for char in new_id):
            raise ValueError(f'Passport ID must contain digits only, got {new_id}')
        self._passport_id = new_id


class Flight:
    """A flight of an Airline containing Passenger instances."""

    def __init__(self, flight_id: str, from_airport: str, to_airport: str) -> None:
        """Create a flight instance.

        Args:
            flight_id (str): ID of a Flight.
            from_airport (str): Departure.
            to_airport (str): Destination.
        """
        self.flight_id = flight_id
        self.from_airport = from_airport
        self.to_airport = to_airport

    @property
    def flight_id(self) -> str:
        """Get ID of the Flight.

        Returns:
            str: Flight's ID.
        """
        return self._flight_id

    @flight_id.setter
    def flight_id(self, new_id: str) -> None:
        """Set new ID for the Flight.

        Args:
            new_id (str): Flight's new ID
        """
        check(new_id, str)
        self._flight_id = new_id

    @property
    def from_airport(self) -> str:
        """Get the departure airport.

        Returns:
            str: Where from does the flight head off.
        """
        return self._from_airport

    @from_airport.setter
    def from_airport(self, new_airport: str) -> None:
        """Set new departure airport.

        Args:
            new_airport (str): New departure airport.
        """
        check(new_airport, str)
        self._from_airport = new_airport

    @property
    def to_airport(self) -> str:
        """Get the destination airport.

        Returns:
            str: Where does the flight arrive at.
        """
        return self._to_airport

    @to_airport.setter
    def to_airport(self, new_airport: str) -> None:
        """Set new destination airport.

        Args:
            new_airport (str): New destination airport.
        """
        check(new_airport, str)
        self._to_airport = new_airport


class Ticket:
    """Ticket neccesary for attending a flight."""

    def __init__(self, flight: Flight, passenger: Passenger, ticket_id: str) -> None:
        """Create Passenger's ticket for a Flight.

        Args:
            flight (Flight): Flight where the ticket is used.
            passenger (Passenger): Owner of the ticket.
            ticket_id (str): ID of a ticket.
        """
        self.flight = flight
        self.passenger = passenger
        self.ticket_id = ticket_id

    @property
    def flight(self) -> Flight:
        """Get flight where the ticket is used.

        Returns:
            Flight: The flight.
        """
        return self._flight

    @flight.setter
    def flight(self, new_flight: Flight) -> None:
        """Set new flight for the ticket.

        Args:
            new_flight (Flight): New flight.
        """
        check(new_flight, Flight)
        self._flight = new_flight

    @property
    def passenger(self) -> Passenger:
        """Get Passenger who this ticket belongs to.

        Returns:
            Passenger: Owner of the ticket.
        """
        return self._passenger

    @passenger.setter
    def passenger(self, passenger: Passenger) -> None:
        """Set new Passenger who this ticket belongs to.

        Args:
            passenger (Passenger): New ticket's owner.
        """
        check(passenger, Passenger)
        self._passenger = passenger

    @property
    def ticket_id(self) -> str:
        """Get the ID of a ticket.

        Returns:
            str: Ticket's ID.
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, new_id: str) -> None:
        """Set new ticket's ID.

        Args:
            new_id (str): New ID of a Ticket.
        """
        check(new_id, str)
        self._ticket_id = new_id


class Airline:
    """A company that aggregates Flights, Passengers and Tickets."""

    def __init__(
        self,
        title: str,
        flights: list[Flight],
        passengers: list[Passenger],
        tickets: list[Ticket],
    ) -> None:
        """Create an airline with Flights, Passengers and Tickets.

        Args:
            title (str): Title of the company.
            flights (list[Flight]): List of Flights this Airline serves.
            passengers (list[Passenger]): List of Passengers.
            tickets (list[Ticket]): List of Ttickets.
        """
        self.title = title
        self.flights = flights
        self.passengers = passengers
        self.tickets = tickets

    @property
    def title(self) -> str:
        """Title of the Airline.

        Returns:
            str: Name of the aviacompany.
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Set new title of the Airline.

        Args:
            title (str): New Airline's name.
        """
        check(title, str)
        self._title = title

    @property
    def flights(self) -> list[Flight]:
        """Get all flights of an airline.

        Returns:
            list[Flight]: List containing every Airline's flight
        """
        return self._flights

    @flights.setter
    def flights(self, new_flights: list[Flight]) -> None:
        """Set new flights list for an Airline.

        Args:
            new_flights (list[Flight]): List of flights.
        """
        check(new_flights, list)
        for flight in new_flights:
            check(flight, Flight)
        self._flights = new_flights

    @property
    def passengers(self) -> list[Passenger]:
        """Get all passengers of an airline.

        Returns:
            list[Passenger]: List containing every Airline's passenger.
        """
        return self._passengers

    @passengers.setter
    def passengers(self, new_passengers: list[Passenger]) -> None:
        """Set new passengers list of an Airline.

        Args:
            new_passengers (list[Passenger]): List of passengers.
        """
        check(new_passengers, list)
        for passenger in new_passengers:
            check(passenger, Passenger)
        self._passengers = new_passengers

    @property
    def tickets(self) -> list[Ticket]:
        """Get all tickets of the Airline.

        Returns:
            list[Ticket]: List containing every sold Airline's ticket.
        """
        return self._tickets

    @tickets.setter
    def tickets(self, new_tickets: list[Ticket]) -> None:
        """Set new tickets list for an Airline.

        Args:
            new_tickets (list[Ticket]): List of tickets.
        """
        check(new_tickets, list)
        for ticket in new_tickets:
            check(ticket, Ticket)
        self._tickets = new_tickets

    def add_flight(self, flight: Flight) -> None:
        """Add a new Airline's flight.

        Args:
            flight (Flight): New flight.
        """
        check(flight, Flight)
        self._flights.append(flight)

    def remove_flight(self, flight: Flight) -> None:
        """Remove Airline's flight.

        Args:
            flight (Flight): Flight to be removed.

        Raises:
            ValueError: When Flight is not found in the current list.
        """
        if flight not in self._flights:
            raise ValueError(f'Flight {flight} was not found among current flights')
        self._flights.remove(flight)

    def add_passenger(self, passenger: Passenger) -> None:
        """Add a new Airline's passenger.

        Args:
            passenger (Passenger): New passenger.
        """
        check(passenger, Passenger)
        self._passengers.append(passenger)

    def remove_passenger(self, passenger: Passenger) -> None:
        """Remove Airline's passenger.

        Args:
            passenger (Passenger): Passenger to be removed.

        Raises:
            ValueError: When Passenger is not found in the current list.
        """
        if passenger not in self._passengers:
            raise ValueError(f'Passenger {passenger} was not found among current passengers')
        self._passengers.remove(passenger)

    def buy_ticket(self, ticket: Ticket):
        """Buy (add) Airline's ticket.

        Args:
            ticket (Ticket): Ticket to buy.
        """
        check(ticket, Ticket)
        self._tickets.append(ticket)

    def cancel_ticket(self, ticket: Ticket):
        """Cancel (remove) Airline's ticket.

        Args:
            ticket (Ticket): Ticket to be removed.

        Raises:
            ValueError: When Ticket is not found in the current list.
        """
        if ticket not in self._tickets:
            raise ValueError(f'Ticket {ticket} was not found among sold tickets')
        self._tickets.remove(ticket)
