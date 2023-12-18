"""Module that provides the Flight class."""

from . import hw3


class Flight:
    """Flight represents an avia flight from one airport to another."""

    def __init__(self, flight_id: str, from_airport: str, to_airport: str) -> None:
        """Initialize an instance of Flight.

        Args:
            flight_id (str): unique flight identifier
            from_airport (str): airport from which this flight starts
            to_airport (str): airport where this flight ends
        """
        self.flight_id = flight_id
        self.from_airport = from_airport
        self.to_airport = to_airport

    @property
    def flight_id(self) -> str:
        """Getter for flight_id.

        Returns:
            str: flight_id
        """
        return self._flight_id

    @flight_id.setter
    def flight_id(self, flight_id: str) -> None:
        """Setter for flight_id.

        Args:
            flight_id: new flight_id value
        """
        hw3.check_type(flight_id, str)
        self._flight_id = flight_id

    @property
    def from_airport(self) -> str:
        """Getter for from_airport.

        Returns:
            str: from_airport value
        """
        return self._from_airport

    @from_airport.setter
    def from_airport(self, from_airport: str) -> None:
        """Setter for from_airport.

        Args:
            from_airport (str): new from_airport value
        """
        hw3.check_type(from_airport, str)
        self._from_airport = from_airport

    @property
    def to_airport(self) -> str:
        """Getter for to_airport.

        Returns:
            str: to_airport value
        """
        return self._to_airport

    @to_airport.setter
    def to_airport(self, to_airport: str) -> None:
        """Setter for to_airport.

        Args:
            to_airport (str): new to_airport value
        """
        hw3.check_type(to_airport, str)
        self._to_airport = to_airport
