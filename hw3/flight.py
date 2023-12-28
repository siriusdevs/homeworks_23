"""Module with Flight class."""

import check_functions as check


class Flight:
    """A class that describes the flight with flight number passing from the departure airport \
        to the arrival airport."""

    def __init__(self, flight_number: str, departure_airport: str, arrival_airport: str) -> None:
        """Initialize a Flight instance.

        Args:
            flight_number (str): flight number.
            departure_airport (str): departure airport.
            arrival_airport (str): arrival airport.
        """
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport

    @property
    def flight_number(self) -> str:
        """Get fhe flight_number.

        Returns:
            str: flight_number.
        """
        return self._flight_number

    @flight_number.setter
    def flight_number(self, new_flight_number: str) -> None:
        """Set the flight_number.

        Args:
            new_flight_number (str): new flight_number value.
        """
        check.check_flight_number(new_flight_number)
        self._flight_number = new_flight_number

    @property
    def departure_airport(self) -> str:
        """Get the departure_airport.

        Returns:
            str: departure_airport.
        """
        return self._departure_airport

    @departure_airport.setter
    def departure_airport(self, new_departure_airport: str) -> None:
        """Set the departure_airport.

        Args:
            new_departure_airport (str): new departure_airport value.
        """
        check.check_airport_name(new_departure_airport)
        self._departure_airport = new_departure_airport

    @property
    def arrival_airport(self) -> str:
        """Get the arrival_airport.

        Returns:
            str: arrival_airport.
        """
        return self._arrival_airport

    @arrival_airport.setter
    def arrival_airport(self, new_arrival_airport: str) -> None:
        """Set the arrival_airport.

        Args:
            new_arrival_airport (str): new arrival_airport value.
        """
        check.check_airport_name(new_arrival_airport)
        self._arrival_airport = new_arrival_airport
