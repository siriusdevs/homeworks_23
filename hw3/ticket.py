"""Module with Ticket class."""


import check_functions as check
from flight import Flight
from passenger import Passenger


class Ticket:
    """A class that describes the ticket with ticket name, flight and passenger."""

    def __init__(self, ticket_number: int, flight: Flight, passenger: Passenger) -> None:
        """Initialize a Ticket instance.

        Args:
            ticket_number (int): number of the ticket.
            flight (Flight): .
            passenger (Passenger): .
        """
        self.ticket_number = ticket_number
        self.flight = flight
        self.passenger = passenger

    @property
    def ticket_number(self) -> int:
        """Get fhe ticket number.

        Returns:
            int: ticket number.
        """
        return self._ticket_number

    @ticket_number.setter
    def ticket_number(self, new_ticket_number: int) -> None:
        """Set the ticket number.

        Args:
            new_ticket_number (int): new ticket number value.
        """
        check.check_ticket_number(new_ticket_number)
        self._ticket_number = new_ticket_number

    @property
    def flight(self) -> Flight:
        """Get fhe flight related to the ticket.

        Returns:
            Flight: flight related to the ticket.
        """
        return self._flight

    @flight.setter
    def flight(self, new_flight: Flight) -> None:
        """Set the flight related to the ticket.

        Args:
            new_flight (Flight): new flight value related to the ticket.
        """
        check.check_type('new_flight', new_flight, Flight)
        self._flight = new_flight

    @property
    def passenger(self) -> Passenger:
        """Get fhe passenger related to the ticket.

        Returns:
            Passenger: passenger related to the ticket.
        """
        return self._passenger

    @passenger.setter
    def passenger(self, new_passenger: Passenger) -> None:
        """Set the passenger related to the ticket.

        Args:
            new_passenger (Passenger): new passenger value related to the ticket.
        """
        check.check_type('new_passenger', new_passenger, Passenger)
        self._passenger = new_passenger
