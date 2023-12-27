"""Module that contains Ticket class."""

from . import hw3
from .flight import Flight
from .passenger import Passenger


class Ticket:
    """Class that provides ticket which contains flight and passenger."""

    def __init__(self, ticket_id: int, flight: Flight, passenger: Passenger) -> None:
        """Initialize ticket.

        Args:
            ticket_id (int): ticket identation number
            flight (Flight): the flight which the ticket belongs
            passenger (Passenger): passenger which have this ticket
        """
        self.ticket_id = ticket_id
        self.flight = flight
        self.passenger = passenger

    @property
    def ticket_id(self) -> int:
        """Getter for ticket id.

        Returns:
            _ticket_id (int): ticket identation number
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, new_ticket_id: int) -> None:
        """Setter for ticket id.

        Args:
            new_ticket_id (int): new ticket identation number

        Raises:
            InvalidType: when new_ticket_id type isn't int
            NegativeNumber: when new_ticket_id less than zero or equal
        """
        if not isinstance(new_ticket_id, int):
            raise hw3.InvalidType(new_ticket_id, int)
        if new_ticket_id <= 0:
            raise hw3.NegativeNumber(new_ticket_id)
        self._ticket_id = new_ticket_id

    @property
    def flight(self) -> Flight:
        """Getter for flight.

        Returns:
            _flight (Flight): plane flight
        """
        return self._flight

    @flight.setter
    def flight(self, new_flight: Flight) -> None:
        """Setter for flight.

        Args:
            new_flight (Flight): new plane flight

        Raises:
            InvalidType: when new_flight type isn't Flight
        """
        if not isinstance(new_flight, Flight):
            raise hw3.InvalidType(new_flight, Flight)
        self._flight = new_flight

    @property
    def passenger(self) -> Passenger:
        """Getter for passenger.

        Returns:
            _passenger (Passenger): airplane passenger
        """
        return self._passenger

    @passenger.setter
    def passenger(self, new_passenger: Passenger) -> None:
        """Setter for passenger.

        Args:
            new_passenger (Passenger): new airplane passenger

        Raises:
            InvalidType: when new_passenger type isn't Passenger
        """
        if not isinstance(new_passenger, Passenger):
            raise hw3.InvalidType(new_passenger, Passenger)
        self._passenger = new_passenger
