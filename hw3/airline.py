"""Module that contains Airline class."""

from . import hw3
from .flight import Flight
from .passenger import Passenger
from .ticket import Ticket


class Airline:
    """Class that represents aircompany."""

    def __init__(
        self,
        name: str,
        flights: list[Flight],
        passengers: list[Passenger],
        tickets: list[Ticket],
    ) -> None:
        """Initialize Airline.

        Args:
            name (str): name of airline
            flights (list[Flight]): list of flights.
            passengers (list[Passenger]): list of passengers.
            tickets (list[Ticket]): list of lickets.
        """
        self.name = name
        self.flights = flights if flights else []
        self.passengers = passengers if passengers else []
        self.tickets = tickets if tickets else []

    @property
    def name(self) -> str:
        """Getter for airline name.

        Returns:
            _name (str): airline current name
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Setter for airline name.

        Args:
            new_name (str): new name for airline

        Raises:
            InvalidType: when new_name type is not str
        """
        if not isinstance(new_name, str):
            raise hw3.InvalidType(new_name, str)
        self._name = new_name

    @property
    def flights(self) -> list[Flight]:
        """Getter for list of flights.

        Returns:
            _flights (list[Flight]): list of flights
        """
        return self._flights

    @flights.setter
    def flights(self, new_flights: list[Flight]) -> None:
        """Setter for list of flights.

        Args:
            new_flights (list[Flight]): new list of flights

        Raises:
            InvalidType: when new_flights type is not list
            InvalidType: when not all elements of the list are type Flight
        """
        if not isinstance(new_flights, list):
            raise hw3.InvalidType(new_flights, list)
        for flight in new_flights:
            if not isinstance(flight, Flight):
                raise hw3.InvalidType(flight, Flight)
        self._flights = new_flights

    @property
    def passengers(self) -> list[Passenger]:
        """Getter for list of passengers.

        Returns:
            _passengers(list[Passenger]): list of passengers
        """
        return self._passengers

    @passengers.setter
    def passengers(self, new_passengers: list[Passenger]) -> None:
        """Setter for list of passengers.

        Args:
            new_passengers (list[Passenger]): new list of passengers

        Raises:
            InvalidType: when new_passengers type is not list
            InvalidType: when not all elements of the list are type Passenger
        """
        if not isinstance(new_passengers, list):
            raise hw3.InvalidType(new_passengers, list)
        for passenger in new_passengers:
            if not isinstance(passenger, Passenger):
                raise hw3.InvalidType(passenger, Passenger)
        self._passengers = new_passengers

    @property
    def tickets(self) -> list[Ticket]:
        """Getter for list of tickets.

        Returns:
            _tickets(list[Ticket]): list of tickets
        """
        return self._tickets

    @tickets.setter
    def tickets(self, new_tickets: list[Ticket]) -> None:
        """Setter for list of tickets.

        Args:
            new_tickets (list[Ticket]): new list of tickets

        Raises:
            InvalidType: when new_tickets type is not list
            InvalidType: when not all elements of the list are type Ticket
        """
        if not isinstance(new_tickets, list):
            raise hw3.InvalidType(new_tickets, list)
        for ticket in new_tickets:
            if not isinstance(ticket, Ticket):
                raise hw3.InvalidType(ticket, Ticket)
        self._tickets = new_tickets

    def add_flight(self, new_flight: Flight) -> None:
        """Add new flight.

        Args:
            new_flight (Flight): new flight

        Raises:
            InvalidType: when new_flight type is not Flight
        """
        if not isinstance(new_flight, Flight):
            raise hw3.InvalidType(new_flight, Flight)
        self._flights.append(new_flight)

    def del_flight(self, flight: Flight) -> None:
        """Delete flight.

        Args:
            flight (Flight): flight for delete

        Raises:
            InvalidType: when flight type is not Flight
            ValueError: when flight not in the list
        """
        if not isinstance(flight, Flight):
            raise hw3.InvalidType(flight, Flight)
        if flight not in self._flights:
            raise ValueError(f'{flight} not in the list')
        self._flights.remove(flight)

    def add_passenger(self, new_passenger: Passenger) -> None:
        """Add new passenger.

        Args:
            new_passenger (Passenger): new passenger

        Raises:
            InvalidType: when new_passenger type is not Passenger
        """
        if not isinstance(new_passenger, Passenger):
            raise hw3.InvalidType(new_passenger, Passenger)
        self._passengers.append(new_passenger)

    def del_passenger(self, passenger: Passenger) -> None:
        """Delete passenger.

        Args:
            passenger (Passenger): passenger for delete

        Raises:
            InvalidType: when passenger type is not Passenger
            ValueError: when passenger not in the list
        """
        if not isinstance(passenger, Passenger):
            raise hw3.InvalidType(passenger, Passenger)
        if passenger not in self._passengers:
            raise ValueError(f'{passenger} not in the list')
        self._passengers.remove(passenger)

    def buy_ticket(self, new_ticket: Ticket) -> None:
        """Add new ticket.

        Args:
            new_ticket (Ticket): new ticket

        Raises:
            InvalidType: when new_ticket type is not Ticket
        """
        if not isinstance(new_ticket, Ticket):
            raise hw3.InvalidType(new_ticket, Ticket)
        self._tickets.append(new_ticket)

    def cancel_ticket(self, ticket) -> None:
        """Delete ticket.

        Args:
            ticket (Ticket): ticket for delete

        Raises:
            InvalidType: _description_
            ValueError: _description_
        """
        if not isinstance(ticket, Ticket):
            raise hw3.InvalidType(ticket, Ticket)
        if ticket not in self._passengers:
            raise ValueError(f'{ticket} not in the list')
        self._tickets.remove(ticket)
