"""Module that provides the Aviacompany class."""

from . import hw3
from .flight import Flight
from .passenger import Passenger
from .ticket import Ticket


class Aviacompany:  # noqa: WPS214
    """Represents an aviacompany that aggregates its flights, passengers and tickets."""

    def __init__(
        self,
        name: str,
        flights: list[Flight],
        passengers: list[Passenger],
        tickets: list[Ticket],
    ) -> None:
        """Initialize an aviacompany.

        Args:
            name: full name of the aviacompany, unrestricted
            flights: list of flights that this aviacompany has
            passengers: list of passengers that are served by this aviacompany
            tickets: list of tickets that were bought
        """
        self.name = name
        self.flights = flights
        self.passengers = passengers
        self.tickets = tickets

    def add_flight(self, flight: Flight) -> None:
        """Add new flight.

        Args:
            flight: new flight
        """
        self.flights += [flight]

    def delete_flight(self, flight: Flight) -> None:
        """Delete a flight.

        If it is not inside flights list, raise ValueError.

        Args:
            flight: flight to delete
        """
        try:
            self.flights.remove(flight)
        except ValueError:
            raise ValueError(f'unable to find flight {flight} in current flights')

    @property
    def name(self) -> str:
        """Getter for name.

        Returns:
            str: name
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Setter for name.

        Args:
            name: new name
        """
        hw3.check_type(name, str)
        self._name = name

    @property
    def flights(self) -> list[Flight]:
        """Getter for flights.

        Returns:
            List[Flight]: list of flights this aviacompany currently has
        """
        return self._flights

    @flights.setter
    def flights(self, flights: list[Flight]) -> None:
        """Setter for flights.

        Args:
            flights: new list of all flights this aviacompany has
        """
        hw3.check_type(flights, list)
        hw3.check_elements_types(flights, Flight)
        self._flights = flights

    @property
    def passengers(self) -> list[Passenger]:
        """Getter for passengers.

        Returns:
            list[Passenger]: list of passengers this aviacompany serves
        """
        return self._passengers

    @passengers.setter
    def passengers(self, passengers: list[Passenger]) -> None:
        """Setter for passengers.

        Args:
            passengers: new list of passengers this aviacompany serves
        """
        hw3.check_type(passengers, list)
        hw3.check_elements_types(passengers, Passenger)
        self._passengers = passengers

    @property
    def tickets(self) -> list[Ticket]:
        """Getter for tickets.

        Returns:
            list[Ticket]: list of tickets that were bought from this company
        """
        return self._tickets

    @tickets.setter
    def tickets(self, tickets: list[Ticket]) -> None:
        """Setter for tickets.

        Args:
            tickets: new list of tickets
        """
        self._tickets = tickets
