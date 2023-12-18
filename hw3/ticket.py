"""Module that provides the Ticket class."""

from . import hw3
from .flight import Flight
from .passenger import Passenger


class Ticket:
    """Class that provides an aeroflight ticket dataclass."""

    def __init__(self, ticket_id: str, passenger: Passenger, flight: Flight) -> None:
        """Initialize a Ticket.

        Args:
            ticket_id: unique ticket identifier
            passenger: Passenger who this ticket belongs to
            flight: flight this ticket is used on
        """
        self.ticket_id = ticket_id
        self.passenger = passenger
        self.flight = flight

    @property
    def ticket_id(self) -> str:
        """Getter for ticket_id.

        Returns:
            str: ticket_id
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id: str) -> None:
        hw3.check_type(ticket_id, str)
        self._ticket_id = ticket_id

    @property
    def passenger(self) -> Passenger:
        """Getter for passenger.

        Returns:
            Passenger: this ticket's passenger
        """
        return self._passenger

    @passenger.setter
    def passenger(self, passenger: Passenger) -> None:
        """Setter for passenger.

        Args:
            passenger: new passenger for this ticket
        """
        hw3.check_type(passenger, Passenger)
        self._passenger = passenger

    @property
    def flight(self) -> Flight:
        """Getter for flight.

        Returns:
            Flight: this ticket's flight
        """
        return self._flight

    @flight.setter
    def flight(self, new_flight: Flight) -> None:
        """Setter for flight.

        Args:
            new_flight: new flight for this ticket
        """
        hw3.check_type(new_flight, Flight)
        self._flight = new_flight
