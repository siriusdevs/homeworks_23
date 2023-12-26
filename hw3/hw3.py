"""HW3 task."""


class BaseFlight:
    """Flight instance."""

    def __init__(self, flight_number: str, departure_airport: str, arrival_airport: str):
        """Flight initialisation.

        Args:
            flight_number (str): the number of flidht
            departure_airport (str): the airport of departure name
            arrival_airport (str): the the airport of arrive name
        """
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport

    @property
    def flight_number(self) -> str:
        """Getter of fight number of the instance.

        Returns:
            str: flight number
        """
        return self._flight_number

    @flight_number.setter
    def flight_number(self, new_fn: str) -> None:
        """Setter of fight number of the instance.

        Args:
            new_fn (str): new flight number

        Raises:
            TypeError: if data wrong type
        """
        if not isinstance(new_fn, str):
            raise TypeError('Your flight number should be str')
        self._flight_number = new_fn

    @property
    def departure_airport(self) -> str:
        """Getter of departure airport of the instance.

        Returns:
            str: departure airport
        """
        return self._departure_airport

    @departure_airport.setter
    def departure_airport(self, new_da: str) -> None:
        """Setter of departore airport of the instance.

        Args:
            new_da (str): new departure airport

        Raises:
            TypeError: if data wrong type
        """
        if not isinstance(new_da, str):
            raise TypeError('Your departure airport should be str')
        self._departure_airport = new_da

    @property
    def arrival_airport(self) -> str:
        """Getter of arrival airport of the instance.

        Returns:
            str: arrival airport
        """
        return self._arrival_airport

    @arrival_airport.setter
    def arrival_airport(self, new_aa: str) -> None:
        """Setter of arrival airport of the instance.

        Args:
            new_aa (str): new arrival airport

        Raises:
            TypeError: if data wrong type
        """
        if not isinstance(new_aa, str):
            raise TypeError('Your arrival airport should be str')
        self._arrival_airport = new_aa


class FlightStr(BaseFlight):
    """Flight metod instance."""

    def __str__(self) -> str:
        """Representation of the instance in string.

        Returns:
            str: string visualisation of the instance.
        """
        return f'{self.flight_number} {self.departure_airport} {self.arrival_airport}'


class Passenger:
    """Passenger instance."""

    def __init__(self, name: str, passport_number: int):
        """Passenger initialization.

        Args:
            name (str): passenger name
            passport_number (int): passenger number of passport
        """
        self.name = name
        self.passport_number = passport_number

    @property
    def name(self) -> str:
        """Getter of passenger name of the instance.

        Returns:
            str: passenger name
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Setter of passenger name of the instance.

        Args:
            new_name (str): new passenger name

        Raises:
            TypeError: if data wrong type
        """
        if not isinstance(new_name, str):
            raise TypeError('Your name should be str')
        self._name = new_name

    @property
    def passport_number(self) -> int:
        """Getter of passport number of the instance.

        Returns:
            int: passport number
        """
        return self._passport_number

    @passport_number.setter
    def passport_number(self, new_pn: int) -> None:
        """Setter of passport number of the instance.

        Args:
            new_pn (int): new passport number

        Raises:
            TypeError: if data wrong type
        """
        if not isinstance(new_pn, int):
            raise TypeError('Your passport number should be int')
        self._passport_number = new_pn

    def __str__(self) -> str:
        """Representation of the instance in string.

        Returns:
            str: string visualisation of the instance.
        """
        return f'{self.name} {self.passport_number}'


class TicketMetod:
    """Ticket metod instance."""

    def __str__(self) -> str:
        """Representation of the instance in string type.

        Returns:
            str: string visualisation of the instance.
        """
        return f'{self.ticket_number} {self.flight} {self.passenger}'


class Ticket(TicketMetod):
    """Ticket instance."""

    def __init__(self, ticket_number: str, flight: BaseFlight, passenger: Passenger):
        """Ticket initializaition.

        Args:
            ticket_number (str): info about number of passenger ticket
            flight (BaseFlight): info about flight class (data from that class)
            passenger (Passenger): info aboutpassenger class (data from that class)
        """
        self.ticket_number = ticket_number
        self.flight = flight
        self.passenger = passenger

    @property
    def ticket_number(self) -> str:
        """Getter of ticket number of the instance.

        Returns:
            str: ticket number
        """
        return self._ticket_number

    @ticket_number.setter
    def ticket_number(self, new_tn: str) -> None:
        """Setter of ticket number of the instance.

        Args:
            new_tn (str): new ticket number

        Raises:
            TypeError: if data wrong type
        """
        if not isinstance(new_tn, str):
            raise TypeError('Your ticket number should be str')
        self._ticket_number = new_tn

    @property
    def flight(self) -> FlightStr:
        """Getter of flight of the instance.

        Returns:
            FlightStr: flight class
        """
        return self._flight

    @flight.setter
    def flight(self, new_flight: BaseFlight) -> None:
        """Setter of flight of the instance.

        Args:
            new_flight (BaseFlight): new flight

        Raises:
            TypeError: if data wrong type
        """
        if not isinstance(new_flight, BaseFlight):
            raise TypeError('Your flight should be class Flight')
        self._flight = new_flight

    @property
    def passenger(self) -> Passenger:
        """Getter of passenger of the instance.

        Returns:
            Passenger: passenger class
        """
        return self._passenger

    @passenger.setter
    def passenger(self, new_passenger: Passenger) -> None:
        """Setter of passenger of the instance.

        Args:
            new_passenger (Passenger): new passenger

        Raises:
            TypeError: if data wrong type
        """
        if not isinstance(new_passenger, Passenger):
            raise TypeError('Your passenger should be class Passager')
        self._passenger = new_passenger


class AirlineSettersAndGetters:
    """Airline setters and getters instance."""

    @property
    def flights(self) -> list:
        """Getter of flights of the instance.

        Returns:
            list: list of flights
        """
        return self._flights

    @flights.setter
    def flights(self, new_fs: list) -> None:
        """Setter of flights of the instance.

        Args:
            new_fs (list): new flights

        Raises:
            TypeError: if data wrong type
        """
        if not isinstance(new_fs, list):
            raise TypeError('Your flights list should be list')
        self._flights = new_fs

    @property
    def passengers(self) -> list:
        """Getter of passrngers of the instance.

        Returns:
            list: list of passengers
        """
        return self._passengers

    @passengers.setter
    def passengers(self, new_ps: list) -> None:
        """Setter of passengers of the instance.

        Args:
            new_ps (list): new passengers

        Raises:
            TypeError: if data wrong type
        """
        if not isinstance(new_ps, list):
            raise TypeError('Your passengers list should be list')
        self._passengers = new_ps

    @property
    def tickets(self) -> list:
        """Getter of tickets of the instance.

        Returns:
            list: list of tickets
        """
        return self._tickets

    @tickets.setter
    def tickets(self, new_ts: list) -> None:
        """Setter of tickets of the instance.

        Args:
            new_ts (list): new tickets

        Raises:
            TypeError: if data wrong type
        """
        if not isinstance(new_ts, list):
            raise TypeError('Your tickets list should be list')
        self._tickets = new_ts


class AirlainMetods(AirlineSettersAndGetters):
    """Airline metods instance."""

    def add_flight(self, flight: FlightStr) -> None:
        """Add flight to flights list.

        Args:
            flight (FlightStr): addeble flight

        Raises:
            TypeError: if data wrong type
        """
        if not isinstance(flight, FlightStr):
            raise TypeError('Your flight should be class Flight')
        self.flights.append(flight)

    def remove_flight(self, flight: FlightStr) -> None:
        """Return flight from flights list.

        Args:
            flight (FlightStr): flight for remove

        Raises:
            TypeError: if data wrong type
            ValueError: if there no data for removing
        """
        if not isinstance(flight, BaseFlight):
            raise TypeError('Your flight should be class Flight')
        if flight not in self.flights:
            raise ValueError(f'Your flight {flight.flight_number} in your flights list')
        self.flights.remove(flight)

    def add_passenger(self, passenger: Passenger) -> None:
        """Add passenger for passengers list.

        Args:
            passenger (Passenger): adeble passenger

        Raises:
            TypeError: if data wrong type
        """
        if not isinstance(passenger, Passenger):
            raise TypeError('Your passenger should be class Passenger')
        self.passengers.append(passenger)

    def remove_passenger(self, passenger: Passenger) -> None:
        """Delete passenger from passengers list.

        Args:
            passenger (Passenger): passehger for remove

        Raises:
            TypeError: if data wrong type
            ValueError: if there no passenger for removing in passengers list
        """
        if not isinstance(passenger, Passenger):
            raise TypeError('Your passenger should be class Passenger')
        if passenger not in self.passengers:
            raise ValueError(f'There is not passenger {passenger.name} in your passengers list')
        self.passengers.remove(passenger)

    def buy_ticket(self, ticket: Ticket) -> None:
        """Add ticket to tickets list.

        Args:
            ticket (Ticket): adeble ticket

        Raises:
            TypeError: if data wrong type
        """
        if not isinstance(ticket, Ticket):
            raise TypeError('Your ticket should be class Ticket')
        self.tickets.append(ticket)

    def cancel_ticket(self, ticket: Ticket) -> None:
        """Remove ticket from tickets list.

        Args:
            ticket (Ticket): tiket to remove

        Raises:
            TypeError: if data wrong type
            ValueError: if there no ticket for removing in tickets list
        """
        if not isinstance(ticket, Ticket):
            raise TypeError('Your ticket should be class Ticket')
        if ticket not in self.tickets:
            raise ValueError(f'There is not ticket {ticket.ticket_number}')
        self.tickets.remove(ticket)


class Airline(AirlainMetods):
    """Ailine instance."""

    def __init__(
        self,
        airline_name: str,
        flights: list[BaseFlight],
        passengers: list[Passenger],
        tickets: list[Ticket],
    ) -> None:
        """Airline initialization.

        Args:
            airline_name (str): name of airline company
            flights (list[BaseFlight]): list of flights
            passengers (list[Passenger]): list of passsengers
            tickets (list[Ticket]): list of tickets
        """
        self.airline_name = airline_name
        self.flights = flights
        self.passengers = passengers
        self.tickets = tickets

    @property
    def airline_name(self) -> str:
        """Getter of airline name of the instance.

        Returns:
            str: airline name
        """
        return self._airline_name

    @airline_name.setter
    def airline_name(self, new_an: str) -> None:
        """Setter of airline name of the instance.

        Args:
            new_an (str): new airline name

        Raises:
            TypeError: if data wrong type
        """
        if not isinstance(new_an, str):
            raise TypeError('Your airline name should be str')
        self._airline_name = new_an

    def __str__(self) -> str:
        """Representation of the instance in string.

        Returns:
            str: string visualisation of the instance.
        """
        return f'{self.airline_name} {self.flights} {self.passengers} {self.tickets}'
