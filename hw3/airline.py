"""Module with Airline class."""


import check_functions as check
from flight import Flight
from passenger import Passenger
from ticket import Ticket


class Airline:
    """A class that describes the airline containing the airline name, \
        flights, passengers and tickets."""

    def __init__(
        self,
        airline_name: str,
        flights: list[Flight],
        passengers: list[Passenger],
        tickets: list[Ticket],
    ) -> None:
        """Initialize an Airline instance.

        Args:
            airline_name (str): name of the airline.
            flights (list[Flight]): airline flights.
            passengers (list[Passenger]): passengers flying on airline flights.
            tickets (list[Ticket]): airline tickets that are available for buying.
        """
        self.airline_name = airline_name
        self.flights = flights
        self.passengers = passengers
        self.tickets = tickets

    @property
    def airline_name(self) -> str:
        """Get fhe airline_name.

        Returns:
            str: airline_name.
        """
        return self._airline_name

    @airline_name.setter
    def airline_name(self, new_airline_name: str) -> None:
        """Set the airline_name.

        Args:
            new_airline_name (str): new airline_name value.
        """
        check.check_airline_name(new_airline_name)
        self._airline_name = new_airline_name

    @property
    def flights(self) -> list[Flight]:
        """Get fhe flights related to the airline.

        Returns:
            list[Flight]: flights related to the airline.
        """
        return self._flights

    @flights.setter
    def flights(self, new_flights: list[Flight]) -> None:
        """Set the flights related to the airline.

        Args:
            new_flights (list[Flight]): new flights values related to the airline.
        """
        check.check_type('new_flights', new_flights, list)
        for new_flight in new_flights:
            check.check_type('new_flight', new_flight, Flight)
        self._flights = new_flights

    @property
    def passengers(self) -> list[Passenger]:
        """Get fhe passengers related to the airline.

        Returns:
            list[Passenger]: passengers related to the airline.
        """
        return self._passengers

    @passengers.setter
    def passengers(self, new_passengers: list[Passenger]) -> None:
        """Set the passengers related to the airline.

        Args:
            new_passengers (list[Passenger]): new passengers values related to the airline.
        """
        check.check_type('new_passengers', new_passengers, list)
        for new_passenger in new_passengers:
            check.check_type('new_passenger', new_passenger, Passenger)
        self._passengers = new_passengers

    @property
    def tickets(self) -> list[Ticket]:
        """Get fhe tickets related to the airline.

        Returns:
            list[Ticket]: tickets related to the airline.
        """
        return self._tickets

    @tickets.setter
    def tickets(self, new_tickets: list[Ticket]) -> None:
        """Set the tickets related to the airline.

        Args:
            new_tickets (list[Ticket]): new tickets values related to the airline.
        """
        check.check_type('new_tickets', new_tickets, list)
        for new_ticket in new_tickets:
            check.check_type('new_ticket', new_ticket, Ticket)
        self._tickets = new_tickets

    def add_flight(self, flight_to_add: Flight) -> None:
        """Add a new flight to existing flights.

        Args:
            flight_to_add (Flight): new flight to add to existing flights.
        """
        check.check_type('flight_to_add', flight_to_add, Flight)
        self.flights.append(flight_to_add)

    def remove_flight(self, flight_to_remove: Flight) -> None:
        """Remove a flight from existing flights.

        Args:
            flight_to_remove (Flight): flight to remove from existing flights.
        """
        check.check_type('flight_to_remove', flight_to_remove, Flight)
        check.check_element_presence_in_elements(
            'flight_to_remove',
            flight_to_remove,
            'self.flights',
            self.flights,
        )
        self.flights.remove(flight_to_remove)

    def add_passenger(self, passenger_to_add: Passenger) -> None:
        """Add a new passenger to existing passengers.

        Args:
            passenger_to_add (Passenger): new passenger to add to existing passengers.
        """
        check.check_type('passenger_to_add', passenger_to_add, Passenger)
        self.passengers.append(passenger_to_add)

    def remove_passenger(self, passenger_to_remove: Passenger) -> None:
        """Remove a passenger from existing passengers.

        Args:
            passenger_to_remove (Passenger): passenger to remove from existing passengers.
        """
        check.check_type('passenger_to_remove', passenger_to_remove, Passenger)
        check.check_element_presence_in_elements(
            'passenger_to_remove',
            passenger_to_remove,
            'self.passengers',
            self.passengers,
        )
        self.passengers.remove(passenger_to_remove)

    def buy_ticket(self, ticket_to_buy: Ticket) -> None:
        """Buy a new ticket and remove it from the tickets available for buying.

        Args:
            ticket_to_buy (Ticket): new ticket to buy and \
                remove it from the tickets available for buying.
        """
        check.check_type('ticket_to_buy', ticket_to_buy, Ticket)
        check.check_element_presence_in_elements(
            'ticket_to_buy',
            ticket_to_buy,
            'self.tickets',
            self.tickets,
        )
        self.tickets.remove(ticket_to_buy)

    def remove_ticket(self, ticket_to_cancel: Ticket) -> None:
        """Cancel a ticket and add it to the tickets available for buying.

        Args:
            ticket_to_cancel (Ticket): ticket to cancel and \
                add it to the tickets available for buying.
        """
        check.check_type('ticket_to_cancel', ticket_to_cancel, Ticket)
        self.tickets.append(ticket_to_cancel)
